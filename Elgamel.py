import numpy as np
from Computation import *


def elgamel_key_creation(p, b):
    """
    Creates a key using the ElGamel crypto-system.
    :param p: a prime number
    :param b: a primitive root mod p
    :return: Public key; (p, b, y), and private key x in form (p, b, y), x
    """

    # Generate random x in [1, p-2]
    x = np.random.random_integers(1, p-2, 1)

    # Calculate y = b^x mod p
    y = square_multiply(b, x, p)

    # Publish public key (p,b,y) and have value of x for use in later decryption
    return (p, b, y), x


def elgamel_encryption(p, b, y, m):
    """
    Encrypts a message using the ElGamel crypto-system
    :param p: from public key (p, b, y)
    :param b: from public key (p, b, y)
    :param y: from public key (p, b, y)
    :param m: message to encrypt
    :return: ciphertext C = (c_1,c_2)
    """

    # Pick random integer k (range arbitrarily restricted) as ephemeral key
    k = np.random.random_integers(1, p-1, 1)

    # Calculate c_1 = b^k mod p, and c_2 = my^k mod p
    c_1 = square_multiply(b, k, p)
    c_2 = square_multiply(np.multiply(m, y), k, p)

    # Publish cipher text
    return c_1, c_2


def elgamel_decryption(c_1, c_2, p, x):
    """
    Decrypts a message using the ElGamel crypto-system
    :param c_1: from ciphertext C = (c_1, c_2)
    :param c_2: from ciphertext C = (c_1, c_2)
    :param p: from public key (p, b, y)
    :param x: private key x. Assumed to be known for decryption
    :return:
    """

    # Decrypt message by calculating (c_2) * (c_1)^x inverse mod p
    # return np.mod(np.multiply(c_2, multiplicative_inverse(square_multiply(c_1,x,p))))
    return np.mod(np.multiply(c_2, multiplicative_inverse(np.power(c_1, x), p)), p)