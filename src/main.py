import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

def sortPoints(points) :
    # sort based on absis (first column), if values are same then compare the ordinat (second column)
    points = sorted(points, key=lambda x: (x[0], x[1]))
    return points


def ConvexHull(points)  :
    res = [[0]*2]*2
    if (len(points) < 2) :
        # Check that there are at least 2 points in the input set S of points
        return
    # Mencari leftmost dan rightmost titik di points (p1,pn), dan memasukkan p1 dan pn ke dalam res array 
    sortedArr = sortPoints(points)
    res[0], res[1] = sortedArr[0], sortedArr[len(sortedArr)-1]
    # Mencari titik yang membentuk convex hull dan dimasukkan ke array res
    findHull(sortedArr, res[0], res[1], res, 1)
    findHull(sortedArr, res[0], res[1], res, -1)
    # DEBUG
    # print(res[0])
    # print()
    # print(res[1])
    # print()
    # print(sortedArr)
    return res


# ====================== MAIN ======================
iris = datasets.load_iris()
#data numpy array
data = iris['data']
#create a DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['Target'] = pd.DataFrame(iris.target)

for i in range(len(iris.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    # print(bucket)
    hull = ConvexHull(bucket)
    print(hull)
    print()
    # DEBUG
    break