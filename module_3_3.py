def print_params(a = 1, b = '', c = True):
    print(a, b, c)
    return
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
values_list = [99, "string", False]
values_dict = { 'a': "pop", 'b': 15, 'c': 9.9}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ["urban", True]
print_params(*values_list_2, 42)