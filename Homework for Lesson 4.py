#Ex1
lista_1 = ["Vanea", "Tolea", "Mariana"]
print(lista_1[0])
print(lista_1[2])
print(lista_1[1])
lista_1[1] = "Sasha"
print(lista_1[1])

#ex2

operatiunea = input("introdu operatiunea: +, -, /, * ")
numar_1 = input("introdu primul numr: ")
numar_2 = input("introdu al doilea numar: ")
if operatiunea == "+":
    rezultat = float(numar_1) + float(numar_2)
elif operatiunea == "-":
    rezultat = float(numar_1) - float(numar_2)
elif operatiunea == "/":
    rezultat = float(numar_1) / float(numar_2)
else:
    rezultat = float(numar_1) * float(numar_2)

print(f"{numar_1}{operatiunea}{numar_2} = {rezultat}")

#or

if operatiunea == "+":
    print(f"{numar_1}{operatiunea}{numar_2} = {float(numar_1) + float(numar_2)}")
elif operatiunea == "-":
    print(f"{numar_1}{operatiunea}{numar_2} = {float(numar_1) - float(numar_2)}")
elif operatiunea == "/":
    print(f"{numar_1}{operatiunea}{numar_2} = {float(numar_1) / float(numar_2)}")
else:
    print(f"{numar_1}{operatiunea}{numar_2} = {float(numar_1) * float(numar_2)}")

#Ex3

string_1 = "3"
string_2 = "+"
string_3 = "20"
print(f"{string_1}{string_2}{string_3}")