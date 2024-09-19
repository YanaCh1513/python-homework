arr = [1, 1, [2, 2, (3, 3, 'SS')], 1, 1]
tup = ('ssss', 4)
print(type(tup) == tuple)
print(type(arr))


def my_sum(my_list):
    sum = 0
    for val in my_list:
        if isinstance(val, (list, tuple)):
            sum += my_sum(val)
        elif isinstance(val, int):
            sum += val
    return sum


result = my_sum(arr)

print(result)
