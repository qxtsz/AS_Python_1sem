if __name__ == "__main__":
    pass
#Задание 6#
with open('f', 'r', encoding='utf-8') as file:
    numbers = file.read().split()
numbers = list(map(int, numbers))
even_count = sum(1 for num in numbers if num % 2 == 0)
print(f"Количество чётных чисел: {even_count}")
