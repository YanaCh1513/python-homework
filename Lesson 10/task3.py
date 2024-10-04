# Задание 3. Взаимосвязь между зарплатой и бонусами
# Создайте точечный график, где по оси X будет отображаться зарплата (salary), а по
# оси Y — бонусы (bonus). Размер точек на графике должен быть пропорционален
# количеству лет в компании (years_at_company). Этот график позволит исследовать
# взаимосвязь между зарплатой и бонусами и оценить влияние стажа на размер
# бонусов.

# %%

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

df.head()

df.columns

# проверка на None (таких значений нет)
df[["salary", "bonus", "years_at_company"]].isna().sum()


# %%
# график рассеяния

# hue - ось Z отображает цветом кржуков
# sns.scatterplot(x="salary", y="bonus", hue="years_at_company", data=df)

# здесь ось Z отображаются размером кружков
sns.scatterplot(
    x="salary", y="bonus", sizes=(70, 300), size="years_at_company", data=df
)
# Настройка заголовка графика
plt.title("Salary vs Bonus with Years at Company")
# Настройка меток осей
plt.xlabel("Salary")
plt.ylabel("Bonus")
plt.rcParams["axes.facecolor"] = "darkgray"
plt.rcParams["figure.facecolor"] = "gray"

# Отображение графика
plt.show()

# %%
