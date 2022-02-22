import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from scipy.spatial import ConvexHull


iris = datasets.load_iris()
#data numpy array
data = iris['data']
#create a DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['Target'] = pd.DataFrame(iris.target)

# MAIN
for i in range(len(iris.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    hull = ConvexHull(bucket)
    # DEBUG
    break

for simplex in hull.simplices:
    print(bucket[simplex, 0], bucket[simplex, 1])