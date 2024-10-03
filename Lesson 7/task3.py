# %%
from collections import Counter


def checkPolyndrom(input):

    # Создаем счетчик частот символов в строке
    char_counts = Counter(input)

    # Проверяем количество символов с нечетным количеством вхождений
    non_pair_symbols_count = len(
        list(filter(lambda x: x % 2 != 0, char_counts.values())))

    return non_pair_symbols_count < 2
    # Условие для проверки возможности формирования палиндрома


res = checkPolyndrom('ssffd')
res
# %%
