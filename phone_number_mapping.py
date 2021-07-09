
keyboard_mapping = {
    'a': '2',
    'b': '2',
    'c': '2',
    'd': '3',
    'e': '3',
    'f': '3',
    'g': '4',
    'h': '4',
    'i': '4',
    'j': '5',
    'k': '5',
    'l': '5',
    'o': '6',
    'n': '6',
    'm': '6',
    'p': '7',
    'q': '7',
    'r': '7',
    's': '7',
    'v': '8',
    'u': '8',
    't': '8',
    'w': '9',
    'x': '9',
    'y': '9',
    'z': '9',
}

class aho():
    def __init__(self):
        self.children = {}
        self.output = []
        self.failure_link = None


def solve(keywords, phonenumber):
    int_keywords = transform_keywords_to_numbers(keywords)

    root = construct_aho_trie(int_keywords)

    search_keywords(root, phonenumber)


def search_keywords(root, phonenumber):
    current = root

    for num in phonenumber:
        while current is not None and num not in current.children:
            current = current.failure_link
        if current is None:
            current = root
            continue
        current = current.children[num]
        for output in current.output:
            print(output)


def construct_aho_trie(int_keywords):
    root = initialize_aho_trie(int_keywords)

    return set_failure_links(root)


def set_failure_links(root):
    queue = []

    for child in root.children.values():
        queue.append(child)
        child.failure_link = root

    while len(queue) > 0:
        current = queue.pop()

        for char, child in current.children.items():
            queue.append(child)
            firstbreak = child.failure_link

            while firstbreak is not None and char not in firstbreak.go:
                firstbreak = firstbreak.failure_link

            child.failure_link = firstbreak.go[char] if firstbreak else root
            child.output += child.failure_link.output

    return root


def initialize_aho_trie(keywords):
    root = aho()

    for keyword in keywords:
        current = root

        for char in keyword:
            current = current.children.setdefault(char, aho())

        current.output.append(keyword)

    return root

def transform_keywords_to_numbers(keywords):
    int_keywords = []
    for keyword in keywords:
        int_keywords.append(''.join([keyboard_mapping[char] for char in keyword]))

    return int_keywords


keywords = ['foo', 'bar', 'bat', 'batman']
phonenumber = '12349228626213'

solve(keywords, phonenumber)