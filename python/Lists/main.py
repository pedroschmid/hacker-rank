if __name__ == '__main__':
    array = list()

    n = int(input())

    for i in range(n):
        entry = input().split(' ')

        if entry[0] == 'insert':
            array.insert(int(entry[1]), int(entry[2]))

        if entry[0] == 'append':
                array.append(int(entry[1]))

        if entry[0] == 'remove':
            array.remove(int(entry[1]))

        if entry[0] == 'pop':
            array.pop() 

        if entry[0] == 'sort':
            array.sort()

        if entry[0] == 'reverse':
            array.reverse()

        if entry[0] == 'print':
            print(array)
