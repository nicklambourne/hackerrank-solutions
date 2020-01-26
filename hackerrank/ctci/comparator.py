class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return self.name + " " + str(self.score)
    def comparator(a, b):
        if a.score != b.score:
            return b.score - a.score
        else:
            if a.name == b.name:
                return 0
            names = sorted([a.name, b.name], reverse=True)
            if names[0] == a.name:
                return 1
            else:
                return -1


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
