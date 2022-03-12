#Ex1:
lambda_square = lambda list1: list1 ** 2
lambda_cube = lambda list1: list1 ** 3
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_square = list()
my_list_cube = list()
for el in my_list:
    le = lambda_square(el)
    my_list_square.append(le)
print(my_list_square)

for el in my_list:
    le = lambda_cube(el)
    my_list_cube.append(le)
print(my_list_cube)

#Ex2:
orig_list = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
palindrome_list = list()
def check_palindrome(a: str):
    z = a.replace(" ", "")
    divide = list(z)
    divide_reverse = []
    for el in divide:
        divide_reverse.append(el)
    divide_reverse.reverse()
    if divide == divide_reverse:
        return True
    else:
        return False

for le in orig_list:
    if check_palindrome(le) == True:
        palindrome_list.append(le)
print(palindrome_list)

#Ex3:
def validate_numeric(funct):
    try:
        funct == float
    except ValueError:
        print(("Is not Numeric"))

@validate_numeric
def numeric(a):
    return a


print(numeric(3))