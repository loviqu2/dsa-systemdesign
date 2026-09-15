# def has_duplicate(nums):
#     for i, num_i in enumerate(nums): #outer loop i is the pos, and num_i is the value
#         for j, num_j in enumerate(nums):
#             if num_i == num_j and i != j:
#                 return True
#     return False

# print(has_duplicate([1, 2, 3, 4, 5]))
# print(has_duplicate([1, 2, 3, 2, 5]))


#hash map

def has_duplicate(nums):
    seen = {}
    for num in nums:  #loop already has this covered
        if num in seen: #this is a 0(1) check, if num is already rec
            return True #if yes, then exit immediately
        else:  
            seen[num] = True #if not, record for future iteration to check against it
    return False  #loop finish with no matches found

print(has_duplicate([1, 2, 3, 4, 5]))
print(has_duplicate([1, 2, 3, 2, 5]))


