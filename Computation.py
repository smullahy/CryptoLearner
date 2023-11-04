import numpy as np


def square_multiply(base, power, modulus):
    bits = __convert_bits(power)

    answer = base
    print(f"Answer: {answer}")
    for bit in bits[1:]:
        if bit == '1':
            answer = np.mod(np.multiply(np.power(answer, 2), base), modulus)
            print(answer)
        elif bit == '0':
            answer = np.mod(np.power(answer, 2), modulus)
    return answer


def __convert_bits(power):
    return bin(power)[2:]


def euclidean_algorithm(value1, value2):
    if value1 >= value2:
        start_value = value1
    else:
        start_value = value2

    np.floor_divide(start_value)


def __division_remainder(dividend, divisor):
    np.floor_divide()


def multiplicative_inverse(value1, value2, modulus):
    euclidean_algorithm(value1, value2) =


def euler_totient(p, q):
    return np.multiply(p - 1, q - 1)
