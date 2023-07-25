class Queue(object):
    def __init__(self):
        self.items = []
      
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
        
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)
    


def levelorder_print(self, start):
    if start is None:
        return
    
    queue = Queue()
    queue.enqueue(start)

    traversal = ""
    while len(queue) > 0:
        traversal += str(queue.peek()) + "-"
        node = queue.dequeue()

        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    
    return traversal