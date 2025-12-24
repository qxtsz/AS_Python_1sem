if __name__ == "__main__":
    pass
#Задание 6#
def create_square_dict(n):
    square_dict = {i: i**2 for i in range(1, n+1)}
    print(f'Словарь квадратов чисел от 1 до {n}:', square_dict)
    return square_dict


def merge_values_from_dicts(dict_list):
    merged_values = [value for d in dict_list for value in d.values()]
    print('Объединённый список значений:', merged_values)
    return merged_values

def remove_empty_elements(input_dict):
    filtered_dict = {k: v for k, v in input_dict.items() if v not in ('', None)}
    print('Словарь после удаления пустых элементов:', filtered_dict)
    return filtered_dict


n = int(input())
create_square_dict(n)

dict_list = [{1:2}, {3:4}, {5:6}]
merge_values_from_dicts(dict_list)

sample_dict = {1:'', 2:'abc', 3:None}
remove_empty_elements(sample_dict)
