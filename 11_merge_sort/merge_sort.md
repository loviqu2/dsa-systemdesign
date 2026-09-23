- divide and conquer. Split the list in half recursively until you reach single elements (base case: len < 2), 
then merge pairs back together by comparing the fronts of two already-sorted lists and popping the smaller each time, dumping any leftovers once one side empties. 

- Recursion must fully finish the left branch before starting right (call stack pauses, same as Day 7's tree traversal). Big-O: O(n log n) — O(log n) levels of splitting, O(n) work per level, multiplied together. Faster than Day 1's O(n²) nested-loop approach for large lists.