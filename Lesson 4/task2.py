def is_poly(string):
    char_dict=dict()
    for n_elem in string:
        char_dict[n_elem] = char_dict.get(n_elem, 0) +1
    odd_variable =0
    for i_value in char_dict.values():
        if i_value % 2 != 0:
           odd_variable += 1
    return odd_variable >=1

input_string = input("введи строку: ")
if is_poly(input_string):
    print("есть полиндром")
else:
    print ("нет полиндрома")

