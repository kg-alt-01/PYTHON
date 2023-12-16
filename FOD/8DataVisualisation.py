#Perform Statistics and Data Visualisation in python.
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

iris = sns.load_dataset('iris')

X = iris.drop('species', axis=1)
y = iris['species']

summary_stats = X.describe()
print("Summary Statistics:")
print(summary_stats)

sns.set(style="ticks")
sns.pairplot(iris, hue="species")
plt.show()
