import numpy as np
from util import *

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