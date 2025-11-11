#задание 6#
if __name__ == "__main__":
    pass
import random
def zxc(B):
    maxzxc = B.index(max(B))
    product = 1
    for x in B[maxzxc + 1:]:
        product *= x
    return product
q = 5
B = [random.randint(1, 100) for a in range(q)]
print(B)
print(zxc(B))
