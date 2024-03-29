# If we traverse a binary tree in-order and it results in a sorted list, then the tree satisfies the BST property.

def is_bst_satisfied(self):
    def helper(node, lower=float("-inf"), upper=float("inf")):
        if not node:
            return True
        
        val = node.data
        if val <= lower or val >= upper:
            return False
        
        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True
        
    return helper(self.root)






# class Node(object):
#   def __init__(self, data):
#     self.data = data
#     self.left = None
#     self.right = None


# class BST(object):
#     def __init__(self, root):
#         self.root = Node(root)

#     def insert(self, data):
#         if self.root is None:
#             self.root = Node(data)
#         else:
#             self._insert(data, self.root)

#     def _insert(self, data, cur_node):
#         if data < cur_node.data:
#             if cur_node.left is None:
#                 cur_node.left = Node(data)
#             else:
#                 self._insert(data, cur_node.left)

#         elif data > cur_node.data:
#             if cur_node.right is None:
#                 cur_node.right = Node(data)
#             else:
#                 self._insert(data, cur_node.right)
#         else:
#             print("Value already in tree!")

#     def inorder_print_tree(self):
#         if self.root:
#             self._inorder_print_tree(self.root)

#     def _inorder_print_tree(self, cur_node):
#         if cur_node:
#             self._inorder_print_tree(cur_node.left)
#             print(str(cur_node.data))
#             self._inorder_print_tree(cur_node.right)

#     def find(self, data):
#         if self.root:
#             is_found = self._find(data, self.root)
#             if is_found:
#                 return True
#             return False
#         else:
#             return None

#     def _find(self, data, cur_node):
#         if data > cur_node.data and cur_node.right:
#             return self._find(data, cur_node.right)
#         elif data < cur_node.data and cur_node.left:
#             return self._find(data, cur_node.left)
#         if data == cur_node.data:
#             return True

#     def is_bst_satisfied(self):
#         def helper(node, lower=float('-inf'), upper=float('inf')):
#             if not node:
#                 return True
            
#             val = node.data
#             if val <= lower or val >= upper:
#                 return False

#             if not helper(node.right, val, upper):
#                 return False
#             if not helper(node.left, lower, val):
#                 return False
#             return True

#         return helper(self.root) 

# bst = BST(4)
# bst.insert(2)
# bst.insert(8)
# bst.insert(5)
# bst.insert(10)

# tree = BST(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
# tree.root.right.left = Node(6)
# tree.root.right.right = Node(7)
# tree.root.right.right.right = Node(8)

# print(bst.is_bst_satisfied())
# print(tree.is_bst_satisfied())
























# def inorder_print(self, start, traversal):
#         """Left->Root->Right"""
#         if start:
#             traversal = self.inorder_print(start.left, traversal)
#             traversal += (str(start.value) + "-")
#             traversal = self.inorder_print(start.right, traversal)
#         return traversal