def merge_the_tools(string, k):
    ts = [string[i:i+k] for i in range(0, len(string), k)]
    us = []
    for t in ts:
        new_string = ''
        for letter in t:
            if letter not in new_string:
                new_string += letter
        us.append(new_string)
    for word in us: 
        print(word)
