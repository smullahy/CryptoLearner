import numpy as np
from Computation import *


def signature_key_creation(p, q):
    n = np.multiply(p, q)
    phi_n = euler_totient(p, q)
    v = 2
    while np.gcd(v, phi_n) != 1:
        v += 1
    s = multiplicative_inverse(v, phi_n)
    return (n, v), s


def sign_message(m, n, s):
    return square_multiply(m, s, n)


def verify_signature(m, s, v, n):
    if square_multiply(s, v, n) == m:
        return True
    else:
        return False
