#Задание 6#
if __name__ == "__main__":
    pass
def zxc(s, n):
    return s[n-1::n]

def qwe(s, n):
    result = ''
    for i in range(len(s)):
        if (i + 1) % n != 0:
            result += s[i]
    return result
s = input()
n = int(input("n-ый символ "))
print(qwe(s, n))
