
class bst:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def height(the_bst):
    if the_bst is None:
        return 0
    return 1 + max(height(the_bst.left), height(the_bst.right))


def print_in_order(node):
    if node is None:
        return
    print_in_order(node.left)
    print(node.value)
    print_in_order(node.right)

def print_pre_order(node):
    if node is None:
        return
    print(node.value)
    print_in_order(node.left)
    print_in_order(node.right)

def print_post_order(node):
    if node is None:
        return
    print_in_order(node.left)
    print_in_order(node.right)
    print(node.value)


def find_node(node, value):
    while node is not None and node.value != value:
        if node.value > value:
            node = node.left
        else:
            node = node.right
        return node


def reverse(llist, start, stop):
    if start < stop - 1:
        llist[start], llist[stop - 1] = llist[stop - 1], llist[start]
        reverse(llist, start + 1, stop -1)

def ssum(llist, i):
    if i != len(llist):
        return llist[i] + ssum(llist, i + 1)
    return 0


if __name__ == "__main__":
    x = bst(8, bst(3, bst(1), bst(6, bst(4), bst(7))), bst(10, None, bst(14, bst(13))))
    llist = [5, 4, 3, 2, 1]
    print(ssum(llist, 0))

