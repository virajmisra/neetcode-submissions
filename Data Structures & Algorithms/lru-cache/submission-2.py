class Node:
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # int (key) -> Node(key,value)
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        p = node.prev
        n = node.next

        p.next = n
        n.prev = p
    
    def insert(self, node): # to the right of double linked list
        p = self.right.prev
        n = self.right

        p.next = node
        n.prev = node

        node.prev = p
        node.next = n
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key,value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        
