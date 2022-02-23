result = 'Hello' * 2 #HelloHello
print(result)

cuvintul_1 = input("introduceti cuvintul ").lower()
print(cuvintul_1.count("a") + cuvintul_1.count("e") + cuvintul_1.count("i") + cuvintul_1.count("o") + cuvintul_1.count("u") + cuvintul_1.count("y"))

email = input("introduceti emailul ")
print(email[-10:] == "@gmail.com")