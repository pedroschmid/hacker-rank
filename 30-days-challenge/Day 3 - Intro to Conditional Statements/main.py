number = int(input())

if number >= 1 and number <= 100:
    if number % 2 != 0:
        print('Weird')
    else:
        if number in range(2, 5+1):
            print('Not Weird')
        elif number in range(6, 20+1):
            print('Weird')
        elif number >= 20:
            print('Not Weird')
