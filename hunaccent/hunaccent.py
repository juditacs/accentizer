from collections import deque
from string import punctuation
import importlib.resources


class Hunaccent(object):

    accents = {
        'a': ['a', 'á'],
        'e': ['e', 'é'],
        'i': ['i', 'í'],
        'o': ['o', 'ó', 'ö', 'ő'],
        'u': ['u', 'ú', 'ü', 'ű'],
    }
    punct = set(punctuation)

    def __init__(self, tree_dir = "hunaccent.tree"):
        self.load_trees(tree_dir)

    def load_trees(self, tree_dir):
        self.trees = {}
        for fn in importlib.resources.files(tree_dir).iterdir():
            self.trees[fn.name] = Tree(fn)
        self.window = self.trees['a'].window

    def accentize(self, text):
        self.slidew = deque(' ' * (2*self.window+1))
        outw = []
        for ch in text + ' '*self.window:
            nc = Hunaccent.normalize_char(ch)
            if not nc:
                continue
            self.slidew.append(nc)
            self.slidew.popleft()
            c = self.slidew[self.window]
            if c.lower() in self.trees:
                if c.isupper():
                    outw.append(self.accentize_char().upper())
                else:
                    outw.append(self.accentize_char())
            else:
                outw.append(c)
        return ''.join(outw)[self.window:]

    def accentize_char(self):
        label = self.trees[self.slidew[self.window]].classify(self.slidew)
        return Hunaccent.accents[self.slidew[self.window]][label]

    @staticmethod
    def normalize_char(char):
        if char.isalpha():
            return char.lower()
        if char.isspace():
            return ' '
        if char.isdigit():
            return '0'
        if char in Hunaccent.punct:
            return '_'
        return '*'

    def print_node(self, char, node_id):
        self.trees[char].nodes[node_id].print()


class Tree(object):
    def __init__(self, fn):
        self.load_from_file(fn)

    def load_from_file(self, fn):
        with fn.open() as f:
            self.read_meta_info(f.readline())
            self.nodes = []
            for l in f:
                self.nodes.append(self.read_node(l))

    def read_meta_info(self, stream):
        meta = stream.split()
        self.window = int(meta[1])
        self.length = int(meta[0])

    def read_node(self, line):
        fd = line[2:].split()
        ch = line[0]
        pos = int(fd[0])
        left = int(fd[1])
        right = int(fd[2])
        out = int(fd[3])
        return Node(ch, pos, left, right, out, self.window, len(self.nodes))

    def classify(self, window, draw_tree:bool = False):
        index = 0
        limit = 200
        if draw_tree:
            print('ACCENTIZING: [{0}[{1}]{2}]'.format(
                    ''.join(window[i] for i in range(self.window)),
                    window[self.window],
                    ''.join(window[i] for i in range(self.window+1, 2*self.window+1))))
        while not self.nodes[index].is_final:
            if draw_tree:
                self.nodes[index].print()
            index = self.nodes[index].decide(window)
            limit -= 1
            if limit < 0:
                return 0
        if draw_tree:
            self.nodes[index].print()
        return self.nodes[index].label


class Node(object):
    def __init__(self, char, pos, left, right, out, window, id_):
        self.char = char
        self.pos = pos
        self.left = left
        self.right = right
        self.is_final = False if out == -1 else True
        self.label = out
        self.window = window
        self.id_ = id_

    def print(self):
        if not self.is_final:
            print(' ({0}), {1: 2d}: [{2}], left: {3}, right: {4}'.format(
                    self.id_, self.pos, self.char, self.left, self.right))
        else:
            print(' LEAF ({0}), {1: 2d}: [{2}], out: {3}'.format(
                    self.id_, self.pos, self.char, self.label))

    def decide(self, w):
        return self.right if w[self.window+self.pos] == self.char else self.left


hunaccent = Hunaccent()
