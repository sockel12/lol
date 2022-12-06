# import numpy
from math import inf
import numpy as np
import scipy.linalg

limit = 1000

xx = 0
xy = 0
yx = 0
yy = 0



def getNext2x2Matrix():
    return np.array([[xx, xy], [yx, yy]])

def calcInv(matrix):
    # if singular, return None
    if np.linalg.det(matrix) == 0:
        return None
    return np.linalg.inv(matrix)


def count():
    global xx, xy, yx, yy
    xx += 1
    if xx > limit:
        xx = 0
        xy += 1
    if xy > limit:
        xy = 0
        yx += 1
    if yx > limit:
        yx = 0
        yy += 1
    if yy > limit:
        return False
    return True

def rowNorm(matrix):
    return scipy.linalg.norm(matrix, ord=1)

def colNorm(matrix):
    return scipy.linalg.norm(matrix, ord=np.inf)

def main():
    while count():
        matrix = getNext2x2Matrix()
        inv = calcInv(matrix)
        if inv is None:
            continue
        A = rowNorm(matrix)
        A_1 = rowNorm(inv)
        B = colNorm(matrix)
        B_1 = colNorm(inv)
        if(A * A_1 == B * B_1):
            print(matrix)
            print(inv)

if __name__ == "__main__":
    main()
    # matrix = np.array([[1, 2], [3, 4]])
    # inv = np.linalg.inv(matrix)
    # print(inv)
    # print(rowNorm(matrix))
    # print(colNorm(matrix))