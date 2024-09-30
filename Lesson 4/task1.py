
# Нужно выполнить две задачи:
# 1. найти элементы, которые есть в каждом списке;
# 2. найти элементы из первого списка, которых нет во втором и третьем
# списках.
# Каждую задачу нужно выполнить двумя способами:
# 1. без использования множеств;
# 2. с использованием множеств.

# %%
array_1 = [1, 5, 10, 20, 40, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# 1. найти элементы, которые есть в каждом списке (без множеств);
# %%
for arr in [array_1, array_2, array_3]:
    print(arr)

el = 80
a = (el in arr for arr in [array_1, array_2, array_3])
for v in a:
    print(v)

100 in (arr for arr in [array_1, array_2, array_3])
# %%


el = 20
# el in array for array in [array_1, array_2, array_3]
# %%

elements = []
all = array_1 + array_2 + array_3


for arra in [array_1, array_2, array_3]:
    print(arra)
# ss = 1 in array for array in [array_1, array_2, array_3]

# for item in all:
#     if item not in elements:  # только для элементов которые мы еще не нашли
#         if all([item in array_1, item in array_2, item in array_3]):
#             elements.append(item)

# print(3 in [1, 2])

print(elements)

# %%
