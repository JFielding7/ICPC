def same_shape_node(node0, node1):
    return ((node0 is None) == (node1 is None) and
            ((node0 is None) or
             (same_shape_node(node0.left, node1.left) and same_shape_node(node0.right, node1.right))))


class Tree:
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Tree.Node(val)
        else:
            prev = None
            curr = self.root
            is_left_child = False

            while curr:
                prev = curr

                if val < curr.val:
                    is_left_child = True
                    curr = curr.left
                else:
                    is_left_child = False
                    curr = curr.right

            if is_left_child:
                prev.left = Tree.Node(val)
            else:
                prev.right = Tree.Node(val)

    def same_shape(self, other):
        return same_shape_node(self.root, other.root)


def ceiling():
    num_trees = int(input().split()[0])
    shapes = 0
    trees = []

    for i in range(num_trees):
        curr_tree = Tree()

        for num in map(int, input().split()):
            curr_tree.insert(num)

        new_shape = True
        for tree in trees:
            if curr_tree.same_shape(tree):
                new_shape = False
                break

        shapes += new_shape
        trees.append(curr_tree)

    print(shapes)


ceiling()
