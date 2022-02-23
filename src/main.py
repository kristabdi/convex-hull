import numpy as np
import pandas as pd
from sklearn import datasets

def isMember(arrToCheck, arr) :
    # Mengecek apakah arrToCheck adalah anggota dari list of array arr
    for i in range(len(arr)) :
        if ((arr[i][0] == arrToCheck[0]) and (arr[i][1] == arrToCheck[1])) :
            return True
    return False

def sortPoints(points) :
    # Sort based on absis (first column), jika absis sama compare ordinatnya (second column)
    points = sorted(points, key=lambda x: (x[0], x[1]))
    return points

def lineDistance(p1, pn, ptest) :
    # Mengembalikan jarak dari titik ptest ke garis yang dibentuk p1 dan pn
    val = (ptest[1] - p1[1]) * (pn[0] - p1[0]) - (pn[1] - p1[1]) * (ptest[0] - p1[0])
    return abs(val)

def whichSide(p1, pn, ptest) :
    # Titik (x3,y3) berada di sebelah kiri dari garis ((x1,y1),(x2,y2)) jika hasil determinan positif
    x1, y1 = p1[0], p1[1]
    x2, y2 = pn[0], pn[1]
    x3, y3 = ptest[0], ptest[1]
    val = (x1*y2 + x3*y1 + x2*y3) - (x3*y2 + x2*y1 + x1*y3)
    # Jika ptest di kiri garis yang dibentuk p1 dan pn akan mengembalikan 1
    # Jika ptest di kanan garis yang dibentuk p1 dan pn akan mengembalikan -1
    if (val > 0) :
        return 1
    elif (val < 0) :
        return -1
    return 0

def getIndices(edgeList, points) :
    # Fungsi yang mengembalikan list of array berisi indeks dimana edgeList berada di points
    res = np.zeros((len(edgeList),2), dtype=int)
    ind = 0
    for i in range(len(edgeList)) :
        foundX = False
        foundY = False
        for j in range(len(points)) :
            if (edgeList[i][0][0] == points[j][0] and edgeList[i][0][1] == points[j][1]) :
                res[ind][0] = j
                foundX = True
            if (edgeList[i][1][0] == points[j][0] and edgeList[i][1][1] == points[j][1]) :
                res[ind][1] = j
                foundY = True
        if (foundX and foundY) :
            ind+=1
    return res

def findHull(s, p, q, res, edgeList, side) :
    # Fungsi rekursif yang mencari titik terjauh dari garis yang dibentuk p dan q di sisi side (1 jika di kiri, -1 jika di kanan)
    if (len(s) == 0) :
        # Base case
        return
    # Inisialisasi variabel
    indexToAdd = None
    dist = 0.0

    for i in range(len(s)) :
        # Mencari titik terjauh di sisi "side" dengan mengiterasi dan memiliki variabel temporary untuk mencatat jarak terjauh
        val = lineDistance(p, q, s[i])
        if ((whichSide(p, q, s[i]) == side)  and (val > dist) and (not isMember(s[i], res))) :
            # Mencatat indeks dari titik yang memiliki jarak terjauh
            dist = val
            indexToAdd = i

    # Jika tidak ada titik terjauh
    if (indexToAdd is None) :
        # Base case untuk menambahkan titik yang terhubung paling luar
        res.append(p)
        res.append(q)
        pair = [p, q]
        # Memasukkan sisi ke edgeList, sisi terbentuk dari titik terjauh dan kedua ujung garis
        edgeList.append(pair)
        return

    # Titik terjauh ditemukan
    # Rekursif DnC untuk mencari titik terjauh dari garis yang dibentuk param ke 2 dan ke 3 dengan sisi(side) area yang konsisten
    findHull(s, s[indexToAdd], p, res, edgeList, -whichSide(s[indexToAdd], p, q))
    findHull(s, s[indexToAdd], q, res, edgeList, -whichSide(s[indexToAdd], q, p))

def ConvexHull(points)  :
    # Fungsi untuk mencari sisi yang koresponden di ConvexHull
    # Inisialisasi array
    res = [[0]*2]*2
    edgeList = [[0]*0]*0
    if (len(points) < 2) :
        # Cek minimal ada 2 titik di points
        return
    # Mencari leftmost dan rightmost titik di points (p1,pn), dan memasukkan p1 dan pn ke dalam res array 
    sortedArr = sortPoints(points)
    res[0], res[1] = sortedArr[0], sortedArr[len(sortedArr)-1]
    # Mencari titik yang membentuk convex hull dan memasukkan sisi yang terhubung ke array edgeList
    findHull(sortedArr, res[0], res[1], res, edgeList, 1)
    findHull(sortedArr, res[0], res[1], res, edgeList, -1)

    edges = getIndices(edgeList, points)
    return edges

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
    edges = ConvexHull(bucket)
    print(edges)
    print()
    # DEBUG
    break