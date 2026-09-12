big O is a notation that describes how algo works as input size grows.

O(1) — constant. Same cost regardless of input size. E.g., dict[key] lookup.
O(n) — linear. Cost scales directly with input size. E.g., one loop through a list of n items.
O(n²) — quadratic. Cost scales with the square of input size. E.g., a loop nested inside another loop over the same data.
O(log n) — logarithmic. Cost barely grows even as input gets huge. E.g., binary search, halving the search space each step.