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
