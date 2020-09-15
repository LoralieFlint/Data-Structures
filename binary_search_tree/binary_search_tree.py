"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
    # compare target value to node value
    # if value > node value
        if value >= self.value:
            # go right
            # if node.right is None
            if self.right is None:
                # create the new node here
                self.right = BSTNode(value)
            else:
                # do the same thing AKA recure
                # insert value into node right
                right_child = self.right
                right_child.insert(value)
            # else if value is < node value
            if value < self.value:
                # go left
                # if node.left is None
                if self.left is None:
                    # create node
                    self.left = BSTNode(value)
                else: 
                    # do the same thing
                    # compare go left or right
                    # insert value to node left
                    left_child = self.left
                    left_child.insert(value)





    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if single element
        # compare target value to node value
        if self.value == target:
            return True
        # if target > node value:
        # go right
        # if node.right is None:
        # weve traversed the tree and havent found it 
        # return False
        elif target > self.value and self.right:
            return self.right.contains(target)
        # else
        # do the same thing
        # return node right contains target
        # else if target < node value 
        # go left 
        elif target < self.value and self.left:
            return self.right.contains(target)
        # if node left is None
        # return False
        # else
        # do the same thing
        # compare go left or right
        # return node left contains target 
        return False

#     """Return the maximum value found in the tree"""
    def get_max(self):
        if self.value and self.right:
            if self.value < self.right.value:
                return self.right.get_max()
        else:
            return self.value
        

#     """ Call the function `fn` on the value of each node"""
    def for_each(self, fn): # recursive
        if self.value is None:
            return
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)


    # def for_each_iterative(self, fn): # iterative
    #     # depth first traversal iterative 
    #     # start at the root 
    #     cur_node = self
    #     # push it on the stack 
    #     stack = Stack()
    #     stack.push(cur_node)
    #     # while stack is not empty
    #     while len(stack) > 0:
    #         cur_node = stack.pop()
    #         # push right
    #         if cur_node.right is not None:
    #             stack.push(cur_node.right)
    #         # push left
    #         if cur_node.left is not None:
    #             stack.push(cur_node.left)
    #         # do the thing with the current node
    #         fn(cur_node.value)

#     # Part 2 -----------------------
#     """ Print all the values in order from low to high
#      Hint:  Use a recursive, depth first traversal """
    def in_order_print(self):
        pass

#     """ Print the value of every node, starting with the given node,
#      in an iterative breadth first traversal"""
    def bft_print(self, node):
        # create a que for nodes
        # add the first node to the que
        # while que is not empty
            # remove the first node from the que
            # print the removed node
            # add all children into the que
        pass

#     """ Print the value of every node, starting with the given node,
#      in an iterative depth first traversal"""
    def dft_print(self, node):
        # create a stack for nodes
        # add the first node to the stack
        # while the stack is not empty
            # get the current node from the top of the stack 
            # print that node
            # add all children to the stack
        pass

# """
#     # Stretch Goals -------------------------
#     # Note: Research may be required
# """

#    """  Print Pre-order recursive DFT"""
#     # def pre_order_dft(self):
#     #     pass

#     """ Print Post-order recursive DFT"""
#     # def post_order_dft(self):
#     #     pass

# """
# This code is necessary for testing the `print` methods
# """
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()