# %%

# Задание 1. one hot
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это
# сделать без get_dummies?


# One Hot кодирование - это когда из разбираемого стобца
# создается N новых столбцов, каждый из которых показывает
# уникальное значение разбираемого столбца. Значения в
# колоноках 0\1.

import random
import pandas as pd

lst = ["robot"] * 10
lst += ["human"] * 10
random.shuffle(lst)

# создаем датафрейм с одной колонкой
data = pd.DataFrame({"whoAmI": lst})
# data.head()

# получаем уникальные значения кодируемого столбца
# чтобы создать на каждое значение свой столбец
unique_values = data["whoAmI"].unique()


one_hot = pd.DataFrame()
# one_hot.head()
# one_hot


for value in unique_values:
    # добавление колонки путем присвоение данных
    one_hot[value] = (data["whoAmI"] == value).astype(int)
    # добавление колонки через assign
    # one_hot.assign(value=(data["whoAmI"] == value).astype(int))

# one_hot = data['whoAmI'] == value
# data.head(4)
# one_hot

data = pd.concat([data, one_hot], axis=1)

data.head()
# %%
