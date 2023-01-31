def get_pr():
    in_str = input('Введите примерчик  (используй операции +, -, /, *): ')
    return in_str

def output(orig_example, my_list):
    print(f'{" ".join(orig_example)} = {my_list[0]}')