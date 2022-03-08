#Ex1.1:
from my_library.circle import circle
from my_library.rectangle import rectangle
from my_library.square import square

c1 = circle(5)
c2 = circle(8)
print(c1.circle_area())
print(c2.circle_area())
print(c1 == c2)
print(c1 > c2)
print(c1 < c2)
print(c1 >= c2)
print(c1 <= c2)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1.__mul_by__(3))
print(c2.__mul_by__(6))

r1 = rectangle(3, 5)
r2 = rectangle(6, 7)
print(r1.rectangle_area())
print(r2.rectangle_area())
print(r1 == r2)
print(r1 > r2)
print(r1 < r2)
print(r1 >= r2)
print(r1 <= r2)
print(r1 + r2)
print(r2 - r1)
print(r1 * r2)
print(r1.__mul_by__(3))
print(r2.__mul_by__(6))

s1 = square(3)
s2 = square(6)
print(s1.square_area())
print(s2.square_area())
print(s1 == s2)
print(s1 > s2)
print(s1 < s2)
print(s1 >= s2)
print(s1 <= s2)
print(s1 + s2)
print(s2 - s1)
print(s1 * s2)
print(s1.__mul_by__(3))
print(s2.__mul_by__(6))

#Ex1.2:
from my_library.circle import circle
from my_library.rectangle import rectangle
from my_library.square import square

class shape_service:
    default_inner_color = "white"
    default_outer_color = "black"

    def __init__(self, inner_color, outer_color):
        self.default_inner_color = inner_color
        self.default_outer_color = outer_color

    @staticmethod
    def create_default_circle(radius):
        return f"{circle(radius)} with Inner Color {shape_service.default_inner_color} and Outer Color {shape_service.default_outer_color}"

    @staticmethod
    def create_default_rectangle(width, length):
        return f"{rectangle(width, length)} with Inner Color {shape_service.default_inner_color} and Outer Color {shape_service.default_outer_color}"

    @staticmethod
    def create_default_square(side_length):
        return f"{square(side_length)} with Inner Color {shape_service.default_inner_color} and Outer Color {shape_service.default_outer_color}"

    @staticmethod
    def color_shapes(list_of_shapes:list, inner_color, border_color):
        for el in list_of_shapes:
            print(f"{el} with Inner Color {inner_color} and Border Color {border_color}.")

y = shape_service.create_default_circle(5)
print(y)
z = shape_service.color_shapes([circle(5), rectangle(2, 3), square(7)], "red", "green")
print(z)

#Ex2:
import json


def get_valut_from_MDL():
    valut = input("In what valut you want to convert to? EX: EUR, USD ")
    return valut

def get_MDL_from_valut():
    valutmdl = input("What valut you want to convert to MDL? Ex: EUR, USD ")
    return valutmdl

def MDL_get_quantity():
    quantity = input("What quantity of MDL? ")
    return quantity

def valut_get_quantity():
    quantity = input("What quantity of Valut? ")
    return quantity

def extract_information_from_file_dict(file_name):
    try:
        file_json_for_riding = open(file_name, "r")
        file_json_read = file_json_for_riding.read()
        list_from_file = json.loads(file_json_read)
    except Exception:
        list_from_file = {}
    return list_from_file

def get_valut_rate(valut):
    valuti = extract_information_from_file_dict("my_library/conversion_rates.json").get(valut)
    rate = valuti.get("rate")
    return rate

def MDL_amount(rate, quantity_mdl):
    amount = float(quantity_mdl) * float(rate)
    return "{:.2f}".format(amount)

def valut_amount(rate, quantity_valut):
    amount = float(quantity_valut) * (1 / float(rate))
    return "{:.2f}".format(amount)

def exchange():
    dict1 = dict()
    dict3 = dict()
    for el in extract_information_from_file_dict("my_library/conversion_rates.json"):
        valuti = extract_information_from_file_dict("my_library/conversion_rates.json").get(el)
        dict1[valuti.get("code")] = valuti.get("rate")
        dict3[valuti.get("code")] = 1 / float(valuti.get("rate"))
        dict2 = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])}
        dict4 = {k: v for k, v in sorted(dict3.items(), key=lambda item: item[1])}
    print(f"We can convert MDL to the following Currencies with the following Rates. Ex: 1 MDL = Currency {dict2}")
    print(f"We can also convert the following Currencies to MDL with the following Rates. Ex: 1 Currency = MDL {dict4}")
    print("Please choose one of the following:")
    print("To convert in Valut from MDL please input '1'")
    print("To convert in MDL from Valut please input '2' ")
    answer = input("What is your answer? ")
    if int(answer) == 1:
        result = MDL_amount(get_valut_rate(get_valut_from_MDL()), MDL_get_quantity())
        return result + "MDL"
    elif int(answer) == 2:
        result2 = valut_amount(get_valut_rate(get_MDL_from_valut()), valut_get_quantity())
        return result2 + "Currency"
    else:
        raise Exception("Please input a valud answer: '1' or '2'. ")

print(exchange())