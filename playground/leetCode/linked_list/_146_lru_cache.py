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
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if key in self.cache:
            # If key is already present, move it to the end
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            # If the cache is full, remove the least recently used item (the first in the order list)
            old_key = self.order.pop(0)
            del self.cache[old_key]

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
    lru_cache.get(1)

    # Display updated cache state
    lru_cache.display_cache()  # Output: [(2, 'Two'), (3, 'Three'), (1, 'One')]

    # Add a new item, causing eviction of the least recently used item (2)
    lru_cache.put(4, "Four")

    # Display updated cache state
    lru_cache.display_cache()  # Output: [(3, 'Three'), (1, 'One'), (4, 'Four')]
