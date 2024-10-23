import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

df = pd.read_csv("execution_times.csv")
df.replace(0, 1e-6, inplace=True)
print(df)

plt.figure(figsize=(10, 6))

for column in df.columns[1:]:
    plt.plot(df["Кількість інтервалів"], df[column], label=column, marker='o')

plt.xlabel("Кількість інтервалів")
plt.ylabel("Час (секунди)")
plt.title("Час підрахунку інтегралу з різною кількістю потоків")
plt.legend()

plt.xscale('log')

x_formatter = FuncFormatter(lambda x, _: f'{x:.0e}')
plt.gca().xaxis.set_major_formatter(x_formatter)

y_formatter = FuncFormatter(lambda y, _: '{:g}'.format(y))
plt.gca().yaxis.set_major_formatter(y_formatter)

plt.grid(True)
plt.savefig('images/plot.png')
plt.show()
