'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Ex:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

# Solution

class LRUCache:

    def __init__(self, capacity: int):
        self.main_d = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.main_d:
            # Need to update it's position
            ret = self.main_d[key]
            temp_d = {key: ret}
            del self.main_d[key]
            self.main_d.update(temp_d)
            #print('Get ', key, ' .. current dict is = ', self.main_d)
            return ret
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        temp_d = {key: value}
        # Check if main_d contains 1:
        #print('Putting in ', key, value, ' into current dict ', self.main_d)
        if key in self.main_d:
            del self.main_d[key]
            self.main_d.update(temp_d)
        else:
            # Check if main_d is max length
            if len(self.main_d) == self.capacity:
                for x in self.main_d.keys():
                    del self.main_d[x]
                    break
            self.main_d[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
