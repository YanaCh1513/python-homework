#%%

import random

team_1 = [round (random.uniform (5,10),2) for _ in range(20)]
# Генерация второй команды аналогично первой
team_2 = [round (random.uniform (5,10),2) for _ in range(20)]
result = []
for i in range(20):
    if team_1[i] > team_2[i]:
        result.append(team_1[i])
    else:
        result.append(team_2[i])
result
result = [team_1[1] if team_1[i] > team_2[i] else team_2[i] 
    for i in range(20)]
print('первая команда:', team_1)
print('вторая команда:', team_2)
print('победитель:', result)
