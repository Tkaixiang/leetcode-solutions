# https://leetcode.com/problems/lru-cache/?envType=study-plan-v2&envId=top-interview-150
class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def pop_least_used(self):
        if not self.tail:
            return

        del self.cache[self.tail.key]

        if not self.tail.prev:
            # Only 1 element
            self.tail = None
            self.head = None
            return

        self.tail = self.tail.prev

    def move_to_front(self, node):
        if self.head == node:  # Do nothing if the node is the head itself
            return

        if self.head == None:
            # LL: None
            # No nodes yet, set this as head and tail
            self.head = node
            self.tail = node
        else:
            # If our node has a previous connection, connect that to the next
            # Case 1:
            # [prev][node][next]
            # [prev][next]
            # Case 2:
            # [][prev][node]
            # [][prev]
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

            if self.tail == node:
                self.tail = node.prev

            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        retrieved_node = self.cache[key]
        # Move recently used node to the front
        self.move_to_front(retrieved_node)
        return retrieved_node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Pull out the relevant node based on the key and update the value
            retrieved_node = self.cache[key]
            retrieved_node.value = value
            # Since we just used it, we need to move it to the front
            self.move_to_front(retrieved_node)
        else:
            # Not inside, check capacity first to see if we need to evict the least recently used node
            if self.capacity <= 0:
                self.pop_least_used()
                self.capacity += 1
            # Not inside, create a new node and insert it at the front
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.move_to_front(new_node)
            self.capacity -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
