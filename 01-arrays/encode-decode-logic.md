# Encode and Decode Strings

**Problem:** `encode(list) → string`, `decode(string) → list`, exact round trip
for any input. `decode(encode(x)) == x` always.

---

## How I got to the format

**Step 1 — I found the break myself.** Ran `",".join(strs)` then `.split(",")`
in the REPL. Round-tripped fine on `["hello","world"]`. Then put a comma
*inside* a string:



**Two strings in, three out.** My own read of it: "wherever there are commas it
gets split into strings" — the separator and the data became
indistinguishable the moment they were joined.

**Step 2 — the realisation.** No character is safe, because a string may
contain any character. So the fix isn't a better separator. It has to be
structural.

**Step 3 — the format.** Record each string's *length* before its content:
`<length>#<string>`.

`["hello","my"]` → `"5#hello2#my"`

Decode never hunts for a terminator — it reads a number and **counts that many
characters**. A `#` inside the data is harmless, because `#` is only ever
looked for while reading a length, never while reading content.

---

## Encode

```python
def encode(strs):
    s = ""
    for st in strs:
        s = s + str(len(st)) + "#" + st
    return s
```

`for` is correct here — one pass per string, no position tracking needed.

### ⚠️ WHERE I WENT WRONG — concatenation order

I first wrote **two** lines inside the loop:

```python
s += st                          # ← redundant
s = str(len(st)) + "#" + s       # ← old s at the END
```

Output: `6#2#4#2#5#hellomynameisakshay` — every length bunched at the front,
every word at the back.

**Cause:** in line 2, `s` sits at the *end* of the expression, so each new
length got **prepended** instead of appended. And line 1 was adding the word
separately, without its prefix.

**How I found it:** traced `s` by hand, two passes:

| step | s |
|---|---|
| start | `""` |
| pass 1, line 1 | `"hello"` |
| pass 1, line 2 | `"5#hello"` |
| pass 2, line 1 | `"5#hellomy"` |
| pass 2, line 2 | `"2#5#hellomy"` |

Pass 2 made it obvious — `2#` jumped in front of `5#hello`.

**Lesson: order in a concatenation is not cosmetic.** `s + x` appends,
`x + s` prepends. Also: two lines both trying to build the same variable are
almost always fighting each other.

**I also slipped on the trace itself** — first read `s += st` as `s = st`.
`+=` accumulates; `=` replaces.

---

## Decode

```python
def decode(s):
    res = []
    i = 0
    while i < len(s):
        j = s.find("#", i)
        length = int(s[i:j])
        word = s[j+1 : j+1+length]
        res.append(word)
        i = j + 1 + length
    return res
```

### Why `while`, not `for`

Chunk sizes vary — `5#hello` is 7 characters, `2#my` is 4. A `for` over the
string hands back one character at a time with no way to skip what's already
been consumed.

| | `for` | `while` |
|---|---|---|
| Steps controlled by | the collection | me |
| Step size | one item, always | whatever I set |
| Can hang forever | no | yes, if the pointer doesn't move |

**First loop I've written that doesn't advance by one.**

### The four lines

1. `j = s.find("#", i)` — position of the next `#`. Second argument is where to
   start searching.
2. `length = int(s[i:j])` — the digits between `i` and `j`. The `#` is excluded
   for free, because slicing's stop is exclusive. `int()` because `"5"` is text
   and I need to count with it.
3. `word = s[j+1 : j+1+length]` — starts one past the `#`, runs `length`
   characters. **No searching.** The count was already known.
4. `i = j + 1 + length` — advance to the next chunk.

---

### ⚠️ WHERE I WENT WRONG — decode

**Threw away `find()`'s result.** Wrote `s.find("#", i)` on its own line. It
computes the position and discards it. Needs assigning to a name.

**Used `length` as a slice stop.** Wrote `s[j+1:length]` → on `"5#hello"`
that's `s[2:5]` = `"hel"`, three characters instead of five.
**A slice's second number is a position, not a count.** Start at `j+1`, want
`length` characters → stop at `j+1+length`.

**Reached for another loop to find where the word ends** — suggested a `while`
scanning until it hit a number. That defeats the entire format, and breaks on
words containing digits (`"abc123"`). **The length exists so that counting
replaces searching.**

**Off-by-one on the advance.** Tried `i = j+1+length+1`. On `"5#hello2#my"`
that lands on index 8 — the `#` — skipping the `2`. Then `int(s[8:8])` gets an
empty string and crashes.

**Thought `s[2:7]` included index 7.** It doesn't.

---

### 🔑 THE KEY INSIGHT — why `i = j+1+length` is exactly right

Two things, and both are needed:

1. **Slicing's stop is exclusive**, so `s[j+1 : j+1+length]` never consumed the
   character at index `j+1+length`. It's the first untouched character.
2. **The pointer must move forward** or the next iteration re-reads the same
   chunk — and `i < len(s)` stays true forever. Infinite loop.

So the *same expression* does two jobs: it's the slice's stopping point, and
it's the pointer's new home. That's not a coincidence — it's exactly because
the stop is exclusive that the two coincide.

---

## Complexity

n = number of strings, m = total characters.

- **Time: O(m)** — each character written once, read once.
- **Space: O(m)** — the encoded string plus the rebuilt list.

---

## What made this the hardest one so far

Not the rating — it's a Medium, same as Group Anagrams and Top K.

It's that **there was no data structure to pick.** Every previous problem had a
pattern to reach for: set for membership, dict for lookup, dict-with-computed-key
for grouping. This one is designing a format and writing its parser. Closer to
engineering than to pattern matching, and nothing in the previous ten problems
prepared me for it.

Also the first `while` loop with a manual pointer.
 