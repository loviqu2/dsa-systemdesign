
appointments = ["9am", "10am", "11am", "2pm"]

def reverse_list(lst):
    empty_list = []
    for i in range(len(lst) - 1 , -1 , -1): #len(lst) - 1 means we start at 2pm, then end at -1, reversing each step by 1
       empty_list.append(lst[i]) #grab the actual value at each index
    return empty_list


print(reverse_list(appointments))