#задание 6#
if __name__ == "__main__":
    pass
import math
import random
q = 5
B = [random.randint(1, 100) for a in range(q)]
z = max(B)
print(B)
index = B.index(z)
f = math.prod(B)
if index == 0:
    print(f//z)
if index == 1:
    print(f // z // B[0])
if index == 2:
    print(f // z // B[0] // B[1])
if index == 3:
    print(f // z // B[0] // B[1] // B[2])
if index == 4:
    print(f // z // B[0] // B[1] // B[2] // B[3])
