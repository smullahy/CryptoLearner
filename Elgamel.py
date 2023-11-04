import numpy as np
from Computation import *


def elgamel_key_creation(p, b):
    x = np.random.random_integers(1, p-2, 1)
    y = b^(x) % p
    return (p, b, y) , x


def elgamel_encryption(p,b,y, m):
    k = np.random.random_integers(1, p-1, 1)
    c_1 = np.mod(np.power(b,k), p)
    c_2 = np.mod(np.multiply(m, np.power(y, k)), p)
    return (c_1, c_2)


def elgamel_decryption(c_1, c_2, p, x):
    return np.mod(np.multiply(c_2, Computation.multiplicative_inverse(np.power(c_1,x), p)),p)