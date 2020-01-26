n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swap_count = 0
iteration_swap_count = None
length = len(a)

while iteration_swap_count != 0:
    iteration_swap_count = 0
    for i in range(length-1):
        if a[i] > a[i+1]:
            swap = a[i]
            a[i] = a[i+1]
            a[i+1] = swap
            iteration_swap_count += 1
    swap_count += iteration_swap_count

print('Array is sorted in {} swaps.'.format(str(swap_count)))
print('First Element: {}'.format(str(a[0])))
print('Last Element: {}'.format(str(a[length-1])))