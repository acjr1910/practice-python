from tree import Tree


class BinaryTree(Tree):
    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        parent = self.parent()
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def child(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def bfs(self):
        """Breadth First Search"""
        return NotImplementedError('TODO: implement this')

    def dfs_pre_order(self):
        """Depth First Search"""
        return NotImplementedError('TODO: implement this')

    def dfs_post_order(self):
        """Depth First Search"""
        return NotImplementedError('TODO: implement this')

    def dfs_in_order(self):
        """Depth First Search"""
        return NotImplementedError('TODO: implement this')
