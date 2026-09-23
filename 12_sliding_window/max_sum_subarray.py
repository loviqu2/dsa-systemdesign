def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k]) #start from 0, k is the size of the window, which ends at k , sum is to total up the numbers inside the window.
    max_sum = window_sum

    for i in range(1, len(nums) - k + 1): #formula to find out how many windows can there be in a list of numbers.
        leaving_element = nums[i - 1]
        entering_element = nums[i + k -1 ] # to find the entering element, we plus the window size subtract by 1, also a rule 
        window_sum = window_sum - leaving_element + entering_element

        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum

#rule is new sum= old sum - (element leaving) + (element entering)

print(max_sum_subarray([2, 5, 1, 8, 3], 2))


#Sliding window — for problems involving a fixed-size (or variable-size) contiguous subarray, avoid recomputing the sum/stat from scratch for every window. Instead, maintain a running value and update it incrementally: subtract the element leaving, add the element entering. Big-O: naive re-sum approach is O(n × k) (worst case O(n²)); sliding window is O(n) since each element is only added/subtracted once.