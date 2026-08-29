# DSA Practice

python solutions, organised by topic.

| Problem | Date | Pattern trigger |
|---|---|---|
| Character frequency count | 14 Aug | Counting/grouping repeated items → dict, keyed on the item itself 
| Largest number without max() | 14 Aug | Track a running "best so far"; update it only when a new value beats it — no else branch needed | 
| Common elements between two lists | 15 Aug | Comparing membership against a large collection repeatedly → convert to set first for O(1) lookup; use a set for the result too, to dedupe automatically |
| Reverse a list without .reverse() or slicing | 15 Aug | Build a new list backwards by inserting each item at index 0 (keep in mind the difference between insert and append) | 
| Contains Duplicate | 19 Aug | Compare every pair in one list → nested loop over indices with `j != i` guard; return True early, return False only after both loops finish |
| Contains Duplicate (set) | 20 Aug | "Have I seen this before?" → one pass with a `dup` set; check BEFORE adding, so the set only holds earlier elements and nothing matches itself |
|valid anagram|21 aug|Comparing composition of two collections regardless of order → build a frequency dict for each, compare with `==`; length check first as a cheap early exit |
| Two Sum (brute force) | 22 Aug | Find a pair meeting a condition → nested loop with inner starting at `i+1`; the bound itself prevents self-comparison and duplicate pairs, so no guard is needed |
| Two Sum (dict) | 23 Aug | Need a partner value AND its position → dict of {number: index}. `dict1[num] = i` files each element's index under the number itself; later, `dict1[target-num]` opens that same drawer and hands the index back. It returns an index only because an index was stored — the dict computes nothing, it just retrieves what a previous pass filed |
| Group Anagrams | 24 Aug | Grouping by a shared property → compute a signature identical for all group members (`"".join(sorted(w))`) and use it as a dict key; dict value is a list, so append to `groups[key]`, not to `groups` |
| Top K Frequent Elements | 26 Aug | Rank by a derived value but return something else → `.items()` to keep key and count attached, `sorted(key=lambda x: x[1], reverse=True)` to order by count, slice `[:k]`, then extract the keys |
| Encode and Decode Strings | 29 Aug | No separator is safe — data may contain any character, so join/split corrupts (`["hello,world","test"]` → 3 items). Fix is structural: length-prefix `<len>#<str>`, so decode **counts instead of searching**. Needs `while` + manual pointer since chunk sizes vary. `i = j+1+length` works because slicing's stop is exclusive — that index was never consumed, so it's already the next chunk's first character. Watch: slice stop is a *position*, not a count |
