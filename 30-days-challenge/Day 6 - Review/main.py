number = int(input())

for i in range(0, number):
    string = str(input())

    print('{} {}'.format(string[0::2], string[1::2]))

