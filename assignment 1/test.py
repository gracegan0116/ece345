# Python program to find BST keys in given range

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# The function prints all the keys in the gicven range
# [k1..k2]. Assumes that k1 < k2
def Print1(root, k1, k2):
    # Base Case
    if root is None:
        return

    # Since the desired o/p is sorted, recurse for left
    # subtree first. If root.data is greater than k1, then
    # only we can get o/p keys in left subtree
    if root.data > k1:
        Print1(root.left, k1, k2)

    # If root's data lies in range, then prints root's data
    if root.data>=k1 and root.data<=k2:
        print(root.data)

    # If root.data is smaller than k2, then only we can get
    # o/p keys in right subtree
    if root.data<k1 or root.data<k2:
        Print1(root.right, k1, k2)

    # Driver function to test above function


k1 = 10;
k2 = 25;
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)

Print1(root, k1, k2)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
