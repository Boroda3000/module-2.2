x = input('Введите три числа разделенных пробелом:').split()
first = int(float(x[0]))
second = int(float(x[1]))
third = int(float(x[2]))
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)