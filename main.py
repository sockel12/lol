# import numpy

from math import inf
import numpy as np
import scipy.linalg
import math
# prety print numpy array
np.set_printoptions(precision=3, suppress=True)
limit = 1000

xx = 1
xy = 1
yx = 1
yy = 1



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
        xx = 1
        xy += 1
    if xy > limit:
        xy = 1
        yx += 1
    if yx > limit:
        yx = 1
        yy += 1
    if yy > limit:
        return False
    return True

def main():
    tol = 0.1
    while count():
        matrix = getNext2x2Matrix()
        a_c = round(np.linalg.cond(matrix, 1), 5)
        i_c = round(np.linalg.cond(matrix, np.inf), 5)
        a = np.linalg.det(matrix)
        if( abs(a) <= tol ):
            continue
        if( a_c == inf or i_c == inf ):
            continue
        if( math.floor(a_c) != math.floor(i_c) ):
            print("Det: {}".format(a))
            print(math.floor(a_c),  math.floor(i_c) )
            print(matrix)
            print("\n\n\n\n\n\n")

        # A = rowNorm(matrix)
        # A_1 = rowNorm(inv)
        # B = colNorm(matrix)
        # B_1 = colNorm(inv)
        # if(A * A_1 != B * B_1):

if __name__ == "__main__":
    main()