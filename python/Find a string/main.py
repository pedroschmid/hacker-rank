from re import findall

def count_substring(string, sub_string):
    match = findall(f'(?={sub_string})', string)

    return len(match)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)