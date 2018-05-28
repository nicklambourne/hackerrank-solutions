"""
Nick's Note: I strongly disagree that a global is required for this task, but it
was provided by the question.
"""


import xml.etree.ElementTree as etree


maxdepth = 0


def depth(elem, level):
    global maxdepth
    level += 1
    if len(elem) == 0:
        if level > maxdepth:
            maxdepth = level
    else:
        for node in elem:
            depth(node, level)
    return maxdepth


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)