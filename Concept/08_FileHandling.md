# File Handling

File handling lets a program **persist data beyond its own runtime** — anything in a variable disappears when the script ends; a file on disk survives.

## Opening a file: `open(path, mode)`
```python
file = open("student.txt", "w")
...
file.close()
```
Every file interaction starts with `open()` and should end with `.close()` — leaving a file open can lock it from other programs or lose unsaved (buffered) writes.

### Modes — this is the part that matters most
| Mode | Meaning | Destructive? |
|---|---|---|
| `"r"` | Read only. File must already exist, or `FileNotFoundError`. | No |
| `"w"` | Write. **Creates the file if missing, or completely erases its existing contents first.** | **Yes — wipes the file** |
| `"a"` | Append. Creates the file if missing; otherwise adds new content to the **end** without touching what's already there. | No |

This is the single most important thing to internalize: `"w"` mode **truncates the file to empty the instant you open it**, even before you write anything. Your `File.py` opens `student.txt` in `"w"` mode twice (once to create it, once to write the name) — the second `open(..., "w")` would already have erased the first write if there had been one, which is why the script re-writes `"Raunak"` fresh each time rather than relying on the earlier open.

## Reading
```python
file = open("student.txt", "r")
content = file.read()       # ENTIRE file as one string
print(content)
file.close()
```
- `.read()` → whole file as a single string.
- `.readlines()` → a **list of strings**, one per line (each still ending with `\n` except possibly the last line).
  ```python
  content = file.readlines()
  print("length of line =", len(content))   # counts lines
  ```
- Looping `for line in file:` (not shown in your code but equivalent) reads one line at a time without loading the whole file into memory — better for very large files.

## Writing vs. appending
```python
file = open("student.txt", "w")
file.write("Raunak")     # overwrites whatever was there
file.close()

file = open("student.txt", "a")
file.write("\nSiwan")     # adds to the end, on a new line
file.close()
```
Note `.write()` does **not** add a newline automatically (unlike `print()`) — you must include `"\n"` yourself if you want the next write to land on a new line, exactly as done here (`"\nSiwan"`).

## Copying a file
```python
source_file = open("student.txt", "r")
destination_file = open("copied.txt", "w")
content = source_file.read()
destination_file.write(content)
source_file.close()
destination_file.close()
```
Simple pattern: **read everything from source → write it into a freshly-opened (and thus emptied) destination file.** This is exactly how `copied.txt` and `copy.txt` in your repo were produced.

## Counting words / characters
```python
content = file.read()
word = content.split()          # splits on whitespace by default → list of words
print("number of word =", len(word))
print("Number of characters:", len(content))   # len() on a string = character count
```
`.split()` with no arguments splits on **any whitespace** (spaces, tabs, newlines) and automatically ignores extra/leading/trailing whitespace — the standard way to tokenize text into words.

## A subtle bug worth knowing: searching for a word
```python
file = open("student.txt", "r")
content = file.read()
word = input("enter the word = ")
if word in file:          # BUG: checking membership against the FILE OBJECT, not `content`
    print("word found")
```
`in file` checks whether `word` is among the file object's remaining *lines* to iterate (and since `.read()` already consumed the whole file, the file pointer is at the end — there's nothing left to iterate, so this will basically always report "not found" regardless of the actual word). The correct check is `if word in content:` — testing membership against the **string you already read**, not the file handle itself. This is a good illustration of why "read it into a variable, then work with the variable" is the safer habit.

## Why `try/except` around file operations (`Merge two text files`)
```python
try:
    file1 = open("file1.txt", "r")
    file2 = open("file2.txt", "r")
    ...
except FileNotFoundError:
    print("file is not found")
```
Any file you didn't just create yourself in the same script might not exist — opening a nonexistent file in `"r"` mode always raises `FileNotFoundError`. Wrapping file I/O in `try/except` (see `07_ExceptionHandling.md`) is standard defensive practice.

## The modern/better way: `with open(...)`
Not used in your current code, but worth knowing: in real projects, prefer
```python
with open("student.txt", "r") as file:
    content = file.read()
# file is automatically closed here, even if an exception happens inside the block
```
`with` guarantees `.close()` is called automatically, even if an error occurs mid-read/write — manually calling `.close()` (as your code does) works fine for short scripts, but it's easy to forget, or to skip it entirely if an exception is raised before reaching the `.close()` line.

## How to work with this topic
1. `"r"` = read (file must exist), `"w"` = **overwrite from scratch**, `"a"` = add to the end. Mixing these up is the #1 source of "why did my data disappear" bugs.
2. Always `.close()` a file you `.open()`ed — or better, use `with open(...) as f:` so it's automatic.
3. Once you `.read()` a file, the content lives in a variable — do all your checking/searching/counting against that variable, not the file object (which may now be "empty" / at end-of-stream).
4. Wrap filesystem operations in `try/except FileNotFoundError` whenever the file's existence isn't guaranteed.
