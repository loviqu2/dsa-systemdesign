def push(heap, value):
    heap.append(value)
    i = len(heap) - 1 #track index of newly added value

    while i > 0:
        parent_i = (i - 1) // 2 #parent formula
        if heap[i] < heap[parent_i]:
            heap[i], heap[parent_i] = heap[parent_i], heap[i] #swap the value of new index, and parent
            i = parent_i
        else:
            break

# heap = [2, 5, 3, 8, 9]
# push(heap, 1)
# print(heap)

def pop(heap):
    root_value = heap[0]  #save what is to be retuned
    heap[0] = heap[-1] # move the last element to the root
    heap.pop()  # pop the last duplicated slow

    i = 0 #track the index , starting on the root
    while True:  
        left = (2 * i) + 1 #left child formula
        right = (2 * i) + 2 #right child formula
        smallest = i #assume current pos is ok for now

        if left < len(heap) and heap[left] < heap[smallest]:
            smallest = left
        if right < len(heap) and heap[right] < heap[smallest]:
            smallest = right

        if smallest == i:
            break
        else:
            heap[i], heap[smallest] = heap[smallest], heap[i]  #swap heap[i] with the samllest
            i = smallest #move tracked index to where we now are

    return root_value


heap = [1, 5, 2, 8, 9, 3]
result = pop(heap)
print(result)
print(heap)



# Heaps (min-heap) — a "loosely sorted" tree structure (stored as a flat array) that guarantees only one thing: every parent ≤ its children. Cheaper to maintain than a fully sorted list. Array index math: left child = 2i+1, right child = 2i+2, parent = (i-1)//2. push: append to end, then bubble up (swap with parent while smaller than parent). pop: save root, move last element to root, remove last slot, then bubble down (swap with the smaller child while bigger than it) until reaching a leaf or satisfying the rule. Both operations: O(log n), since they only ever traverse one path through the tree's log n levels — much cheaper than a full O(n log n) re-sort per insertion.