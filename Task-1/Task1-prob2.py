#symmetric if transpose of matrix= the original matrix
def Symmetric(mat, size):
    for i in range(size):
        for j in range(size):
            if (mat[i][j] != mat[j][i]):
                return False
    return True
 
 

mat = [[1, 2, 3], [2, 1, 4], [3, 4, 3]]
if (Symmetric(mat, 3)):
    print ("Yes")
else:
    print ("No")

