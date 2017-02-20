def printDiag(M, n, m):
    i, j = n - 1, 0
    while j < m:
        k, l = i, j
        res = ""
        while k < n and l < m:
            res += str(M[k][l])+ " "
            l += 1
            k += 1
        if i > 0:
            i -= 1
        else:
            j += 1
        print(res)
# Test
A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9,10,11,12]]

printDiag(A, 3, 5)