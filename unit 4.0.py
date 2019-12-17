a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
c = int (input("Введите значение c: "))
max = 0
if a > b:
    max = a
else:
    max = b
if c > max:
    max = c
print(max)