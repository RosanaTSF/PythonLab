class BSTNode(object):
 
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
 
    def remove(self, key):
        if key < self.key:
            self.left = self.left.remove(key)
        elif key > self.key:
            self.right = self.right.remove(key)
        else:
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            #copia os valores do nó substituto.
            tmp = self.right._min()
            self.key, self.value = tmp.key, tmp.value
            self.right._remove_min()
        return self
 
    def _min(self):
        if self.left is None:
            return self
        else:
            return self.left._min()
 
    def _remove_min(self):
        if self.left is None:  # encontrou o min, daí pode rearranjar
            return self.right
        self.left = self.left._removeMin()
        return self