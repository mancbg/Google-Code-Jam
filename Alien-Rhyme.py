class TrieNode:
    __slots__ = "key", "value", "children"

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.children = dict()

    def get_value(self):
        return self.value

    def get_key(self):
        return self.key

    def add_child(self, node):
        self.children.append(node)

    def update_value(self, value):
        self.value += value

    def get_children(self):
        return self.children

    def has_children(self):
        return len(self.children) > 0

    def __repr__(self):
        return "root = " + str(self.key) + ", value = " + str(self.value) + ", children = " + "".join(
            self.children.keys())


def add_branch(root, w):
    if len(w) > 0:
        if w[-1] not in root.children:
            root.children[w[-1]] = TrieNode(w[-1], 0)

        add_branch(root.children[w[-1]], w[:-1])

    if len(w) == 0:
        root.update_value(1)


def build_trie(root, words):
    for i in range(len(words)):
        add_branch(root, words[i])


def __explore_trie(node, counter):
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
    return __explore_trie(root, 0)[1]


def alien_rhyme(words):
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
