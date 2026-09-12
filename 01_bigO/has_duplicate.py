# to find numbers that are the same values but in different position




def has_duplicate(nums):
    for i, num_i in enumerate(nums): #outer loop i is the pos, and num_i is the value
        for j, num_j in enumerate(nums):
            if num_i == num_j and i != j:
                return True
    return False

print(has_duplicate([1, 2, 3, 4, 5]))
print(has_duplicate([1, 2, 3, 2, 5]))

        
            



# fruits = ["apple", "banana", "cherry"]

# for i, fruit in enumerate(fruits):
#     print(i, fruit)