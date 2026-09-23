def merge(left, right):
    merged = []
    while len(left) > 0 and len(right) > 0: #while len of left and right is not empty
        if left[0] < right[0]:  # compare left first index with right first index, smaller one gets pop into merged
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged += left  #add in the leftovers into the list
    merged += right

    return merged





def merge_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])  #directly pass it into the left side of the list
        right = merge_sort(lst[mid:])
        merged = merge(left, right)  # combine them into one sorted list

        return merged
    
print(merge_sort([8, 3, 5, 1, 2]))