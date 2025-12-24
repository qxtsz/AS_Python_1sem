if __name__ == "__main__":
    pass
#Задание 6#
def remove_char(s, char):
    return s.replace(char, '')
def replace_char(s, old_char, new_char):
    return s.replace(old_char, new_char)
def count_char(s, char):
    return s.count(char)
import string_utils
text = input()
print(string_utils.remove_char(text, ','))
print(string_utils.replace_char(text, ' ', '_'))
print(string_utils.count_char(text, 'и'))
