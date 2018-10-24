class LRUCache:
    capacity = 0
    cache = {}
    stack = []
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.stack = []
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value = -1
        if (key in self.cache):
            self.stack.remove(key)
            self.stack.append(key)
            value = self.cache[key]
        
        return value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """     
        if (len(self.cache) < self.capacity):
            self.cache[key] = value
            if (key in self.stack):
                self.stack.remove(key)
            self.stack.append(key)
        else:
            if (key not in self.cache):
                # Get least recently used and remove it
                lru = self.stack[0]
                self.stack.remove(lru)
            
                # Remove from cache
                self.cache.pop(lru)
                
            self.cache[key] = value
            
            # Remove from stack
            if (key in self.stack):
                self.stack.remove(key)
            self.stack.append(key)

