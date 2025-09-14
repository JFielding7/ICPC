class Tree:
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            self.iterated = False

    @staticmethod
    def construct_tree(row, start, end):
        if start > end:
            return None
        if start == end:
            return Tree.Node((row[start][1], row[start][2]))

        mid = start + end >> 1
        return Tree.Node((row[mid][1], row[mid][2]), Tree.construct_tree(row, start, mid - 1),
                         Tree.construct_tree(row, mid + 1, end))

    def __init__(self, row, start, end):
        self.root = Tree.construct_tree(row, start, end)
        self.len = end - start + 1
        self.iter_stack = []

    def delete_node(self, node, parent):
        self.len -= 1

        if node.left is None:
            if parent is None:
                self.root = node.right
            else:
                if node is parent.left:
                    parent.left = node.right
                else:
                    parent.right = node.right
        else:
            parent = node
            curr = node.left

            while curr.right:
                parent = curr
                curr = curr.right

            if parent.left is curr:
                parent.left = curr.left
            else:
                parent.right = curr.left

            node.val = curr.val

    def delete_extreme(self, val, cmp, cmp_true_next, cmp_false_next):
        extreme_parent = extreme = parent = None
        node = self.root

        while node:
            curr = node

            if cmp(node.val[0], val):
                if extreme is None or cmp(extreme.val[0], node.val[0]):
                    extreme_parent = parent
                    extreme = node
                node = cmp_true_next(node)
            else:
                node = cmp_false_next(node)

            parent = curr

        if extreme is None:
            return None

        val = extreme.val
        self.delete_node(extreme, extreme_parent)
        return val

    left_node = lambda node: node.left
    right_node = lambda node: node.right

    def delete_largest_less_than(self, val):
        return self.delete_extreme(val, int.__lt__, Tree.right_node, Tree.left_node)

    def delete_smallest_greater_than(self, val):
        return self.delete_extreme(val, int.__gt__, Tree.left_node, Tree.right_node)

    def __len__(self):
        return self.len

    def __iter__(self):
        self.iter_stack.append(self.root)
        return self

    def __next__(self):
        if not self.iter_stack:
            raise StopIteration

        curr = self.iter_stack[-1]

        while curr.left and not curr.left.iterated:
            curr = curr.left
            self.iter_stack.append(curr)

        self.iter_stack.pop()
        curr.iterated = True

        if curr.right:
            self.iter_stack.append(curr.right)

        return curr.val


def array_input():
    return map(int, input().split())


def row_input():
    return sorted(map(lambda e: (e[1][0], e[1][1], e[0]), enumerate(zip(array_input(), array_input()), 1)))


def construct_trees_by_price(row):
    trees = []
    curr_price = row[0][0]
    curr_start = 0

    for i, (price, height, index) in enumerate(row):
        if price != curr_price:
            trees.append(Tree(row, curr_start, i - 1))
            curr_price = price
            curr_start = i

    trees.append(Tree(row, curr_start, len(row) - 1))
    return trees


def azulejos():
    input()
    back_row = row_input()
    front_row = row_input()

    ordered_back = []
    ordered_front = []

    back_trees = construct_trees_by_price(back_row)
    back_i = 0
    front_trees = construct_trees_by_price(front_row)
    front_i = 0

    while front_i < len(front_trees) and back_i < len(back_trees):
        front_tree = front_trees[front_i]
        back_tree = back_trees[back_i]

        if len(front_tree) < len(back_tree):
            for front_height, front_index in front_tree:
                back_tile = back_tree.delete_smallest_greater_than(front_height)

                if back_tile is None:
                    print("impossible")
                    return

                _, back_index = back_tile
                ordered_back.append(back_index)
                ordered_front.append(front_index)
            front_i += 1
            back_i += len(back_tree) == 0
        else:
            for back_height, back_index in back_tree:
                front_tile = front_tree.delete_largest_less_than(back_height)

                if front_tile is None:
                    print("impossible")
                    return

                _, front_index = front_tile
                ordered_front.append(front_index)
                ordered_back.append(back_index)
            back_i += 1
            front_i += len(front_tree) == 0

    print(" ".join(map(str, ordered_back)))
    print(" ".join(map(str, ordered_front)))


azulejos()
