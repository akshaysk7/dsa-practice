# Two Sum — brute force

**Problem:** given a list of numbers and a target, return the **indices** of
the two numbers that add up to the target. Exactly one solution exists, and
the same element can't be used twice.

## Logic

1. Two nested loops over **indices**, not values — the answer is a pair of
   positions, so `range(len(nums))` is needed rather than looping over
   values directly.

2. The inner loop starts at `i+1`, not 0. This does two jobs at once:
   - `j` can never equal `i`, so no self-comparison — **no `j != i` guard
     needed**, unlike Contains Duplicate. The loop bounds enforce it.
   - Each pair is checked once instead of twice. `(0,1)` and `(1,0)` are
     the same pair for addition, so checking both is wasted work.

3. For each pair, test whether `nums[i] + nums[j] == target`. If yes,
   `return [i, j]` immediately — the problem guarantees one solution, so
   there's nothing left to look for.

4. `return []` sits outside both loops. Reached only if every pair has been
   checked and none matched. Same placement rule as `return False` in
   Contains Duplicate: a "checked everything, found nothing" line can never
   live inside the loop.

## Complexity

- **Time: O(n²)** — for each of n elements, scan the remaining elements.
  The `i+1` start halves the work to n(n-1)/2, but halving a constant
  doesn't change the growth class. Still quadratic.
- **Space: O(1)** — only loop counters, no extra structure.

Passes on LeetCode: the constraints (n ≤ 10⁴) are small enough that O(n²)
finishes in time. Unlike Contains Duplicate, where the same approach timed out.

## LeetCode submission gotchas

- `class Solution:` — **not** `class Solution(twoSum):`. Parentheses after a
  class name mean inheritance, so that form makes Python look for a class
  by that name and fail with a NameError.
- Method name must be exactly `twoSum` — capital S. Names are case-sensitive.
- No `print`, no test data. The harness supplies input and reads the return.


# SET VERSION OF TWO SUM

---

# Optimised — one pass with a dict

## Logic

1. Create an empty dict inside the function. It maps **number → index** for
   every element already walked past.

2. Loop once with `enumerate(nums)` — both the index and the value are
   needed: the value for arithmetic, the index for the answer.

3. For each element, compute the partner directly: `target - num`. No
   searching involved — if a pair exists, this is exactly the other half.

4. Ask the dict whether that partner has already been seen. `if target-num
   in dict1` — an O(1) check, not a scan.

5. **Found:** the answer is two indices. `i` is the current position;
   `dict1[target-num]` returns the position stored when that partner was
   walked past. Return `[dict1[target-num], i]`.

6. **Not found:** file the current element for future passes —
   `dict1[num] = i`. A later element may be looking for *this* one.

## The key idea

The dict does not compute anything. Line 6 writes `i` into the drawer
labelled `num`; step 5 opens a drawer and gets back whatever was filed
there. It returns an index solely because indices are what were stored —
storing anything else would return that instead.

Choosing the mapping is the real design decision. `{number: index}` works
because the search is *by value* and the answer needed is a *position*.
Flipping it to `{index: number}` would store fine and be useless.

## Why check before storing

The dict only ever holds elements from earlier passes, so an element can
never match itself. Same ordering rule as Contains Duplicate — and it's
also what makes `[3,3]` work: the first 3 is stored, the second finds it.

## Complexity

- **Time: O(n)** — one pass, O(1) dict operations throughout.
- **Space: O(n)** — the dict can end up holding every element.

Versus brute force: O(n²) time / O(1) space. Speed bought with memory again.

## Gotchas hit

- `range(...)` has no place here — it generates loop bounds, not a return
  value. The answer is a plain two-element list.
- No `else` needed. If the `if` fires, `return` exits; otherwise execution
  falls through to the store line.
- Storing `1` instead of `i` silently breaks everything: every lookup
  returns 1 regardless of position. The stored value must match what the
  return expects.