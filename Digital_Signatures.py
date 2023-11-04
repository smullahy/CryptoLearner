from Computation import *


def signature_key_creation(prime_1, prime_2):
    """
    Creates a signing key using the RSA Digital Signatures crypto-system
    :param prime_1: a prime number
    :param prime_2: a prime number not equal to prime_1
    :return: public key (pub_mod, verification_key), and private signing key signing_key in form (pub_mod, verification_key), signing_key
    """

    # Calculate pub_mod = prime_1 * prime_2
    pub_mod = np.multiply(prime_1, prime_2)

    # Calculate the euler totient value of pub_mod
    phi_pub_mod = euler_totient(prime_1, prime_2)

    # Find verification_key such that gcd(v, euler_totient(n)) = 1
    verification_key = 2
    while np.gcd(verification_key, phi_pub_mod) != 1:
        verification_key += 1

    # Calculate signing key
    signing_key = multiplicative_inverse(verification_key, phi_pub_mod)

    # Publish (pub_mod, verification_key) and have value of signing_key to use in later encryption
    return (pub_mod, verification_key), signing_key


def sign_message(message, pub_mod, signing_key):
    """
    Signs a message using the RSA digital signatures crypto-system
    :param message: message to sign
    :param pub_mod: from public key (pub_mod, verification_key)
    :param signing_key: from private key signing_key
    :return: signed message
    """
    return square_multiply(message, signing_key, pub_mod)


def is_valid_signature(message, signed_message, verification_key, pub_mod):
    """
    Checks if the signature provided is a valid signature
    :param message: unsigned message
    :param signed_message: signed message
    :param verification_key: from public key (pub_mod, verification_key)
    :param pub_mod: from public key (pub_mod, verification_key)
    :return: Boolean representing validity of key
    """
    if square_multiply(signed_message, verification_key, pub_mod) == message:
        return True
    else:
        return False
