# backtracking
# assume that a service list has 4 items, we want to find out all the possible outcomes of choosing, they can choose none at all, or 2 of the 4, or all of it

#thought process
# we start off with items, index, result, and a path. Path is the current position where we walk down on specific branch of the tree, while result is the permanenant collection of the leaf. 
# everytime we finish towards the base case, it it saved into result. 


def subsets(items, index, path, result):
    if index ==  len(items):
        result.append(path[:])  # make an independant copy of whatever the path currently cointains
        return #once there is nothing left to do, then return



    #choice 1: include items[index] thats why we have path.append(items[index])
    path.append(items[index])  
    subsets(items, index + 1, path, result)

    #backtrack
    path.pop()

    # choice 2: skip items[index] #append is left out as we want to skip it
    subsets(items, index + 1, path, result)


result = []
subsets(["Facial", "Massage"], 0, [], result)
print(result)


# Backtracking (subsets) — systematically explores every possible combination of choices (include/skip each item) using recursion. Tracks the current in-progress choice in a path list (scratchpad), and saves a frozen copy (path[:]) into result (answer sheet) whenever a complete decision set is reached (index == len(items), the base case). Critically, every append must be matched by a pop() after exploring that branch, to undo the choice before trying the alternative — that undo step is what "backtracking" refers to. Big-O: O(2ⁿ), since there are exactly 2ⁿ total subsets to generate for n items, and (unlike DP) there's no overlapping work to cache — every subset is a genuinely distinct answer.