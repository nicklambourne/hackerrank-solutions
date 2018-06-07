from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : " + tag)
        for attr in attrs:
            print('-> ' + attr[0] + ' > ' + str(attr[1]))

    def handle_endtag(self, tag):
        print("End   : " + tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty : " + tag)
        for attr in attrs:
            print('-> ' + attr[0] + ' > ' + str(attr[1]))


n = int(input().strip())
string = ''
for _ in range(n):
    string += input()
parser = MyHTMLParser()
parser.feed(string)
parser.close()