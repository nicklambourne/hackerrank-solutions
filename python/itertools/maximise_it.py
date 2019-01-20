# Parse input
k, m = [int(x) for x in input().strip().split(" ")]
lists = []
for i in range(k):
    lists.append([int(x) for x in input().strip().split(" ")][1:])

combinations = [[i] for i in lists[0]]

# Create combinations
for list_ in lists[1:]:
    new_combinations = []
    for item in list_:
        for combination in combinations:
            new_combinations += combination.append(item)
    combinations = new_combinations

# Perform function on each
s = []
for combination in combinations:
    sum_ = 0
    for item in combination:
        sum_ += item**2
    s.append(sum_ % m)

# Return max
print(max(x))