dictionary_size = int(input())
phone_book = dict()

for _ in range(dictionary_size):
    name, phone = str(input()).split()
    phone_book[name] = phone

while True:
    try:
        name = str(input())
        phone = phone_book.get(name)

        if phone:
            print('{}={}'.format(name, phone))
        else:
            print('Not found')
    except EOFError:
        break