array_size = int(input())

array = str(input()).split(' ')
array.reverse()

for item in array:
    print('{} '.format(item), end='')