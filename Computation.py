import numpy as np


def square_multiply(base, power, modulus):
    """
    Computes powers mod numbers
    :param base: base number
    :param power: the power the base is taken to
    :param modulus: the number used as mod
    :return: an integer representing the answer to a base^{power} mod 'modulus'
    """

    bits = __convert_bits(power)

    answer = base
    for bit in bits[1:]:
        if bit == '1':
            answer = np.mod(np.multiply(np.power(answer, 2), base), modulus)
            print(answer)
        elif bit == '0':
            answer = np.mod(np.power(answer, 2), modulus)
    return answer


def __convert_bits(power):
    """
    Converts a power to binary
    :param power: int to change to bits
    :return: binary string
    """
    return bin(power)[2:]


def euclidean_algorithm(value1, value2):
    """

    :param value1:
    :param value2:
    :return:
    """

    if value1 >= value2:
        start_value = value1
    else:
        start_value = value2
    pass




def __division_remainder(dividend, divisor):
    """
    Finds the amount of times the divisor is in the dividend and finds remainder
    :param dividend: int to divide
    :param divisor: int to divide by
    :return: tuple containing (divisor_amt, remainder)
    """

    divisor_amt = np.floor_divide(dividend, divisor)
    remainder = np.mod(dividend, divisor)
    return divisor_amt, remainder


def multiplicative_inverse(b, p):
    return pow(b, -1, p)


def euler_totient(p, q):
    return np.multiply(p - 1, q - 1)