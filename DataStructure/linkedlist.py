# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.nextnode = None  # Initialize next as null

    def __repr__(self):
        return f'{self.data}'


a = Node(1) # declaring data in each node
b = Node(2)
c = Node(3)

a.nextnode = b # link first node to second node
b.nextnode = c # link second node to third node

print(a)
print(b)
print(c)