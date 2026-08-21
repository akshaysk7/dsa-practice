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