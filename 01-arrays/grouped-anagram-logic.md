# Group Anagrams

**Problem:** given a list of strings, group the anagrams together. Return a
list of lists. `["eat","tea","tan","ate","nat","bat"]` →
`[["eat","tea","ate"], ["tan","nat"], ["bat"]]`.

## Logic

1. One dict, `groups`, created once before the loop. It maps
   **signature → list of words with that signature**. This is the first
   problem where a dict value is a collection rather than a single number.

2. Loop over `strs`. Each pass gives one **whole word**, not a character —
   looping a list yields its items; looping a string yields its characters.
   The character-level work happens later, inside `sorted()`.

3. Compute the signature: `key = "".join(sorted(word))`.
   - `sorted(word)` returns a **list** of characters in order.
   - `"".join(...)` glues that list back into a string.
   - The join is required because dict keys must be hashable, and lists
     are mutable, so they can't be keys.

4. **The core insight — there is no anagram comparison happening.**
   Sorting is a *normalizing* step. Every member of an anagram family has
   exactly one sorted form, so `"cat"` and `"tac"` both produce the literal
   string `"act"` — not "similar", identical. Once they're the same string,
   an ordinary dict lookup does the grouping for free.

   Precisely: it groups by identical characters **in identical counts**.
   `"aab"` and `"abb"` share the same letters but sort differently, so they
   correctly land in separate groups.

5. Check-then-branch, same shape as the character-frequency warm-up:
   - key already present → `groups[key].append(word)` — reach into the dict
     to get the list stored there, then append to *that list*. The dict
     itself is never appended to; dicts have no `.append()`.
   - key absent → `groups[key] = [word]` — create a new one-item list.
     It must be a list, not a bare word, or the next `.append()` on that
     key would have nothing to call itself on.

6. `return list(groups.values())` — the keys were only ever scaffolding for
   grouping; the answer is the values. `.values()` returns a `dict_values`
   view object, not a real list, so `list(...)` converts it to the type the
   problem expects.

## Complexity

Let n = number of words, k = average word length.

- **Time: O(n · k log k)** — sorting each word costs k log k, done n times.
  The dict operations are O(1) each and don't dominate. This is the first
  problem where an operation *inside* the loop isn't constant time.
- **Space: O(n · k)** — every word ends up stored in the dict.

## The pattern

**When grouping items by a shared property: compute a value that is
identical for every member of the group, then use it as a dict key.**
The dict does the grouping. The only real work is inventing the right
signature.

## Gotchas hit

- `sorted(strs)` sorts the *list order*; `sorted(word)` sorts the *letters
  inside one word*. Needed the second one.
- `.get()` fetches one value by key; `.values()` fetches all of them.
- A test list with no actual anagram pairs makes correct code look broken —
  every word lands in its own group, which is the right answer for that
  input. Test data has to contain the case being tested.
  