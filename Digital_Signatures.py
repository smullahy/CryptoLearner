from Computation import *


def signature_key_creation(p, q):
    """
    Creates a signing key using the RSA Digital Signatures crypto-system
    :param p: a prime number
    :param q: a prime number not equal to p
    :return: public key (n,v), and private signing key s in form (n,v), s
    """

    # Calculate n = pq
    n = np.multiply(p, q)

    # Calculate the euler totient value of n
    phi_n = euler_totient(p, q)

    # Find v such that gcd(v, euler_totient(n)) = 1
    v = 2
    while np.gcd(v, phi_n) != 1:
        v += 1

    # Calculate signing key
    s = multiplicative_inverse(v, phi_n)

    # Publish (n,v) and have value of s to use in later encryption
    return (n, v), s


def sign_message(m, n, s):
    """
    Signs a message using the RSA digital signatures crypto-system
    :param m: message to sign
    :param n: from public key (n, v)
    :param s: from private key s
    :return: signed message
    """
    return square_multiply(m, s, n)


def is_valid_signature(m, s, v, n):
    """
    Checks if the signature provided is a valid signature
    :param m: unsigned message
    :param s: signed message
    :param v: from public key (n, v)
    :param n: from public key (n, v)
    :return: Boolean representing validity of key
    """
    if square_multiply(s, v, n) == m:
        return True
    else:
        return False
