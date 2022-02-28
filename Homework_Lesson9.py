#Ex1:
def Fibonacci_number(number):
    w = [0, 1]
    for el in range(number):
        w.append(sum(w[-2:]))
    print(w[:-2])

Fibonacci_number(8)

#Ex2:
from datetime import datetime
import json


def extract_information_from_file_list(file_name):
    try:
        file_json_for_riding = open(file_name, "r")
        file_json_read = file_json_for_riding.read()
        list_from_file = json.loads(file_json_read)
    except Exception as ex:
        print(ex)
        list_from_file = []
    return list_from_file


info = extract_information_from_file_list("C:\\Users\\vozia\\PycharmProjects\\ProjectGitHub\\big_file.json")
name_list = list()
position_list = list()
salary_list = list()
start_of_work_list = list()
top_salary_name = list()
top_longest_name = list()
for el in info:
    name_list.append(el["name"])
    position_list.append(el["position"])
    salary_list.append(el["salary"])
    start_of_work_list.append(el["employee_from"])
print(f"List of employers are: {name_list}")
print(f"List of positions are: {position_list}")
print(f"Amount of salary the company has to pay per month in total are: {sum(salary_list)}")
tax = float(input("Input a TAX RATE (%): "))
print(f"Amount of money the company has to pay in TAXES per month are: {(sum(salary_list) / 100) * tax}")
rev = sorted(salary_list)
rev.reverse()
for le in rev:
    for el in info:
        if le == el["salary"]:
            top_salary_name.append(el)
print(f"Top 10 highest paid employees from highest paid to lower are: {top_salary_name[:10]}")
sorted_dates = list()
for yy in start_of_work_list:
    sorted_dates.append(datetime.strptime(yy, "%m/%d/%Y"))
ver = sorted(sorted_dates)
ver_str = [date.strftime("%m/%d/%Y") for date in ver]
for tt in ver_str:
    for el in info:
        if tt == el["employee_from"]:
            top_longest_name.append(el)
print(f"Top 10 employees with the longest time in the company from highest to lower are: {top_longest_name[:10]}")