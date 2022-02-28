import numpy as np
from searchHull import *
from util import *

def myConvexHull(points)  :
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