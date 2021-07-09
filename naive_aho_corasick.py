from collections import deque

class aho:
    def __init__(self):
        self.go = {}
        self.output = []
        self.breaks = None


def aho_trie(list1):
    root = aho()

    for way in list1:
        cur = root
        for i in way:
            cur = cur.go.setdefault(i, aho())

        cur.output.append(way)

    return root

def aho_set_failure_links(list1):
    root = aho_trie(list1)
    queue = []

    for child in root.go.values():
        queue.append(child)
        child.breaks = root

    while len(queue) > 0:
        right_child = queue.pop(0)

        for clue, uniquechild in right_child.go.items():
            queue.append(uniquechild)
            firstpoint = right_child.breaks

            while firstpoint != None and clue not in firstpoint.go:
                firstpoint = firstpoint.breaks
            uniquechild.breaks = firstpoint.go[clue] if firstpoint else root
            uniquechild.output += uniquechild.breaks.output

    return root

def aho_search(y, root, call):  #searching the input
    point = root

    for i in range(len(y)):
        while point != None and y[i] not in point.go:
            point = point.breaks
        if point == None:
            point = root
            continue
        point = point.go[y[i]]
        for design in point.output:
            call(i - len(design) + 1, design)

def found(loc, list1):    #printing the results
    print (f"The Design found at position {loc}, found­ pattern: {list1}")

list1 = ['a', 'ab', 'aa', 'abc', 'bc', 'bca', 'cc', 'c', 'cba', 'cab']
y = "abcbaacab"
main = aho_set_failure_links(list1)
aho_search(y, main, found)

