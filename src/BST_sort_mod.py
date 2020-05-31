
class BST_node:
    def __init__(self, val, parent, left):
        self.val = val
        if parent is None:
            self.height = 0
            self.is_root = True
        else:
            self.is_left = left
            self.is_right = not left
            self.is_root = False
            parent.is_leaf = False
            self.height = parent.height + 1
        self.parent = parent
        self.left = None
        self.right = None
        self.is_leaf = True
        self.has_left = False
        self.has_right = False

    def make_leaf_if_needed(self):
        if self.left is None and self.right is None:
            self.is_leaf = True

    def print_node(self, message):
        print("Height: " + str(self.height) + ", " + message + ": " + str(self.val))

    def remove_left(self):
        self.left = None
        self.has_left = False
        self.make_leaf_if_needed()

    def remove_right(self):
        self.right = None
        self.has_right = False
        self.make_leaf_if_needed()

    def replace_parent_pointer(self, node):
        if self.is_left:
            if node is None:
                self.parent.remove_left()
            else:
                self.parent.left = node
                node.parent = self.parent
                node.is_left = True
                node.is_right = False

        else:
            if node is None:
                self.parent.remove_right()
            else:
                self.parent.right = node
                node.parent = self.parent
                node.is_left = False
                node.is_right = True
        self.parent.make_leaf_if_needed()


class BST:
    def __init__(self, val: int):
        self.root = BST_node(val, None, None)
        self.size = 0
        self.height = 0

    def insert(self, val, subtree_root):
        # print("Inserting:" + str(val))
        self.size += 1
        tmp_node = subtree_root
        # When smaller go left
        if val <= tmp_node.val:
            if tmp_node.left is None:
                tmp_node.left = BST_node(val, tmp_node, True)
                tmp_node.has_left = True
            else:
                self.insert(val, tmp_node.left)
        elif val > tmp_node.val:
            if tmp_node.right is None:
                tmp_node.right = BST_node(val, tmp_node, False)
                tmp_node.has_right = True
            else:
                self.insert(val, tmp_node.right)

    def find_min(self, subtree_root):
        assert subtree_root is not None
        # print("is left none: " + str(subtree_root.left == None))
        if subtree_root.left is not None:
            return self.find_min(subtree_root.left)
        else:
            return subtree_root

    def remove_left_most_element(self, node):
        # node.print_node("Val")
        if node.is_root:
            assert self.root is node
            assert node.parent is None
            assert not node.has_left
            if node.has_right:
                self.root = node.right
                node.right.is_root = True
                node.right.parent = None
        else:
            assert node.parent is not None
            assert not node.has_left
            if node.has_right:
                assert not node.has_left
                node.replace_parent_pointer(node.right)
            else:
                assert not node.has_right and not node.has_left
                assert node.is_leaf
                node.replace_parent_pointer(None)

    @property
    def find_min_and_remove(self):
        node = self.find_min(self.root)
        # print("Min is : " + str(node.val) + " Root is : " + str(self.root.val))
        assert node is not None
        assert node.left is None
        self.remove_left_most_element(node)
        return node.val

    def print_bst(self, subtree_root, height):
        if self.root == subtree_root:
            subtree_root.print_node("root")
        assert subtree_root.height == height
        left = subtree_root.left
        right = subtree_root.right
        if left is not None:
            left.print_node("left")
            self.print_bst(left, height + 1)
        if right is not None:
            right.print_node("right")
            self.print_bst(right, height + 1)


def BST_sort(array: list):
    size = len(array)
    print(array)
    bst_tree = BST(array[0])
    for i in range(1, size):
        bst_tree.insert(array[i], bst_tree.root)
    # bst_tree.print_bst(bst_tree.root, 0)

    for i in range(size):
        array[i] = bst_tree.find_min_and_remove

    print(array)
