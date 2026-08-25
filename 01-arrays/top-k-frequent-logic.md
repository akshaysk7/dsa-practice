# Top K Frequent Elements

**Problem:** given a list of numbers and an integer k, return the k numbers
that appear most often. `[1,1,1,2,2,3], k=2` → `[1,2]`.

**Status: submitted, 2 test cases failing.** Core approach is correct;
an edge case is unhandled. Revisit.

## Logic

Four operations chained — the first problem needing more than one idea.

1. **Count.** Standard frequency dict, same loop as the character-count
   warm-up. `[1,1,1,2,2,3]` → `{1:3, 2:2, 3:1}`.

2. **Flatten to pairs.** `count.items()` gives `[(1,3), (2,2), (3,1)]` —
   one pair per entry, key and count travelling together. Needed because
   sorting the values alone would lose track of *which number* each count
   belonged to, and the answer is the numbers, not the counts.

3. **Sort by count, descending.**
   `sorted(count.items(), key=lambda x: x[1], reverse=True)`
   - `key=` tells `sorted()` what to compare. Without it, it compares the
     first element of each pair — the number itself, not its count.
   - `lambda x: x[1]` is a throwaway one-line function: given a pair,
     hand back its second element.
   - `reverse=True` because `sorted()` goes smallest-first by default.

4. **Slice to k.** `sortd[:k]` takes the first k pairs. `k` is a function
   parameter — it varies per call, nothing hardcoded.

5. **Strip the counts.** Loop the sliced pairs, append `pair[0]` of each
   into a result list. Tuples index like lists.

## Key ideas

- **Sort by one thing, return another.** The count decides the order; the
  key is what gets returned. `.items()` is what keeps them attached so
  this is possible.
- `sorted(dict)` sorts only the **keys** — iterating a dict gives keys by
  default. `.items()` is required to get pairs.
- `return` both exits the function *and* hands a value back. `print` does
  neither — it displays text and returns `None`, which is why a printing
  function fails every grader test regardless of what appears on screen.

## Complexity

n = length of nums, m = number of distinct values (m ≤ n).

- **Time: O(n + m log m)** — O(n) to count, O(m log m) to sort the m
  distinct entries, O(k) to slice and strip. The sort dominates.
- **Space: O(m)** — the dict plus the sorted pair list.

There is a known O(n) approach (bucket sort by frequency) that avoids the
sort entirely. Not attempted here.

## Gotchas hit

- `count` is a dict, not a function — `count(...)` fails. Index with `[]`
  or call methods with `.`.
- `sorted()` needs the collection as its **first** argument, before any
  keyword arguments.
- No colon on an assignment line — colons only open blocks.