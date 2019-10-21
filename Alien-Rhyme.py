"""
Read the problem here:

https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e05
"""


class TrieNode:
    __slots__ = "key", "value", "children"

    def __init__(self, key=None, value=None):
        """
        Trie node class constructor
        :param key: letter that denotes the path
        :param value: 1 if the word ends on this letter.
        Helps explore pairs indicating how many words are left to be paired
        """
        self.key = key
        self.value = value
        # Child letters from this letter
        self.children = dict()

    def get_value(self):
        """
        :return: value
        """
        return self.value

    def get_key(self):
        """
        :return: key
        """
        return self.key

    def add_child(self, node):
        """
        Add the child in children
        :param node: child to add
        :return: None
        """
        self.children.append(node)

    def update_value(self, value):
        """
        Add the value into existing value
        :param value: to be added
        :return: None
        """
        self.value += value

    def get_children(self):
        """
        :return: children dictionary {key: TrieNode}
        """
        return self.children

    def has_children(self):
        """
        Return if the node has children
        :return: True if it has children, False otherwise
        """
        return len(self.children) > 0

    def __repr__(self):
        """
        Representation of the node
        :return:
        """
        return "root = " + str(self.key) + ", value = " + str(self.value) + ", children = " + "".join(
            self.children.keys())


def add_branch(root, w):
    """
    Add the word branch in the tree from given root node
    :param root: root TrieNode
    :param w: word
    :return: None
    """
    if len(w) > 0:
        if w[-1] not in root.children:
            root.children[w[-1]] = TrieNode(w[-1], 0)

        add_branch(root.children[w[-1]], w[:-1])

    if len(w) == 0:
        root.update_value(1)


def build_trie(root, words):
    """
    Build a trie from the root node and the list of words
    :param root: root Node
    :param words: list of words
    :return: None
    """
    for i in range(len(words)):
        add_branch(root, words[i])


def __explore_trie(node, counter):
    """
    Helper function of explore_trie()
    Update every node's value based on children's values to check if the
    word rhyme is already found, or not found
    :param node: node to explore the trie from
    :param counter: number of words that can be used so far
    :return: root node's value and counter
    """
    if not node.has_children():
        return node.get_value(), counter

    for child in node.get_children().values():
        res, counter = __explore_trie(child, counter)
        node.update_value(res)
    if node.get_value() >= 2 and node.get_key() != "*":
        node.update_value(-2)
        counter += 2
    return node.get_value(), counter


def explore_trie(root):
    """
    Update root.value based on pairs found and update counter for every pair found
    while exploring the trie
    :param root: root node
    :return: Number of maximum words found that can be paired with only one other word
    sharing a unique suffix
    """
    return __explore_trie(root, 0)[1]


def alien_rhyme(words):
    """
    Find the number of maximum words that are in valid rhymes
    Valid rhyme pair are two words that share a common unique suffix that no other pair has
    :param words:
    :return:
    """
    root = TrieNode("*", 0)
    build_trie(root, words)
    counter = explore_trie(root)
    return counter


def main():
    T = int(input())

    for t in range(T):
        n = int(input())
        alien_poetry = list()

        for i in range(n):
            alien_poetry.append(input())

        print("Case #" + str(t + 1) + ": " + str(alien_rhyme(alien_poetry)))


if __name__ == '__main__':
    main()
