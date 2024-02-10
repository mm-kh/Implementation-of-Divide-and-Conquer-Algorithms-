def strassen_matrix_multiply(A, B):

    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]

    n = len(A)
    m = n // 2

    A11 = [row[:m] for row in A[:m]]
    A12 = [row[m:] for row in A[:m]]
    A21 = [row[:m] for row in A[m:]]
    A22 = [row[m:] for row in A[m:]]

    B11 = [row[:m] for row in B[:m]]
    B12 = [row[m:] for row in B[:m]]
    B21 = [row[:m] for row in B[m:]]
    B22 = [row[m:] for row in B[m:]]

    P1 = strassen_matrix_multiply(A11, sub(B12, B22))
    P2 = strassen_matrix_multiply(add(A11, A12), B22)
    P3 = strassen_matrix_multiply(add(A21, A22), B11)
    P4 = strassen_matrix_multiply(A22, sub(B21, B11))
    P5 = strassen_matrix_multiply(add(A11, A22), add(B11, B22))
    P6 = strassen_matrix_multiply(sub(A12, A22), add(B21, B22))
    P7 = strassen_matrix_multiply(sub(A11, A21), add(B11, B12))

    C11 = add(sub(add(P5, P4), P2), P6)
    C12 = add(P1, P2)
    C21 = add(P3, P4)
    C22 = sub(sub(add(P5, P1), P3), P7)

    result = []
    for i in range(n):
        if i < m:
            result.append(C11[i] + C12[i])
        else:
            result.append(C21[i - m] + C22[i - m])

    return result

def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

def main():
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    B = [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]

    result = strassen_matrix_multiply(A, B)

    for row in result:
        print(row)

main()
