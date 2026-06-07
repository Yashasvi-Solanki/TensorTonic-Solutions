import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Get the dimensions of the input matrix
    rows = len(A)
    cols = len(A[0])
    
    # Create a new array of shape (cols, rows) using np.zeros
    transposed = np.zeros((cols, rows))
    
    # Fill the transposed matrix using nested loops
    for i in range(rows):
        for j in range(cols):
            # Swap the row and column indices
            transposed[j, i] = A[i][j]
            
    return transposed
