import numpy as np
from Computation import *


def elgamel_key_creation(p, b):
    x = np.random.random_integers(1, p-2, 1)
    y = square_multiply(b, x, p)
    return (p, b, y), x


def elgamel_encryption(p, b, y, m):
    k = np.random.random_integers(1, p-1, 1)
    c_1 = square_multiply(b, k, p)
    c_2 = square_multiply(np.multiply(m, y), k, p)
    return c_1, c_2


def elgamel_decryption(c_1, c_2, p, x):
    # return np.mod(np.multiply(c_2, multiplicative_inverse(square_multiply(c_1,x,p))))
    return np.mod(np.multiply(c_2, multiplicative_inverse(np.power(c_1,x), p)),p)