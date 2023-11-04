from Computation import *


def elgamel_key_creation(prime, prim_root):
    """
    Creates a key using the ElGamel crypto-system.
    :param prime: a prime number
    :param prim_root: a primitive root mod prime
    :return: Public key; (prime, prim_root, pub_key), and private key priv_key in form (prime, prim_root, pub_key), priv_key
    """

    # Generate random priv_key in [1, prime - 2]
    priv_key = np.random.randint(1, prime - 1, 1)[0]

    # Calculate pub_key = prim_root ^ priv_key mod prime
    pub_key = square_multiply(prim_root, priv_key, prime)

    # Publish public key (prime, prim_root, pub_key) and have value of priv_key for use in later decryption
    return (prime, prim_root, pub_key), priv_key


def elgamel_encryption(prime, prim_root, pub_key, message):
    """
    Encrypts a message using the ElGamel crypto-system
    :param prime: from public key (prime, prim_root, pub_key)
    :param prim_root: from public key (prime, prim_root, pub_key)
    :param pub_key: from public key (prime, prim_root, pub_key)
    :param message: message to encrypt
    :return: ciphertext = (cipher1, cipher2)
    """

    # Pick random integer ephemeral_key (range arbitrarily restricted) as ephemeral key
    ephemeral_key = np.random.randint(1, prime, 1)[0]

    # Calculate cipher1 = prim_root ^ ephemeral_key mod prime, and cipher2 = message * pub_key ^ ephermeral_key mod prime
    cipher1 = square_multiply(prim_root, ephemeral_key, prime)
    cipher2 = np.mod(np.multiply(message, square_multiply(pub_key, ephemeral_key, prime)),prime)

    # Publish cipher text
    return cipher1, cipher2


def elgamel_decryption(cipher1, cipher2, prime, priv_key):
    """
    Decrypts a message using the ElGamel crypto-system
    :param cipher1: from ciphertext = (cipher1, cipher2)
    :param cipher2: from ciphertext = (cipher1, cipher2)
    :param prime: from public key (prime, prim_root, pub_key)
    :param priv_key: private key, assumed to be known for decryption
    :return: decrypted original message
    """

    # Decrypt message by calculating (cipher2) * (cipher1) ^ priv_key inverse mod prime
    # return np.mod(np.multiply(cipher2, multiplicative_inverse(square_multiply(cipher1, priv_key, prime), prime)))
    return np.mod(np.multiply(cipher2, multiplicative_inverse(np.power(cipher1, priv_key), prime)), prime)