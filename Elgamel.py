import numpy as np
import numpy.random


def elgamel_encrypt(p, b):
    x = np.random.random_integers(1, p-2, 1)
    y = b^(x) % p
    return (p, b, y)
