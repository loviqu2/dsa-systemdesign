#The problem it solves: your clinic wants live search suggestions — as a customer types "ca", you want to instantly show every service name that starts with "ca". A trie stores your words in a shape specifically built for this "starts with" lookup, sharing common prefixes between words instead of storing each word as a separate, disconnected string.


#prefix means the beginning portion of the word


class TrieNode:
    def __init__ (self):
        self.children = {}
        self.is_end_of_word = False


# check at each letter if a door exist for them from this letter ( the current letter). if not, build one node, then walk thorugh the door with current = current.children[char]. once all has been placed then mark the end of the word as true 

def insert(root, word):
    current = root   #starting at the root
    for char in word:  #for every character in word
        if char not in current.children:  #if word not in path, create one
            current.children[char] = TrieNode() #trieNode is like a node/room, a point in the structure. represent "we typed this much letters so far."
        current = current.children[char] #move down into that child node ( to find exactly where we are currently at)
    current.is_end_of_word = True # after the loop, place every letter then mark the end.



# to check the existence if the word is completed or not, return false. if every letter is checked successfully, then we check again if the current word is the end of the word. based on the insert.
def search(root, word):
    current = root
    for char in word:
        if char not in current.children:
            return False
        current = current.children[char]
    return current.is_end_of_word



# autocomplete, two stage process, 
# 1, walk to the end of the given prefix, fail if the prefix does not exist. 
# 2, from wherever the walk ends, find the possible outwards branch, recursively, collecting any node flagged is_end_of_word along the way
def starts_with(root, prefix):
    current = root
    for char in prefix:  #walk to the end of prefix, search
        if char not in current.children:
            return []    #prefix does not exist, then return nothing, FAIL case.
        current = current.children[char] 

    results = []
    collect_words(current, prefix, results)
    return results

def collect_words(node, current_word, results):
    if node.is_end_of_word:
        results.append(current_word)  #node itself complete a real word, save

    for char, child in node.children.items():  # to explore every branch out of this node.
        collect_words(child, current_word + char, results)




root = TrieNode()
insert(root,"cat")
insert(root, "car")

print(search(root, "cat"))
print(search(root, "ca"))
print(search(root, "dog"))

print(starts_with(root, "ca"))
print(starts_with(root, "do"))


#to search the end of the word, current = whatever we are tracking within the word.