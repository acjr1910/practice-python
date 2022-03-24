class Singly_Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class Doubly_Node:
    __slots__ = '_element', '_next', '_prev'

    def __init__(self, element, prev, next):
        self._element = element
        self._prev = prev
        self._next = next