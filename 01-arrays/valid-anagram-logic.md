# Valid Anagram

**Problem:** given two strings, return True if one is a rearrangement of the
other — same letters, same counts, any order.

## Logic

1. **Length check first.** If the two strings differ in length, one has
   letters the other can't account for. Return False immediately — O(1),
   and it rules out most non-anagrams before any counting happens.

2. **Build a frequency dict for each string.** Two empty dicts, two
   sequential loops. For each character: if it's already a key, increment
   its count; if not, create it with a count of 1. Same pattern as the
   character-frequency warm-up.

3. **Compare with `==`.** Two dicts are equal when they hold the same keys
   mapped to the same values. Key order is irrelevant, which is exactly
   right here — "anagram" and "nagaram" produce identical dicts despite
   completely different letter order.

4. `return count1 == count2` — the comparison itself is the answer, so it
   goes straight into the return.

## Watch out

- The two loops need **different loop variables** (`ch` and `ch1`). Reusing
  `ch` in the second loop silently indexes with a stale value from the
  first loop — no error, just wrong counts.
- Two loops one after another is **sequential, not nested**: n + n = O(n),
  not O(n²). Nesting multiplies; sequencing adds.

## Complexity

- **Time: O(n)** — two separate passes, each dict operation O(1).
- **Space: O(n)** — two dicts, each holding up to one entry per distinct
  character.

## Note

Python's `collections.Counter` does the whole counting loop in one call.
Written manually here to build the frequency-dict pattern by hand first.
