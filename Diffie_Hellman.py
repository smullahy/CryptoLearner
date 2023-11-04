from Computation import *


def diffie_hellman_key_setup(p, b):
    """
    Sets up values for diffie hellman key exchange
    :param p: a prime number
    :param b: a primitive root mod p
    :return: a tuple containing X^{secret_int}, secret_int
    """

    # p is non-inclusive, hence why it's not p - 1
    secret_int = np.random.randint(1, p, 1)[0]
    return square_multiply(b, secret_int, p), secret_int


def diffie_hellman_key_creation(base, secret_int):
    """
    Calculates a shared diffie hellman key
    :param base: base computed value
    :param secret_int: secret random value
    :return: shared diffie hellman key
    """

    return np.power(base, secret_int)
