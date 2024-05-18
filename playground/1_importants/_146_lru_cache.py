
"""
    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

    Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists.
    Otherwise,add the key-value pair to the cache. If the number of keys exceeds
    the capacity from this operation, evict the least recently used key.
    The functions get and put must each run in O(1) average time complexity.

    Example 1:

    Input
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Output
    [null, null, null, 1, null, -1, null, -1, 3, 4]

    Explanation
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1}
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    lRUCache.get(1);    // return 1
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2);    // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1);    // return -1 (not found)
    lRUCache.get(3);    // return 3
    lRUCache.get(4);    // return 4

    Constraints:

    1 <= capacity <= 3000
    0 <= key <= 104
    0 <= value <= 105
    At most 2 * 105 calls will be made to get and put.

"""


from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None
        else:
            # Move the accessed key to the end to mark it as the most recently used
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            # If key is already present, move it to the end
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # If the cache is full, remove the least recently used item
            self.cache.popitem(last=False)
        # Add the new key-value pair to the cache
        self.cache[key] = value

    def display_cache(self):
        print(list(self.cache.items()))


class LRUCache2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key in self.cache:
            # Move the accessed key to the end to mark it as the most recently used
            self.order.remove(key)  # O(n)
            self.order.append(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if key in self.cache:
            # If key is already present, move it to the end
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            # If the cache is full, remove the least recently used item (the first in the order list)
            lru = self.order.pop(0)  # O(n)
            del self.cache[lru]

        # Add the new key-value pair to the cache and the end of the order list
        self.cache[key] = value
        self.order.append(key)

    def display_cache(self):
        print([(key, self.cache[key]) for key in self.order])


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


"""
----------------------------------------------------------------
|Head|       all the add and remove will be between       |Tail|
----------------------------------------------------------------
"""


class LRUCache3:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)  # dummy nodes
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # insert node to the right -> tail
    def insert(self, node) -> None:
        prev, nxt = self.tail.prev, self.tail
        prev.next = node
        nxt.prev = node

        node.next, node.prev = nxt, prev

    # remove node from list
    def remove(self, node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) >= self.capacity:
            # remove from the list and delete the LRU from the cache
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

    def display_cache(self):
        current = self.head.next
        while current != self.tail:
            print(f"({current.key}, {current.value})", end=" -> ")
            current = current.next
        print("None")


if __name__ == '__main__':
    # Example usage:
    my_capacity = 3
    lru_cache = LRUCache(my_capacity)

    lru_cache.put(1, "One")
    lru_cache.put(2, "Two")
    lru_cache.put(3, "Three")

    # Display current cache state
    lru_cache.display_cache()  # Output: [(1, 'One'), (2, 'Two'), (3, 'Three')]

    # Access a key to mark it as most recently used
    value = lru_cache.get(1)
    # print(value)

    # Display updated cache state
    lru_cache.display_cache()  # Output: [(2, 'Two'), (3, 'Three'), (1, 'One')]

    # Add a new item, causing eviction of the least recently used item (2)
    lru_cache.put(4, "Four")

    # Display updated cache state
    lru_cache.display_cache()  # Output: [(3, 'Three'), (1, 'One'), (4, 'Four')]
