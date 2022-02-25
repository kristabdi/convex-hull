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