

#ExA:
any_number = input("Write any number ")
how_many_times = input("How many times? ")
a = []
while any_number:
    if not any_number.isnumeric():
        print("Im done")
        break
    elif int(any_number) % 2 == 0:
        a.append(any_number)
        print(f"{any_number} is even")
        if len(a) == int(how_many_times):
            break
    else:
        a.append(any_number)
        print(f"{any_number} is odd")
        if len(a) == int(how_many_times):
            break

#ExB:
from datetime import datetime, timedelta
date = input("Write a date, \"Ex: 21-02-2022\" ")
date_split = date.split("-")
comp_date = datetime(int(date_split[2]), int(date_split[1]), int(date_split[0]))
one_day = timedelta(days=1)
next_day = comp_date + one_day
print(next_day)

#Ex1:
list = input("Input a list ")
no_coma_list = list.strip(",")
end_list = no_coma_list.split(" ")
tuple_end_list = tuple(end_list)
print(f"List : {end_list}")
print(f"Tuple : {tuple_end_list}")

#Ex2:
import calendar
from datetime import datetime, timedelta
date = input("Write a date, \"Ex: 02-2022\" ")
date_split = date.split("-")
y = int(date_split[1])
m = int(date_split[0])
print(y)
print(m)
print(calendar.month(y, m))
#or
year = int(input("year: "))
month = int(input("month: "))
print(calendar.month(year, month))

#Ex3:
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
final_list = []
for el1 in color_list_1:
    final_list.append(el1)
for el2 in color_list_2:
    final_list.append(el2)
set_final_list = set(final_list)
result = set_final_list - color_list_2
print(result)

#Ex4
seconds = int(input("Input time in seconds: "))
days = int(seconds / 86400)
hours = int(int(seconds % 86400) / 3600)
minutes = int(int((seconds % 86400) % 3600) / 60)
seconds = int(int((seconds % 86400) % 3600) % 60)
print(f"{days} days {hours} hours {minutes} minutes {seconds} seconds")

#Ex:5
celsius = int(input("Input Celsius: "))
fahrenheit = 9.0 / 5.0 * celsius + 32
print(fahrenheit)
fahrenheit1 = int(input("Input Fahrenheit: "))
celsius1 = (fahrenheit1 - 32) * 5.0 / 9.0
print(celsius1)

#Ex6:
dict1 = {}
number = int(input("Input the number: "))
for el in range(number):
    dict1[el + 1] = (el + 1) ** 2
print(dict1)

#Ex8:
number = int(input("Put the number: "))
list = range(number)
list1 = []
list2 = []
list3 = []
for el1 in list:
    for el2 in list:
        for el3 in list:
            if el1 + el2 + el3 == len(list):
                if not el1 == 0:
                    if not el2 == 0:
                        if not el3 == 0:
                            list1.append(el1)
                            list2.append(el2)
                            list3.append(el3)
print(list1)
print(list2)
print(list3)

#Ex9:
n = True
list = []
while n:
    n = int(input("Input: "))
    list.append(n)
    s = sum(list)
    v = s / int(len(list))
    if n == 0:
        print(f"You've entered a total of {int(len(list) - 1)} numbers")
        print(f"Sum is {s}")
        print(f"Average is {s / (int(len(list) - 1))}")
        break
    else:
        print(f"Sum is {s}")
        print(f"Average is {v}")

