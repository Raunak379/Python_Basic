# Strings: Indexing & Slicing

A Python `str` is an **immutable sequence of characters**. "Sequence" is the key word — it means strings support the same indexing/slicing rules as lists and tuples.

## Indexing
Every character has a position (index), starting at **0** from the left, and **-1** from the right.

```
P   y   t   h   o   n
0   1   2   3   4   5
-6  -5  -4  -3  -2  -1
```

```python
name = "Python"
name[0]   # 'P'  (first)
name[-1]  # 'n'  (last)
name[6]   # IndexError: string index out of range (index 6 doesn't exist, max is 5)
```

Because strings are immutable, you **cannot** do `name[0] = "J"` — that raises `TypeError`. To "change" a character you must build a new string (e.g., slicing + concatenation).

### Looping with indices
`String.py` loops forward and backward using indices:
```python
for i in range(len(word)):      # forward: 0,1,2,...,len-1
    print(word[i])
for i in range(5, -1, -1):      # backward: 5,4,3,2,1,0 (hardcoded to word length 6)
```
Note the backward loop is hardcoded to `5` — it only works correctly for a 6-character word. A more robust version would use `range(len(word)-1, -1, -1)`.

## Slicing
Syntax: `sequence[start:stop:step]` — **stop is always exclusive**, and any of the three parts can be omitted (defaults: `start=0`, `stop=len`, `step=1`).

```python
word = "Programming"
word[0:3]    # 'Pro'   — first 3 chars
word[-3:]    # 'ing'   — last 3 chars (start from -3 to end)
word[1:]     # everything except first char
word[:-1]    # everything except last char
word[1:-1]   # everything except first AND last
word[::2]    # every 2nd char, start to end
word[::-1]   # the WHOLE string reversed (negative step walks backward)
word[-5:][::-1]   # last 5 chars, then reverse just that slice
```

**Why `[::-1]` reverses a sequence:** step `-1` means "walk backward," and omitting start/stop means "use the full range," so Python walks from the last index to the first.

**Why `word[::-1][::2]`** (from `Slicing.py`) means "every 2nd character from the reversed string" — slicing can be chained because each slice returns a *new* string, which you can slice again immediately.

This exact mechanism works identically on **lists and tuples** — `Collection/list.py`'s `Fruits[::-1]` and `Collection/Tuples.py`'s `fruits[::-1]` use the same rule.

## Strings are iterable, not just indexable
```python
for ch in word:        # no index needed at all
    count += 1
```
This is the idiomatic way to walk a string character-by-character when you don't need the position.

## How to work with this topic
1. Index 0 = leftmost, index -1 = rightmost. Out-of-range index → `IndexError`.
2. Slicing never errors on out-of-range bounds (`word[0:999]` just returns up to the end) — this is a key difference from single indexing.
3. `step` controls direction and stride: positive = forward, negative = backward, `abs(step) > 1` = skip characters.
4. Strings/lists/tuples share the exact same indexing & slicing rules because they're all Python **sequences**.
