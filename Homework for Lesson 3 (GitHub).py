#Ex:1

a = float(input('Insert width'))
b = float(input('Insert length'))
c = float(input('Insert height'))
print(a * b * c)

#Ex:2

n1 = float(input('Number 1'))
n2 = float(input('Number 2'))
highest = n1 if n1 > n2 else n2
print(highest)

# Longer version

n1 = float(input('Number 1'))
n2 = float(input('Number 2'))
if n1 > n2:
    print(n1)
else:
    print(n2)

#Ex:3

name = input('Name:')
age = int(input('Age:'))
gender = input('Gender (F/M):')
if age >= 18:
    if gender.upper() == 'F':
        print('Welcome Ms.', name)
    else:
        print('Welcome Mr.', name)
else:
    print('Yo', name)

# If-expression version

name = input('Name:')
age = int(input('Age:'))
gender = input('Gender (F/M):')
if age >= 18:
    text = 'Welcome Ms.' if gender.upper() == 'F' else 'Welcome Mr.'
    print(text, name)
else:
    print('Yo, ', name)

# If-elif version

name = input('Name:')
age = int(input('Age:'))
gender = input('Gender (F/M):')
if age >= 18 and gender.upper() == 'F':
    print('Welcome Ms.', name)
elif age >= 18 and gender.upper() == 'M':
    print('Welcome Mr.', name)
else:
    print('Yo, ', name)


#Ex:4

temp = int(input('Temperature'))
if temp < 0:
    print('Freezing weather')
elif 0 <= temp < 10:
    print('Very Cold weather')
elif 10 <= temp < 20:
    print('Cold weather')
elif 20 <= temp < 30:
    print('Normal in Temp')
elif 30 <= temp < 40:
    print("It's Hot")
elif temp >= 40:
    print("It's Very Hot")

# Or

if temp < 0:
    print('Freezing weather')
elif temp >= 0 and temp < 10:
    print('Very Cold weather')
elif temp >= 10 and temp < 20:
    print('Cold weather')
elif temp >= 20 and temp < 30:
    print('Normal in Temp')
elif temp >= 30 and temp < 40:
    print("It's Hot")
elif temp >= 40:
    print("It's Very Hot")

# Or

# This will work, so it's not wrong, but it doesn't mean it's right :D See below
if temp < 0:
    print('Freezing weather')
if 0 <= temp < 10:
    print('Very Cold weather')
if 10 <= temp < 20:
    print('Cold weather')
if 20 <= temp < 30:
    print('Normal in Temp')
if 30 <= temp < 40:
    print("It's Hot")
if temp >= 40:
    print("It's Very Hot")