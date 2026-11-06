import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # a = np.array(a)
    # m = a.shape[0]
    # n = a.shape[1]

    # temp = [[0] * m for _ in range(n)]

    # for i in range(m):
    #     for j in range(n):
    #         temp[j][i] = a[i][j]
    
    # return temp

    a = np.transpose(a)
    return a




