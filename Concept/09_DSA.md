# Data Structures & Algorithms (DSA)

This is the biggest folder in the repo. Each file implements a classic data structure **from scratch**, usually backed by a Python `list` or a chain of custom `Node` objects, so you can see exactly how the structure works under the hood instead of just calling a built-in.

---

## Array (`Array.py`)
Python's `list` is already dynamic and flexible, so Python has a separate, stricter `array` module for when you want a **fixed-type, memory-efficient** sequence (closer to a C array) — all elements must be the same type (`'i'` = signed int).

```python
import array
val = array.array('i', [1,2,3,4,5,6])
```
Key operations shown: `.reverse()`, `.insert(i, v)`, `.append(v)`, direct index assignment `val[2] = 200`, `.pop(i)` (remove by index), `.remove(v)` (remove by value), and slicing `val[1:4]`.

**numpy arrays** (also covered) are a different, far more powerful tool — used for numerical/scientific computing:
- `linspace(10, 20, 5)` → 5 evenly spaced values between 10 and 20 (inclusive).
- `arange(10, 20, 2)` → like `range()` but returns a numpy array, works with floats too.
- `zeros(10)` / `ones(10)` / `full(10, 5)` → pre-filled arrays, useful for initializing buffers/matrices.
- Multi-dimensional arrays: `array([[1,2,3],[4,5,6]])` is a 2D array (matrix) — this is the foundation for the adjacency **matrix** used later in `Graph.py`.

**When to use which:** plain `list` for everyday general-purpose code, `array` module when you need a lightweight fixed-type sequence, `numpy` when doing numerical/matrix work (and in real projects, numpy is almost always what's actually used over the stdlib `array` module).

---

## Stack (`Stack.py`) — LIFO: Last In, First Out
Think of a stack of plates — you can only add/remove from the **top**.

```python
class Stack:
    def __init__(self):
        self.lis = []
    def Push(self, value):
        self.lis.append(value)     # add to the END — treat end-of-list as "the top"
    def pop(self):
        return self.lis.pop()      # remove from the END
    def peek(self):
        return self.lis[-1]        # look at the top without removing it
```
Your file shows **two implementations**: one uses `.insert(0, value)` for push (treating index 0 as "top," so `pop(0)`/`peek → lis[0]`), the other uses `.append()` (treating the *end* as "top," so `pop()`/`peek → lis[-1]`).

**Why the `.append()`/`.pop()` version is better:** `insert(0, ...)` and `pop(0)` are **O(n)** — every other element has to shift over by one position in memory. `append()` and `pop()` (no index) are **O(1)** — they only touch the end of the list. Same logical stack, very different performance at scale.

**Real-world uses of stacks:** undo/redo history, the "back" button in a browser, function call stacks (how recursion itself works — see below), balanced-parenthesis checking, depth-first search (DFS).

---

## Queue (`Queue.py`) — FIFO: First In, First Out
```python
class Queue:
    def __init__(self):
        self.items = []
    def insert(self, value):
        self.items.append(value)    # add to the END (the "back" of the line)
    def delete(self):
        return self.items.pop(0)    # remove from the FRONT
```
Like a line at a checkout counter — whoever got in line first gets served first. (Note: your current `DSA/Queue.py` file is empty — this is the implementation it's meant to hold, matching the structure already present in `Stack.py`/`CicularQueue.py`.)

`pop(0)` here is also O(n) for the same reason as the stack above — in production code you'd use `collections.deque` instead (O(1) from both ends), but implementing it with a plain list first is the right way to *learn* why queues need special data structures.

**Real-world uses:** task scheduling, print job queues, breadth-first search (BFS), any "process things in the order they arrived" scenario.

---

## Circular Queue (`CicularQueue.py`)
A **fixed-size** queue that reuses empty slots instead of always growing — once the last slot is used, the next insertion wraps back around to index 0 (hence "circular"), as long as there's a free slot.

```python
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = self.rear = -1
```
- `front == -1` means **empty**.
- Checking full: `(self.rear + 1) % self.size == self.front` — the `% self.size` is what creates the "wraparound" behavior: once `rear` hits the last index, adding 1 and taking `% size` brings it back to 0.
- Checking "only one element left" (`front == rear`) is a special case for deletion — after removing it, both pointers reset to `-1` (empty again) rather than leaving them pointing at a stale slot.

**Why this exists:** a plain queue backed by a list that only ever appends/pops(0) can still work, but a circular queue is the classic data structure used when you have **fixed, pre-allocated memory** (common in embedded systems, OS buffers, streaming data) and want to reuse freed slots instead of shifting elements or growing the array.

---

## Deque — Double-Ended Queue (`Deque.py`)
A deque allows insertion **and** deletion from **both ends**.

```python
class Deque:
    def insertAtEnd(self, value): self.items.append(value)
    def insertAtFront(self, value): self.items.insert(0, value)
    def deleteAtEnd(self): return self.items.pop()
    def deleteAtFront(self): return self.items.pop(0)
```
It's a generalization of both stack (use only `insertAtEnd`/`deleteAtEnd`) and queue (use `insertAtEnd`/`deleteAtFront`) in one structure. Python's own `collections.deque` is the production-ready, O(1)-both-ends version of exactly this idea.

---

## Linked List (`Linked_list.py`, `DoubleLL.py`)
A linked list stores elements as a chain of **Node** objects, where each node holds data *and* a pointer to the next node — unlike a list/array, elements are **not stored in one contiguous memory block**.

### Singly Linked List
```python
class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next

class SingleLL:
    def __init__(self, head=None):
        self.head = head    # head = pointer to the FIRST node; the list's only entry point

    def InsertAtEnd(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:   # walk to the LAST node
                t1 = t1.next
            t1.next = temp                # attach new node after it
```
**Why walking is necessary:** unlike a list where you know the last index instantly (`len(lst)-1`), a linked list has no index — the only way to find the end is to follow `.next` pointers one by one until you hit a node whose `.next` is `None`. This makes `InsertAtEnd` **O(n)**, while `InsertAtBeg` is **O(1)**:
```python
def InsertAtBeg(self, value):
    temp = Node(value)
    temp.next = self.head   # new node points to the OLD first node
    self.head = temp         # head now points to the new node
```
No walking needed — you just rewire two pointers.

**Insert at middle** (after a specific value `Loc`):
```python
def InsetAtMid(self, value, Loc):
    temp = Node(value)
    t1 = self.head
    while t1 is not None:
        if t1.info == Loc:
            temp.next = t1.next   # new node points to what used to come after Loc
            t1.next = temp         # Loc now points to the new node
            break
        t1 = t1.next
```
The order of those two lines matters: you must save "what comes after `Loc`" into `temp.next` **before** overwriting `t1.next`, or you'd lose the rest of the list.

**Delete a value:**
```python
def deleteLL(self, value):
    if self.head.info == value:        # special case: deleting the head itself
        self.head = self.head.next
        return
    prev = None
    tHead = self.head
    while tHead is not None:
        if tHead.info == value:
            prev.next = tHead.next      # skip over tHead — nothing points to it anymore, so it's "deleted"
            return
        prev = tHead
        tHead = tHead.next
```
Deletion is really just **rerouting pointers around the node you want gone** — you need a `prev` pointer because to delete a node, you must modify the node *before* it.

### Doubly Linked List (`DoubleLL.py`)
Same idea, but every node also has a `.prev` pointer back to the previous node:
```python
class Node:
    def __init__(self, value=None):
        self.data = value
        self.prev = None
        self.next = None
```
This lets you walk **backward** as well as forward, and makes deletion/insertion easier because you don't need a separate `prev` tracking variable — each node already knows its own predecessor. Trade-off: extra memory (one more pointer per node) and extra bookkeeping (every insert/delete must update *two* links on *two* neighboring nodes, not just one).

```python
def insertAtBeg(self, value):
    temp = Node(value)
    temp.next = self.head
    self.head.prev = temp   # the OLD head must now point back to the new node
    self.head = temp
```

**Note:** your `DSA/Recursion.py` file currently contains this exact doubly-linked-list code, but entirely wrapped in a docstring comment (`"""..."""`), so none of it actually executes — the file has no working recursion examples right now. See the Recursion section below for what *should* go there.

**Linked list vs. array/list — when to use which:**
| | Array/Python list | Linked List |
|---|---|---|
| Access by index | O(1) | O(n) — must walk from head |
| Insert/delete at front | O(n) (shifts everything) | O(1) |
| Insert/delete at end | O(1) amortized | O(n) (singly) unless you track a tail pointer |
| Memory layout | contiguous | scattered, linked via pointers |

---

## Binary Search Tree — BST (`BST.py`)
A BST is a tree where, for **every** node: everything in its **left** subtree is smaller, everything in its **right** subtree is larger.

```python
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def insert(root, value):
    if root is None:
        return Node(value)          # found the empty spot — place the new node here
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
```
This is **recursive**: at each node, decide "go left or go right" based on the BST rule, and recurse into that subtree. The base case is `root is None` — an empty spot, where the new node gets created and returned to be attached by the caller.

**Search** follows the exact same left/right decision logic, just checking for a match instead of inserting.

**Delete** is the trickiest operation, with three cases:
1. Node has no children → simply remove it (return `None` upward, detaching it).
2. Node has one child → replace it with that one child.
3. Node has two children → can't just remove it (you'd orphan a whole subtree). Instead, find the **in-order successor** (the smallest value in the right subtree — `get_successor`), copy that value into the node being "deleted," then delete the successor instead (which is guaranteed to have at most one child, reducing back to an easier case).
```python
def get_successor(root):
    root = root.right
    while root is not None and root.left is not None:
        root = root.left   # smallest value in the right subtree = leftmost node there
    return root
```

**Why BSTs matter:** search/insert/delete are all **O(log n)** on a balanced tree (each comparison roughly halves the remaining search space) versus O(n) for an unsorted list — the entire reason BSTs exist is fast lookup combined with maintained order.

**In-order traversal of a BST prints values in sorted order** — not a coincidence, it falls directly out of the left-smaller/right-larger invariant (see Tree Traversal below).

---

## Tree Traversal (`TreeTravelsal.py`)
"Traversal" = visiting every node in a tree in some defined order. For a binary tree (no BST ordering assumed here — just parent/left/right), there are 3 classic **depth-first** orders, all implemented recursively:

```python
def preorder(root):    # ROOT, then left, then right
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def Inorder(root):     # left, then ROOT, then right
    if root:
        Inorder(root.left)
        print(root.data)
        Inorder(root.right)

def postorder(root):   # left, then right, then ROOT
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
```
The name tells you **where the root gets visited relative to its children**: pre = before both, in = between them, post = after both. Same recursive skeleton every time — only the position of the `print()` line changes.

**When each is used:** pre-order to copy/serialize a tree's structure, in-order for sorted output on a BST, post-order when children must be processed before the parent (e.g., deleting a tree bottom-up, evaluating an expression tree).

---

## Graph (`Graph.py`)
A graph is a set of **vertices** (nodes) connected by **edges**. Your file shows the two standard representations:

### 1. Adjacency Matrix
```python
class Graph:
    def __init__(self, vertex):
        self.mat = [[0]*vertex for x in range(vertex)]   # a VxV grid of zeros
    def add_edge(self, src, dest):
        self.mat[src][dest] = 1
        self.mat[dest][src] = 1   # symmetric → undirected graph
```
A 2D grid where `mat[i][j] = 1` means "an edge connects vertex i and vertex j." Simple and gives O(1) "are these two connected?" checks, but wastes memory (`O(V²)`) when most vertices *aren't* connected to each other (a "sparse" graph).

### 2. Adjacency List
```python
class Graph:
    def __init__(self):
        self.adjList = {}      # dict: vertex -> list of its neighbors
    def addEdge(self, src, dest):
        self.add_vertex(src); self.add_vertex(dest)
        self.adjList[src].append(dest)
        self.adjList[dest].append(src)
```
Instead of a full grid, each vertex only stores **its actual neighbors** in a list — much more memory-efficient for sparse graphs (most real-world graphs: social networks, road maps, web links). This is the representation almost always preferred in practice.

(Note: `printGraph` in your file is currently unfinished — it has no body. A working version would loop over `self.adjList.items()` and print each vertex with its neighbor list, mirroring the matrix version's `print()` method.)

**Why two representations exist:** matrix = fast edge lookup, simple code, bad for memory on sparse graphs. List = memory-efficient, slightly more code to check "are these connected," and is what graph traversal algorithms (BFS/DFS) are usually built on top of.

---

## Recursion
A recursive function is one that **calls itself**, each time working on a smaller version of the same problem, until it reaches a **base case** simple enough to answer directly without recursing further.

Every recursive function needs exactly two parts:
1. **Base case** — the condition that stops the recursion (without one, you get infinite recursion → `RecursionError: maximum recursion depth exceeded`).
2. **Recursive case** — the function calling itself with a smaller/simpler input, trusting that the smaller call will correctly solve its own (smaller) version of the problem.

You've actually already used recursion twice elsewhere in the repo without a dedicated file for it:
- **BST `insert`/`Search`/`delete`** — each call either hits the base case (`root is None`, or a match found) or recurses into `root.left`/`root.right`.
- **Tree traversal (`preorder`/`Inorder`/`postorder`)** — base case `root is None` (implicitly, via `if root:`), recursive case: call the same function on `root.left` and `root.right`.

A classic standalone example to put in this file, factorial:
```python
def factorial(n):
    if n == 0:          # base case
        return 1
    return n * factorial(n - 1)   # recursive case: solve a smaller problem (n-1), then use it
```
`factorial(4)` expands as: `4 * factorial(3)` → `4 * (3 * factorial(2))` → ... → `4*3*2*1*factorial(0)` → `4*3*2*1*1 = 24`. Each call waits (paused, sitting on the **call stack** — the same "stack" data structure covered above!) for the call below it to return before it can finish its own multiplication. This is exactly why deep recursion can run out of memory/hit Python's recursion limit — every pending call occupies a frame on the stack simultaneously.

**Recursion vs. loops:** anything recursive can be rewritten as a loop (and vice versa for simple cases) — recursion tends to read more naturally for problems that are *already* defined in terms of smaller versions of themselves (trees, factorial, Fibonacci, divide-and-conquer algorithms), while loops are usually more memory-efficient for simple linear repetition.

---

## How to work with this topic
1. Identify the **access pattern** you need (LIFO → stack, FIFO → queue, both ends → deque, fast ordered lookup → BST, arbitrary relationships → graph) before picking a structure — each one trades off speed differently for insert/delete/search depending on *where* in the structure you're operating.
2. For anything built on `Node` objects (linked list, BST, trees, graphs): always draw it on paper first — pointer-rewiring bugs (losing a reference before saving it elsewhere) are the single most common mistake, as seen in the `InsetAtMid` ordering note above.
3. For recursion: write the base case first, then trust that the recursive call correctly solves the smaller subproblem — don't try to mentally unroll the entire call chain while writing it.
4. Big-picture complexity cheat sheet: array/list index access O(1), linked list index access O(n), BST search/insert/delete O(log n) *average* (balanced) but O(n) worst case (degenerates into a line if inserted in sorted order), stack/queue push/pop O(1) when done from the correct end.
