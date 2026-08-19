# Contains Duplicate — brute force

**Problem:** given a list, return True if any value appears more than once, False if all values are unique.

## Logic

1. Take a list of numbers as input to a function.

2. Use two nested loops over the list's **indices**, not its values.
   `range(len(nums))` gives positions (0, 1, 2...), which is what lets us
   compare one position against another.

3. The outer loop (`i`) holds the reference element. The inner loop (`j`)
   runs fully for each single value of `i` — so when i=0, j sweeps the
   entire list, then i=1 and j sweeps again. That's what makes it n × n.

4. Two conditions must both hold before we declare a duplicate:
   - `j != i` — skip the case where an element is compared to itself,
     which would always be equal and give a false positive.
   - `nums[j] == nums[i]` — two different positions holding the same value.

5. If both hold, `return True` immediately. One match is enough to be
   certain, so there's no reason to keep checking.

6. `return False` sits **outside both loops**, at function level. This is
   the key placement: "no duplicates" can only be concluded after every
   pair has been checked. Putting it inside the loops would exit on the
   first non-matching pair and never see the rest of the list.

## Complexity

- **Time: O(n²)** — for each of n elements, we scan all n elements.
- **Space: O(1)** — no extra data structure; only loop counters.

## Note

There is a faster O(n) solution using a set. Written here as brute force
first, deliberately, to feel the cost difference.
---

# Optimised — set (one pass)

## Logic

1. Create an empty set inside the function. It records every value already
   walked past. **Inside**, not outside — a set at module level persists
   between calls and corrupts the second one.

2. Loop over the list once, taking values directly (no indices needed).

3. For each value, ask: is it already in the set?
   - **Yes** → it appeared earlier in the list → `return True`, function exits.
   - **No** → the `if` block is skipped, execution falls through to `.add()`,
     and the value is recorded for future passes.

4. **Key insight — the ordering does the work.** Check first, add second.
   The set only ever contains values from *previous* iterations, so an
   element can never match itself. This replaces the `j != i` guard the
   brute force needed. Reversing the order (add then check) would report
   a duplicate on the very first element.

5. `return False` outside the loop — reached only when every value has been
   checked and none repeated.

## Complexity

- **Time: O(n)** — one pass, and each `in` / `.add()` on a set is O(1).
- **Space: O(n)** — worst case (no duplicates) the set ends up holding
  every element.

## The trade

| Version | Time | Space |
|---|---|---|
| Brute force | O(n²) | O(1) |
| Set | O(n) | O(n) |

Speed bought with memory. The brute force stores nothing but rechecks
everything; the set remembers everything so it never rechecks.