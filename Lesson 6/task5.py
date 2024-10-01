# %%

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabetLenght = len(alphabet)

input = "это питон."
shift = 3

result = ""  # должен быть = 'ахс тлхср.'

for i, ch in enumerate(input):
    if ch in alphabet:
        index = alphabet.index(ch)
        if index + shift + 1 > alphabetLenght:
            result += alphabet[index + shift - alphabetLenght]
        else:
            result += alphabet[index + shift]
    else:
        result += ch

result

# %%
3 % 2
