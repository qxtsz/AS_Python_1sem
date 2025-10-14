if __name__ == "__main__":
    pass
#Задание 6 из ЕГЭ-профиль 2026 [https://math-ege.sdamgia.ru/problem?id=77369]
#Найдите корень уравнения (x-6)^2 = -24x
for x in range(-100, 100):
    if (x-6)**2 == -24*x:
        print(x)
