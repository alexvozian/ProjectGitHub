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
def validate_numeric(func):
    def wrapper_func(*args, **kwargs):
        arg_list = args[0]
        for arg in arg_list:
            if type(arg) == int or type(arg) == float:
                pass
            else:
                raise TypeError

        value_returned = func(*args, **kwargs)
        print(value_returned)
        return value_returned

    return wrapper_func

@validate_numeric
def numeric(list1):
    return sum(list1)

numeric([3, 2])

#Ex4:
def my_user_input_generator(stop_at):
    user_input = ""
    while user_input != stop_at:
        user_input = input("Please enter something: ")
        yield user_input


for user_input in my_user_input_generator('STOP'):
    if user_input != "STOP":
        print(user_input)