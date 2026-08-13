import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pokemon.csv")

#tratamento de dados
df["weight_kg"] = df["weight"] / 10
df["height_m"] = df["height"] / 10

#conhecendo a base
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

# os mais pesados
print(df.sort_values("weight_kg", ascending=False)[["name", "weight_kg"]].head(10))

# media e mediana de peso
print(df["weight_kg"].mean())
print(df["weight_kg"].median())

# media e mediana de altura
print(df["height_m"].mean())
print(df["height_m"].median())

#organizando altura por nome
print(df.sort_values("height_m", ascending=False)[["name", "height_m"]].head(10))

df["weight_kg"].corr(df["height_m"])
print(df["weight_kg"].corr(df["height_m"]))

plt.scatter(df["height_m"], df["weight_kg"])

plt.xlabel("altura (m)")
plt.ylabel("peso (kg)")
plt.title("relacao entre altura e peso dos pokemon")
plt.show()