#Задание 6#
if __name__ == "__main__":
    pass
s = input().strip()
n = int(input())
if not s:
    print("error")
else:
    f = s[:n] + s[n+1:]
    print(f)
