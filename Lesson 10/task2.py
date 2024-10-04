# Задание 2. Анализ расходов по возрасту.
# Постройте линейный график, где по оси X будет отображаться возраст (age), а по оси
# Y — балл по расходам (spending_score). Этот график поможет визуализировать, как
# изменяются расходы в зависимости от возраста сотрудников. Проанализируйте тренды
# и выявите возможные закономерности

# %%

import pandas as pd  # тоже устанавливать пришлось
import seaborn as sns  # графики пришлось устанавливать
import matplotlib.pyplot as plt  # Этот модуль вроде был

df = pd.read_csv("data.csv")
print(df.columns)

# df.info() # all data non-null. Ok! Columns types age=int64, spending_score=int64

df.dtypes  # проверка типов колонок (чуть компактнее чем df.info())
df.head()

df.astype({"age": "int32", "spending_score": "int32"}).dtypes

# ради интереса преобразовал отображаемые колонки из int64 -> int32
df = df.astype({"age": "int32", "spending_score": "int32"})
df.dtypes

sns.lineplot(x="age", y="spending_score", data=df)
plt.title("Age vs Spending Score")
plt.xlabel("Age")
plt.ylabel("Spending Score")
plt.rcParams["axes.facecolor"] = "darkgray"
plt.rcParams["figure.facecolor"] = "gray"
plt.show()

# вывод: основные расходы приходятся на людей от 32-37 лет
