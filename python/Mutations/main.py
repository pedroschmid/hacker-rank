def mutate_string(string, position, character):
    l = list(string)
    l[position] = character

    return "".join(l)

if __name__ == '__main__':
    s = str(input())
    i, c = str(input()).split()
    s_new = mutate_string(s, int(i), c)

    print(s_new)