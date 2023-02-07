from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("data/Cleaned-Data.csv")
data.dropna(inplace=True)
print(data)



