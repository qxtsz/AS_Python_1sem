#Задание 6#
if __name__ == "__main__":
    pass
import math
n = int(input())
k = math.cos(n)
f = 0
for i in range(1, n + 1):
    f += (1 ** (n + 1)) * k
print(f)
