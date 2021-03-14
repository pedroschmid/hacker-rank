i = int(input())
d = float(input())
s = str(input())

def print_sum(x, y):
    print(x + y)
    
integer_input = int(input()) 
double_input = float(input())
string_input = str(input())

print_sum(i, integer_input)
print_sum(d, double_input)

print("{}{}".format(s, string_input))
