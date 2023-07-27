class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):  
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s




#ITERATIVE APPROACH

def size(self):
    if self.root is None:
        return 0
    
    stack = Stack()
    stack.push(self.root)
    size = 1

    while stack:            #while loop which runs as long as stack is not empty
      node = stack.pop()
      if node.left:
        size += 1
        stack.push(node.left)
      if node.right:
        size += 1
        stack.push(node.right)
    return size



#RECURSIVE APPROACH

def size_(self, node):
    if node is None:
        return 0
    return 1 + self.size_(node.left) + self.size_(node.right)