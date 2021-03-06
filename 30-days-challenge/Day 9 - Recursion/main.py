def factorial(n):
    if n >= 2 and n <= 12:
        return (n * factorial(n-1))
    else:
        return 1

n = int(input())

result = factorial(n)

print(result)