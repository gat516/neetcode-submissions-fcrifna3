class LRUCache:

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def get(self, key):
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        
        return self.cache[key]

    def put(self, key, value):
        #handle update
        if key in self.cache:
            self.cache.move_to_end(key)
        #update key
        self.cache[key] = value
        #pop
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)