if __name__ == "__main__":
    pass
#Задание 6#
import string
input_file = 'text.txt' 
output_file = 'newtext.txt' 
with open(input_file, 'r', encoding='utf-8') as f:
    text = f.read()
punctuation_chars = [ch for ch in text if ch in string.punctuation]
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(''.join(punctuation_chars))
