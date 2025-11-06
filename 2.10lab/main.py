#Задание 6#
if __name__ == "__main__":
    pass
from logging import raiseExceptions

n = int(input("Число: "))
f = int(input("Степень: "))
#A#
if f < 0:
    raiseExceptions(ValueError("Отрицательная степень"))
else:
    k = n ** f
    print(k)
#Б#
if n % 2 == 1:
    print("Число не является четным")
else:
    print("Число является четным")
#B#
h = int(input("Число: "))
j = int(input("Степень: "))
assert j > 0, "Отрицательная степень"
g = h ** j
print(g)
