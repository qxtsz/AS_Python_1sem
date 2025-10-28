#задание 6#
if __name__ == "__main__":
    pass
import random
a = [random.randint(1, 100) for i in range(5)]
c = [x for x in a if x >= 10]
c.sort()
print(c)
