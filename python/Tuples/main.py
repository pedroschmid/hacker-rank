if __name__ == '__main__':
    array = list()

    n = int(input())
    entry = str(input()).split(' ')

    for item in entry:
        array.append(int(item))

    t = tuple(array)

    print(hash(t))
