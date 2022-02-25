#Ex1:
text = input("Type anything: ")
try:
    text = int(text)
    print("Is a Integer")
except ValueError:
    print("Is not Integer")
try:
    text = float(text)
    print("Is a Float")
except ValueError:
    print("Is not Float")
try:
    text = str(text)
    print("Is a String")
except ValueError:
    print("Is not String")

#Ex2:
import json

new_file = open("test_file.txt", "a")
new_file.write("Hello")
#new_file.seek(0)                     #NOT WORKING
new_file.write("first ")
#new_file_py = json.loads(new_file)   # NOT WORKING if is JSON
new_file.close()

# print(new_file_py)                  #NOT WORKING if is JSON
print(new_file)

#Ex3:
new_file2 = open("test_file.txt", "a")
new_file2.write("Hey there.If you can see this in your console, this means your program works, and you are printing from a file.")
new_file2.close()
print(new_file2)

#Ex:4
file_name = input("Input a name for a file: ")
file = open(file_name, "a")
text = input("Text in the file: ")
file.write(text)

#Ex5:
import json

def print_dishes():
    file_dish_json = open("file_dish.json", "r")
    file_dish_json.read()
    file_dish_list = json.loads(file_dish_json)
    file_dish_list = []
    return file_dish_list



def add_dish():
    dish = input("What dish to add? ")
    file_dish = open("file_dish.json", "a")
    file_dish_json = json.dumps(file_dish)
    file_dish_json.write(dish)
    file_dish_json.write(", ")
    file_dish_json.close()
    print(f"Dish {dish} was added to the list.")
    return

def prog():
    try:
        print('Input "1" to print out all dishes')
        print('Input "2" to add a new dish')
        number = int(input("What is your choice? "))
        if number == 1:
            return print_dishes()
        elif number == 2:
            return add_dish()
        else:
            print('Please input "1" or "2".')
            return
    except ValueError:
        print("Please input a Number")
        return

prog()
