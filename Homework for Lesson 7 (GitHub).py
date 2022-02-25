#Ex 1:
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
#print(check_palindrome("nurses run"))

#Ex 2:
def prime_check(a: int):
    z = list(range(a))
    q = []
    for el in z:
        if (int(a) / (int(el + 1))).is_integer():
            q.append(int(a) / int((el + 1)))
    print(q)
    if len(q) > 2:
        return f"{a} is NOT PRIME"
    else:
        return f"{a} is PRIME"
#print(prime_check(19))

#Ex 3:
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
#print(perfect_number(6))

#This function is NOT WORKING
def find_perfect_number():
    list = []
    while True:
        p = input("Number or \"end\" to stop")
        if p == "end":
            break
        else:
            number = int(p)
            if perfect_number(number):
                list.append(p)
    return list

#print(find_perfect_number())

#Ex4:
sentence = input("Input a sentence: ")
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punctuations = ""
only_punctuations = ""
for el in sentence:
    if el not in punctuations:
        no_punctuations = no_punctuations + el
    else:
        only_punctuations = only_punctuations + el
words_list = no_punctuations.split(" ")
print(f"All the words used in the text: {no_punctuations}")
print(f"All the punctuation marks used in the text: {only_punctuations}")
punctuations_list = list(only_punctuations)
dict = {}
punct_dict = {}
for rr in words_list:
    y = words_list.count(rr)
    dict[rr] = f"was used {y} times"
print(dict)
for key, value in dict.items():
         if max(dict.values()) == value:
             k = key
print(f'Most commonly used word was "{k}", {max(dict.values())}')
for gg in punctuations_list:
    u = punctuations_list.count(gg)
    punct_dict[gg] = f"was used {u} times"
print(punct_dict)
for keys, values in punct_dict.items():
         if max(punct_dict.values()) == values:
             b = keys
             print(f'Most commonly used word was "{b}", {max(punct_dict.values())}')