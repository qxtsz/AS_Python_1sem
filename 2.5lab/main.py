if __name__ == "__main__":
    pass
#Задание 6#
A = int(input())
B = int(input())
C = int(input())
D = int(input())
def NOD(A, B):
    if A == 0:
        return B
    else:
        return NOD(B % A, A)
AB = NOD(A, B)
AC = NOD(A, C)
AD = NOD(A, D)
print(AB)
print(AC)
print(AD)
