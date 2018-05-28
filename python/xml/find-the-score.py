import sys
import xml.etree.ElementTree as etree


def score(node):
    if len(node) == 0:
        return len(node.attrib)
    else:
        total = 0
        total += len(node.attrib)
        for nd in node:
            total += score(nd)
        return total


def get_attr_number(root):
    return score(root)


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))