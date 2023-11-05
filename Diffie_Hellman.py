from Computation import *


class DiffeHellman:
    def __init__(self, prime, prim_root):
        """
        Initialize the DiffieHellman class with a prime and a primitive root.
        :param prime: a prime number
        :param prim_root: a primitive root mod p
        """
        self.prime = prime
        self.prim_root = prim_root
        self.secret_int = None
        self.secret_key = None
        self.true_key = None

    def key_setup(self):
        """
        Sets up values for diffie hellman key exchange.
        :return: a tuple containing X^{secret_int}
        """
        self.secret_int = np.random.randint(1, self.prime, 1)[0]
        self.secret_key = square_multiply(self.prim_root, self.secret_int, self.prime)
        return self.secret_key

    def key_creation(self, base):
        """
        Calculates a shared diffie hellman key.
        :param base: base computed value
        :return: shared diffie hellman key
        """
        self.true_key = square_multiply(base, self.secret_int, self.prime)
        return self.true_key


def diffie_hellman_key_setup(prime, prim_root):
    """
    Sets up values for diffie hellman key exchange
    :param prime: a prime number
    :param prim_root: a primitive root mod p
    :return: a tuple containing X^{secret_int}, secret_int
    """

    # p is non-inclusive, hence why it's not p - 1
    secret_int = np.random.randint(1, prime, 1)[0]
    return square_multiply(prim_root, secret_int, prime), secret_int


def diffie_hellman_key_creation(base, secret_int, prime):
    """
    Calculates a shared diffie hellman key
    :param base: base computed value
    :param secret_int: secret random value
    :param prime: a prime number
    :return: shared diffie hellman key
    """
    return square_multiply(base, secret_int, prime)
