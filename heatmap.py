import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

number = np.random.rand(12,15)
print(number)

sns.heatmap(number , annot=True)
plt.show()


data = pd.read_csv("flights.csv")

flights = data.pivot("month" , "year" , "passengers")
sns.heatmap(flights  , annot=True , fmt='d')
plt.show()