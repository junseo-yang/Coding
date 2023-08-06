# Coding
## Big O
* A Language and metric that we use to describe the efficiency of algorithms
* Best Case, Worst Case, Expected Case
* Time Complexity
* **Space Complexity**
    * Memory or Space required by an algorithm
    * e.g., an array of size $n$ = $O(n)$ space
    * e.g., an two dimensional array of size $n*n$ = $O(n^2)$ space
    * The term Space Complexity is misused for Auxiliary Space at many places. Following are the correct definitions of Auxiliary Space and Space Complexity. 
    * **Auxiliary Space** is the extra space or temporary space used by an algorithm.
* Drop the Constants
    * $O(2n)$ = $O(n)$
* Drop  the  Non-Dominant Terms
    * $O(N^2 + N)$ = $O(N^z)$
    * $O(N + log N)$ = $O(M)$
    * $(5*2^N + ie00N^{100})$ = $O(2^N)$
* Big O Chart
    * $O(1)$ - Excellent/Best
    * $O(log n)$ - Good
    * $O(n)$ - Fair
    * $O(n log n)$ - Bad
    * $O(n^2)$, $O(2^n)$ and $O(n!)$ - Horrible/Worst
* Multi-Part Algorithms: Add vs. Multiply
* Amortized Time
    * ArrayList

## Arrays
* An Array is a data structure consisting of a collection of elements, of same memory size, each identified by at least one array index or key.
* We can get size, capacity, is_empty, element at a specific index, push, etc
* Time
    * In an array, ‘ARR’ where the address of the first element is ‘A’ and the size of each element is ‘S’, ‘i’th element can be defined as 
    * $ARR[i] = A + (i - 1) * S$
    * Thus accessing an element at a specific memory address takes O(1) time, as its relative address can be calculated in constant time.
    * Similarly editing any element of the array takes O(1) time.
    * Inserting a new element at a particular index in arrays is only possible when we skip all the elements before that index, which takes O(N) time.
    * Similarly, deletion operation also takes O(N) time.
    * Searching operation in arrays takes O(N) time without any specific algorithm as we need to iterate and check every element in the array.
* Space
    * Contiguous in memory, proximity helps performance
    * Space needed = (array capacity, which is >= n) * size of each item, but even if $2n$, still $O(n)$

## Linked Lists
* A Linked List is a data structure for storing objects in linear order
* A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers.
### Characteristics
* In most cases, it has head pointer and tail pointer
* It store data `Null` if it's the end of LinkedList
### Operations
* Insert
* Delete
* Search
### Types
* Singly Linked List
* Doubly Linked List
* Circular linked List
### Singly Linked List
* a pointer that points the first node
* value
* next node pointer
#### Operations
* Access
    * Worst Case: $O(n)$
* Insert
    * Worst Case: $O(n)$
* Delete
    * Worst Case: $O(n)$
* Search
    * Worst Case: $O(n)$
### Doubly Linked List
#### Architecture
* a pointer that points the first node
* previous node pointer
* value
* next node pointer
#### Operations
* Access
    * Worst Case: $O(n)$
* Insert
    * Worst Case: $O(1)$
* Delete
    * Worst Case: $O(n)$
* Search
    * Worst Case: $O(n)$
### Linked List vs Array
* Linked List doesn't need to resize unlike Array does
* Array has an random access capability unlike Linked List doesn't
* Search operation takes $O(n)$ for Singly Linked List unlike Array takes $O(1)$
* Linked List has in-contiguous memory allocation unlike Array has contiguous memory allocation

## Stacks
* A stack is an abstract data type that serves as a collection of elements
### Characteristics
* LIFO
* Can be implemented with LinkedList or Array
### Operations
* Push, which adds an element to the collection, and
* Pop, which removes the most recently added element that was not yet removed.
* Peek, which returns the value of the last element added.
### Time Complexity
1. Push: $O(1)$
2. Pop: $O(1)$
3. Peek: $O(1)$
4. Search: $O(n)$
5. Size: $O(1)$
### Space Complexity
* In most cases, $O(n)$


## Queue
* A Queue is defined as a linear data structure that is open at both ends and the operations are performed in First In First Out (FIFO) order.
### Operations
* Enqueue, which adds an element to the rear of the queue
* Dequeue, which removes an element from the front
### Time Complexity
* Enqueue: O(1)
* Dequeue: O(1)
* Since in most cases a queue can be implemented using Arrays or Linked Lists.
### Space Complexity
* Enqueue: O(1) (Auxiliary Complexity)
* Dequeue: O(1) (Auxiliary Complexity)

## Hash Table
* Hash Table is a data structure stores elements in key-value pairs where
* key: unique integer that is used for indexing the values
* value: data that are assoicated with keys
### Dictionary
* A generic way to map keys to values
### Hash Table 
* An implementation of a dictionary using a hash function
### Hashing
* Hashing is a technique of mapping a large set of arbitrary data to tabular indexes using a hash function. It is a method for representing dictionaries for large datasets.
* It allows lookups, updating and retrieval operation to occur in a constant time i.e. $O(1)$
### Hash Collision
* Hash Collision is a conflict that occurs when a hash function generates the same index for multiple keys
* Can be resolved by:
    * Collision resolution by chaining
    * Open Addressing: Linear/Quadratic Probing and Double Hashing
### Direct-access tables
* U = universe of keys (e.g., 0, 1, 2, 3, 4, ...)
* K = actual keys (e.g., 4, 5, ...)
### Operations
### Time Complexity
* Insert: average $O(1)$, worst $O(n)$
* Delete: average $O(1)$, worst $O(n)$
* Search: average $O(1)$, worst $O(n)$

## Binary Search 
Binary search is a search algorithm that is used to quickly find a value in a sorted sequence with each iteration of the algorithm half of the remaining values
### Pseudo Code 
* Case 1: The element that you are searching is not in the target space - Return `-1`
    * max < min
* Case 2: The element that you are searching is in the target space
    * Set min = 0 and max n - 1
    * Guess the `arr[mid]`
    * if `arr[mid]` < `target`, then `min` = `mid + 1`
    * else-if `target` < `arr[mid]`, then `max` = `mid - 1`
    * else `arr[mid]` == `target`, return the mid
### Time Complexity
* $Log_2(N)$ 

## Bitwise operations
### Operators
* `&, |, ^, ~, >>, <<`
### Manipulation
* Bit manipulation is the act of algorithmically manipulating bits or other pieces of data shorter than a word. 
* In computing, a `word` is the natural unit of data used by a particular processor design. A word is a fixed-sized datum handled as a unit by the instruction set or the hardware of the processor. The number of bits or digits in a word (the word size, word width, or word length) is an important characteristic of any specific processor design or computer architecture.
* Set Bit
    ```python
    def set_bit(x, position):
        mask = 1 << position
        return x | mask
    ```
* Clear Bit
    ```python
    def clear_bit(x, position):
        mask = 1 << position
        return x & ~ mask
    ```
* Flip Bit
    ```python
    def flip_bit(x, position):
        mask = 1 << position
        return x ^ mask
    ```
* Is Bit Set
    ```python
    def is_bit_set(x, position):
        shifted = x >> position
        return shifted & 1
    ```
* Modify Bit (Clear)
    ```python
    def modify_bit(x, position, state):
        mask = 1 << position
        return (x & ~mask) | (-state & mask)
    ```
### Bit Tricks
* Check If Even
    ```python
    def is_even(x):
        return (x & 1) == 0
    ```
    ```python
    def is_even(x):
        return ~(x & 1)
    ```
* Check if power of two
    ```python
    def is_power_of_two(x):
        return (x & x - 1) == 0
    ```
    ```python
    def is_power_of_two(x):
        return ~(x & x - 1)
    ```
### 1's Complement
* The ones' complement of a binary number is the value obtained by inverting (flipping) all the bits in the binary representation of the number
### 2's Complement
* Two's complement is a mathematical operation to reversibly convert a positive binary number into a negative binary number with equivalent negative value, using the binary digit with the greatest place value as the sign to indicate whether the binary number is positive or negative. 
#### Solve
* -0 and +0

## Trees
### Definition
* Tree data structure is a hierarchical structure that is used to represent and organize data in a way that easy to navigate and search
* It is a collection of nodes that are connected by edges and has a hierarchical relationship between the nodes.
* Root is the topmost node. and nodes below it are called child nodes.
* Each node can have multiple child nodes, and these child nodes can also have their own child nodes, forming a recursive structure.  
### Traversal
#### BFS (Breadth-first Search)
* Breadth-first Search is an algorithm for searching a tree data structure for a node that satisfies the given property.
* It starts at the tree root and explorers all nodes at the present depth prior to moving on to the next depth level of nodes. 
* All connections at one time
* Level order (using Queue)
* Time complexity: $O(n)$
* Space complexity: best: $O(1)$ worst: $O(n/2) = O(n)$
#### DFS (Depth-first Search)
* Depth-first Search is an algorithm for traversing or searching tree or graph data structures.
* The algorithm starts at the root of node and explores as far as possible along each branch before backtracking.
* time complexity: $O(n)$
* space complexity: best $O(log n) = height of the tree$ / worst $O(n)$ 
* In-order: L - Root - R
* Pre-order: Root - L - R
* Post-order: L - R - Root

## Binary Search tree
*  Binary Search tree, also known as an ordered or sorted binary tree, is rooted rooted binary tree data structure with the key of each internal node being greater than all the respective node's left subtree and less than the ones its right sub tree.
### Search
* Compare the given value, if it's less than the key, go left. If it's greater than the key, go right.
* If a node is a leaf (has no children), you can insert the given node to the node.
* Time Complexity: $O(log n) = height of the tree$
### Insert
* Compare the given value, if it's less than the key, go left. If it's greater than the key, go right.
* If the leaf node, insert the target based on the same criteria.
### Delete
1. The given node is a leaf node, the node will be replaced by `nil`
2. The given node has one child, the node will be replaced by `nil` and the node's child will take over the node's position
3. The given node has two children, you'll find the key value that is bigger than the target but the smallest in the right subtree of the node and replace the target node and the smallest node.
### Travesal
1. Pre-order
2. In-order
3. Post-order
### Discussion
1. Runtime
   1. Search - best: $O(log n)$ / worst: $O(n)$ - consequent order
   2. Insert - best: $O(log n)$ / worst: $O(n)$ - consequent order
   3. Delete - best: $O(log n)$ / worst: $O(n)$ - consequent order
2. Duplicate value?
   1. It's up to your choice. In most cases, best practice will be in the right leaf because it makes more sense when we traverse it in-order.
### Find the Maximum Depth or Height of given Binary Tree
1. The height of an empty tree is `0`.
2. Use DFS
   1. Recursively calculate the height of the left and the right subtrees of a node and assign height to the node as max of the heights of two children + 1.
   2. Time complexity: $O(n)$
   3. Auxiliary Space: $O(n)$ due to recursive stack 
3. Use BFS
   1. Use Queue.
      1. Traverse the tree in level order traversal starting from root
      2. Run a while loop till Q is not empty 
         1. Store the front element of Q and Pop out the front element
         2. If the front of Q is `NULL` then incremenet depth by one and if queue is not empty then push NULL into the Q.
         3. Else if the element is not `NULL` then check for its left and right children and if they are not NULL push them into Q.
      3. Return depth
   2. Time Complexity: $O(n)$
   3. Auxiliary Space: $O(n)$
