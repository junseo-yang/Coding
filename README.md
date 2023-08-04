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