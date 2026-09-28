def merge_intervals(intervals):  

    # assume our list is [[1,3], [2,6]]
    intervals = sorted(intervals)
    result = [intervals[0]] #save the first interval into the result #[1,3]

    for current in intervals[1:]: #for the current one which is the one after the first in the list
        last = result[-1] #the most recently placed block [1,3]

        if current[0] <= last[1]:   #[2,6] = 2(current[0]) < [1,3] = 3(last[1])
            last[1] = max(last[1], current[1])  # last[1] = max(last[1]) = 3, max(current[1]) = 6 so last[1] = 6 
            # because max of 3,6 is 6.
        else: 
            result.append(current)

    return result


intervals = [[1,3], [2,6], [8,10], [15,18]]
print(merge_intervals(intervals))


# Greedy intervals (merge overlapping intervals) — sort by start time first (guarantees any overlapping interval appears immediately next, not scattered). Walk through once, comparing each new interval's start against the last merged block's end (current[0] <= last[1] → overlap). On overlap, extend the block's end with max(last[1], current[1]) (not just the new end, to handle fully-contained intervals correctly). last and result[-1] are the same list object (shared reference), so mutating last updates result automatically. Big-O: O(n log n) — dominated by the initial sort; the merge pass itself is only O(n) and gets dropped when added to the bigger term.