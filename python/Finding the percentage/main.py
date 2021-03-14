def average(array):
    return sum(array) / len(array)

def calculate_average(scores):
    return average(scores)

if __name__ == '__main__':
    students = dict()

    n = int(input())

    for i in range(n):
        entry = str(input()).split(' ')

        students[entry[0]] = [float(entry[1]), float(entry[2]), float(entry[3])]
    
    query = str(input())
    avg_result = average(students[query])

    print(f'{avg_result:.2f}')

