# Coding
## Big O
* A Language and metric that we use to describe the efficiency of algorithms
* Best Case, Worst Case, Expected Case
* Time Complexity
* Space Complexity
    * Memory or Space required by an algorithm
    * e.g., an array of size $n$ = $O(n)$ space
    * e.g., an two dimensional array of size $n*n$ = $O(n^2)$ space
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
An Array is a data structure consisting of a collection of elements, of same memory size, each identified by at least one array index or key.