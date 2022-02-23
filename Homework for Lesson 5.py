#ex1

numbers_list = []
dict1 = {}

times = int(input("How many numbers? "))

for i in range(times):
    user_number = float(input("Gimme number"))
    numbers_list.append(user_number)
for el in numbers_list:
    z = numbers_list.count(el)
    dict1[el] = z
for number, nr_of_input in dict1.items():
    print(f"Number {number} was used {nr_of_input} times")

#Ex2
my_dict = {
    "brand":"Audi",
    "Year":1991,
    "Price":2000,
    "Currency":"EUR"
}

price = my_dict.pop("Currency")
print(my_dict)

#Ex3

even = []
impar = []
for w in range(5):
    k = int(input("Number please"))
    if not k % 2:
        even.append(k)
    else:
        impar.append(k)
print(even)
print(impar)

#Ex4

my_dict = dict()
for a in range(5):
    key = input("key? ")
    val = input("Value? ")
    my_dict[key] = val
print(my_dict)

