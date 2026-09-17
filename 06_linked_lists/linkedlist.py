
#linked list are used when we need to insert or remove items in the middle of a list, if we use 
# traditional ways, it would be computationally expensive where all the values inside the list need to move

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

patient = ["Patient A", "Patient B" ,"Patient C"]



# this part is to find out the node of the patients, giving them a link to a position
head = Node(patient[0])
current = head

for patients in patient[1:]: #start at index one, since head is stated, do it until the end
    new_node = Node(patients)  # create a new node first
    current.next = new_node #point the current node to the next one
    current = new_node #update the current node and repeat until finish

# # this can be changed into a loop
# node_a = Node("Patient A")
# node_b = Node("Patient B")
# node_c = Node("Patient C")

# node_a.next() = node_b  # this part just stores whats inside the node for the while loop to work
# node_b.next() = node_a

# current = node_a

current = head  # we need to reset the current node, if not it will print out as C

while current is not None:
    print(current.value)  # when the current node is not empty, print the node ( A to C, until none)
    current = current.next




