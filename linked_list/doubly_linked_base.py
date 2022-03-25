from utils.nodes import Doubly_Node


class DoublyLinkedBase:
    def __init__(self):
        self._header = Doubly_Node(None, None, None)
        self._trailer = Doubly_Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = Doubly_Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        sucessor = node._next
        predecessor._next = sucessor
        sucessor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None  # deprecate node
        return element
