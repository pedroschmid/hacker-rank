def split_and_join(line):
    splitted_line = line.split(' ')
    joined_splitted_line = '-'.join(splitted_line)
    
    return joined_splitted_line

if __name__ == '__main__':
    line = str(input())

    result = split_and_join(line)
    print(result)