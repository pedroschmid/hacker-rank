if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    max = -100
    runner = -100
    for i in arr:
        if i > max:
            runner = max
            max = i
    print(runner)
