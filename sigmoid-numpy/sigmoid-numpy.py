import numpy as np

def sigmoid(x):
    """
    Compute the sigmoid of x.
    x can be a scalar, a list, or a NumPy array.
    """
    # Convert input to a float array to handle scalars, lists, and arrays uniformly
    x = np.asarray(x, dtype=float)
    
    # Apply the vectorized sigmoid formula
    return 1 / (1 + np.exp(-x))