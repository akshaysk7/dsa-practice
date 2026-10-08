# Product of Array Except Self

**Problem:** return a list where position i holds the product of every element
except `nums[i]`. `[1,2,3,4]` → `[24,12,8,6]`.

**Constraints:** no division, target O(n).

---

## Why division is banned

If allowed, it's three lines: total product, then divide by each element.

Then `[1,2,0,4]` arrives. Total product is 0, so every answer becomes 0 — but
position 2 should be 1×2×4 = 8. And dividing *by* the zero crashes outright.

Zeros break division-based approaches. The ban forces an approach that handles
them naturally — and both solutions below do, without any special-casing.

---

## Brute force — O(n²)

```python
def productExceptSelf(nums):
    result = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if j != i:
                product *= nums[j]
        result.append(product)
    return result
```

- `i` = which answer is being built
- `j` = which element is being considered for multiplication
- `product` = running total for the current `i`

**`product = 1` sits between the loops** — inside the outer, outside the inner.
Before the outer loop it would never reset; inside the inner loop it would
reset every step and destroy the accumulation.

**Why 1 and not 0:** 1 is multiplication's identity. Starting at 0 keeps
everything 0 forever.

`j != i` is the same skip guard used in Contains Duplicate's brute force.

### The waste

For `[1,2,3,4]`, position 0 computes 2×3×4 and position 1 computes 1×3×4.
Both multiply 3×4. Every pass rebuilds from scratch — 16 multiplications for
4 answers. That repetition is what the O(n) version eliminates.

---

## Optimised — prefix/suffix, O(n)

### The insight

Every answer splits in two:

| position | LEFT of it | RIGHT of it | product |
|---|---|---|---|
| 0 | (nothing) → 1 | 2×3×4 = 24 | 24 |
| 1 | 1 | 3×4 = 12 | 12 |
| 2 | 1×2 = 2 | 4 | 8 |
| 3 | 1×2×3 = 6 | (nothing) → 1 | 6 |

**answer[i] = (product of everything before i) × (product of everything after i)**

Empty side = 1, same identity reasoning as the accumulator.

And critically: reading down the LEFT column — 1, 1, 2, 6 — each value is the
previous one times one more element. Nothing needs recomputing. Carry a
running product instead of restarting.

### Pass 1 — left to right

```python
result = []
product = 1
for i in range(len(nums)):
    result.append(product)
    product *= nums[i]
```

| i | append | product becomes |
|---|---|---|
| 0 | 1 | 1 |
| 1 | 1 | 2 |
| 2 | 2 | 6 |
| 3 | 6 | 24 |

→ `[1, 1, 2, 6]`

### Pass 2 — right to left

```python
product = 1
for j in range(len(nums)-1, -1, -1):
    result[j] *= product
    product *= nums[j]
return result
```

| j | result[j] before | × product | result[j] after | product becomes |
|---|---|---|---|---|
| 3 | 6 | ×1 | 6 | 4 |
| 2 | 2 | ×4 | 8 | 12 |
| 1 | 1 | ×12 | 12 | 24 |
| 0 | 1 | ×24 | 24 | 24 |

→ `[24, 12, 8, 6]`

`range(len(nums)-1, -1, -1)` — start at the last index, stop before -1 (so 0 is
included), step backwards by 1.

---

## 🔑 THE KEY IDEA — write before multiplying

In both passes: **append/update first, then grow the running product.**

Writing first means position i captures the product of everything encountered
*before* arriving there — excluding itself, automatically.

Multiply first and each position would include its own value, which is exactly
what the problem forbids.

**This replaces the `j != i` guard entirely.** The brute force checked and
skipped; here the *timing* handles exclusion structurally. No condition needed.

---

## Where I went wrong

**Put `product = 1` inside the single loop.** Correct placement in the brute
force (each `i` needs a fresh product), wrong here (the product must carry
across passes). Same line, opposite requirement, depending on structure.

**Multiplied before appending.** Position i then included itself — the one
thing the problem rules out.

**`result.append(i)`** — appended the loop counter instead of the accumulator.
Would have produced `[0,1,2,3]`.

**Forgot to reset `product` before pass 2.** It ended pass 1 holding 24 and
would have poisoned every suffix value.

**Reached for `+=` instead of `*=`** on the suffix growth.

**Thought the nested loop meant 2D arrays.** Nesting doesn't create a
dimension — `nums[j]` is still a flat list, and there's no `nums[i][j]`
anywhere.

---

## Complexity

| version | time | space |
|---|---|---|
| brute force | O(n²) | O(n) |
| prefix/suffix | O(n) | O(n) |

Two sequential loops = n + n = O(n). **Sequential adds, nested multiplies** —
same distinction as Valid Anagram's two loops.

The output list isn't usually counted as extra space, since it's the required
return value. By that convention the optimised version is O(1) auxiliary space.

---

## The pattern

**When each answer depends on "everything except this one," split it into
everything-before × everything-after, and compute each side with a single
running pass.**

First prefix/suffix problem. Prefix sums (the additive version) appear in
weeks 2–3 of the roadmap.