def height(self, node):
    if node is None:
        return -1        #we return -1 on line 3 as we have gone past the leaf nodes, Once a leaf node discovers that its left and right children are reporting heights of -1 each, it will add 1 to -1 and return 0 as its height.
    left_height = self.height(node.left)
    right_height = self.height(node.right)

    return 1 + max(left_height, right_height)