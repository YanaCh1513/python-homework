# %%
from collections import Counter

def checkPolyndrom(text):

    # Создаем счетчик частот символов в строке

    char_counts = Counter(text.lower())

    print(char_counts)

    # Проверяем количество символов с единственным вхождением
    one_symbols_count = len(
        list(filter(lambda x: x == 1, char_counts.values())))

    return one_symbols_count
    # Условие для проверки возможности формирования палиндрома


res = checkPolyndrom('ssFFsbffdv')
res
# %%
