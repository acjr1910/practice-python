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


class BinaryTreeNode():
    __slots__ = '_element', '_parent', '_left', '_right'

    def __init__(self, element, parent=None, left=None, right=None):
        self._element = element
        self._parent = parent
        self._left = left
        self._right = right
