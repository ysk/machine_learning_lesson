import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mglearn
from IPython.display import display

X, y = mglearn.datasets.make_forge()
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.legend(["Class 0", "Class 1"], loc = 4) # 凡例
plt.xlabel("第1特徴量", fontname="MS Gothic")
plt.ylabel("第2特徴量", fontname="MS Gothic")


plt.show()

