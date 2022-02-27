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
new_file2.write("Hey there.\nIf you can see this in your console, this means your program works, and you are printing from a file.")
new_file2.close()
print(new_file2)

#Ex:4
file_name = input("Input a name for a file: ")
file = open(file_name, "a")
text = input("Text in the file: ")
file.write(text)

#Ex5:
import json

def extract_information_from_file():
    try:
        file_json_for_riding = open("file_json", "r")
        file_json_read = file_json_for_riding.read()
        list_from_file = json.loads(file_json_read)
    except Exception:
        list_from_file = []
    return list_from_file

def add_new_element_to_file():
    new_element = input("What dish to add? (One element only) ")
    file_json_for_riding = open("file_json", "r")
    file_json_read = file_json_for_riding.read()
    list_from_file = json.loads(file_json_read)
    list_from_file.append(new_element)
    file_json_for_writing = open("file_json", "w")
    list_from_file_json = json.dumps(list_from_file)
    file_json_for_writing.write(list_from_file_json)
    file_json_for_writing.close()
    print(f"Dish {new_element} was added to the list.")
    return

#or

def add_new_element_to_file_2():
    new_element = input("What dish to add? (One element only) ")
    list_from_file = extract_information_from_file()
    list_from_file.append(new_element)
    file_json_for_writing = open("file_json", "w")
    list_from_file_json = json.dumps(list_from_file)
    file_json_for_writing.write(list_from_file_json)
    file_json_for_writing.close()
    print(f"Dish {new_element} was added to the list.")
    return


def prog():
    try:
        print('Input "1" to print out all dishes')
        print('Input "2" to add a new dish')
        number = int(input("What is your choice? "))
        if number == 1:
            return print(extract_information_from_file())
        elif number == 2:
            return print(add_new_element_to_file())
        else:
            print('Please input "1" or "2".')
            return
    except ValueError:
        print("Please input a Number")
        return

prog()

#-----------------------------------------or--------------------------------------------------------

def extract_information_from_file2():
    file_json_for_riding = open("file_json", "r")
    file_json_read = file_json_for_riding.read()
    return file_json_read

def add_new_element_to_file2():
    new_element = input("What dish to add? (One element only) ")
    file_json_for_adding = open("file_json", "a")
    file_json_for_adding.write(new_element)
    file_json_for_adding.write(", ")
    file_json_for_adding.close()
    print(f"Dish {new_element} was added to the list.")
    return


def prog2():
    try:
        print('Input "1" to print out all dishes')
        print('Input "2" to add a new dish')
        number = int(input("What is your choice? "))
        if number == 1:
            return print(extract_information_from_file2())
        elif number == 2:
            return print(add_new_element_to_file2())
        else:
            print('Please input "1" or "2".')
            return
    except ValueError:
        print("Please input a Number")
        return

prog2()

#Ex1(Extra)
create_file = open("file.txt", "w")
create_file.write("Hey there.\nIf you can see this in your console, this means your program works, and you are printing from a file.")
create_file.close()
open_file_r = open("file.txt", "r")
read_file = open_file_r.read()
oneline_file = read_file.replace("\n", " ")
punctuations_list = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for el in punctuations_list:
    oneline_file = oneline_file.replace(el, "")
words_list = oneline_file.split(" ")
print(f"The file contains {len(words_list)} words.")

#Ex2(Extra)
create_file = open("file.txt", "w")
create_file.write("Hey there.\nIf you can see this in your console, this means your program works, and you are printing from a file.")
create_file.close()
open_file_r = open("file.txt", "r")
read_file = open_file_r.read()
oneline_file = read_file.replace("\n", " ")
punctuations_list = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for el in punctuations_list:
    oneline_file = oneline_file.replace(el,"")
one_string = oneline_file.replace(" ", "")
elements_list = list(one_string)
print(f"The file contains {len(elements_list)} letters")
print(f"The file contains {len(read_file)} characters")

#Ex3(Extra)
create_file = open("file.txt", "w")
create_file.write("Hey there.\nIf you can see this in your console, this means your program works, and you are printing from a file.")
create_file.close()
open_file_r = open("file.txt", "r")
read_file = open_file_r.read()
line_list = read_file.split("\n")
a = max(line_list)
print(a)
