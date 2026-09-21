referrals = {
    "Dr. A": ["Dr. B", "Dr. C"],
    "Dr. B": ["Dr. C"],
    "Dr. C": ["Dr. A"]     # notice this creates a cycle: A -> C -> A
}

def bfs_graph(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:  #while there is value inside the queue
        current = queue.pop(0)
        print(current)

        for neighbour in graph[current]:
            if neighbour not in visited:  #if the neighbour is not visited before, add and append into the queue and visited entry. 
                visited.add(neighbour)
                queue.append(neighbour)

bfs_graph(referrals, "Dr. A")

# Starts at 1 , where A is current, then visited after the step is A , B , C, queue after is B,C and printed is A
# step 2 is, current is B, where visited is A, B, C, queue after is C, so printed A, B
# step 3 is current is C, same visited, queue after is None, so printed C
# the steps follows the same for B, and C.

# Graphs & BFS

# A graph is a more general structure than a tree — any node can connect to
# any other node(s), in any direction, and cycles are allowed (a tree is
# really just a restricted graph: no cycles, single parent per node).

# Representation: adjacency list, using a dict where each key is a node and
# its value is a list of nodes it connects to.

# Use a set() for visited, not a list — same reasoning as Day 4's hash maps:
# `neighbor not in visited` needs to be O(1), and a set gives that same
# hash-based fast lookup a dict's keys do.
