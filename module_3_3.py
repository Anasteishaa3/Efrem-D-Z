def  print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [25, None, 'Boris_Brejcha']
values_dict = {'a':52.52, 'b':"Казантип", 'c':False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Ekaterinberg_', 38]

print_params(values_list_2, 67)