class Tree():
    def __init__(self):
        self.data = []
        
def traverse(self, visit, order='pre'):
    if order == 'pre':
        visit(self)
    if self.left is not None:
        self.left.traverse(visit, order)
    if order == 'in':
        visit(self)
    if self.right is not None:
        self.right.traverse(visit, order)
    if order == 'post':
        visit(self)

        