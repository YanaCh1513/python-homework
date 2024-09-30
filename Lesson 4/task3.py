synonims_dict=dict()
pairs_count = int (input('введите количество пар слов: '))
for i_pair in range (pairs_count):
    first_word, second_word = input(f'{i_pair + 1} пара:').lower().split(' - ')
    synonims_dict[first_word] = second_word
    synonims_dict[second_word] = first_word
while True:
    word = input ('введи слово: ').lower()
    if word in synonims_dict:
        print ('синоним: ', synonims_dict[word].capitalize())
        break
    else:
        print ('такого слова нет в словаре')