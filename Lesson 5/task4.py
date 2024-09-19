nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def to_one_list(result_list, my_list):
    for val in my_list:
        if isinstance(val, (list, tuple)):
            to_one_list(result_list, val)
        elif isinstance(val, int):
            result_list.append(val)


new_list = []

to_one_list(new_list, nice_list)

print(new_list)

b = [4, 5]
a = [1, 2, 3]
a.extend(b)
print(a)
