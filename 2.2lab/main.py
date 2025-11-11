if __name__ == "__main__":
    pass
import math
p = 0
def TringleP(a, h):
    b = math.sqrt(a // 2)**2 + h**2
    p = 2 * math.sqrt(a**2 - h**2) + 2*a
    return p
