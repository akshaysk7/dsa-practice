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
