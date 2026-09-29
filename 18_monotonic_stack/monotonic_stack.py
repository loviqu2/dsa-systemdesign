def next_greater_element(nums):
    answer = [-1] * len(nums) #start every pos at -1, no next greater found yet.
    stack = [] #something like a room where we're waiting for the next bigger number

    for i in range(len(nums)): # walk through every index, one at a time
        while stack and nums[i] > nums[stack[-1]]: #check if stack is empty, and check if the value beats the value on top
            popped_index = stack.pop() #remove top index from stack
            answer[popped_index] = nums[i] #record the next greater value for popped_index
        stack.append(i)
        # after while loop finish ( stack empty or no more greater next value), push today index into stack

    return answer #anything still left in the stack 

print(next_greater_element([3, 1, 4, 2, 5]))


#Monotonic stack (next greater element) — maintains a stack of indices whose values stay in decreasing order. For each new number, pop off (and record an answer for) any index on the stack whose value is smaller, since the new number is their "next greater." Then push the current index on. while stack and ... guards against IndexError on an empty stack via short-circuit evaluation. Big-O: O(n) via amortized analysis — even though it's a while nested in a for, each element is pushed once and popped at most once across the entire run, so total work stays linear despite the nested-loop appearance.