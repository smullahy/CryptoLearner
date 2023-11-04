import numpy as np


def square_multiply(base, power, modulus):
    bits = convert_bits(power)

    answer = base
    print(f"Answer: {answer}")
    for bit in bits[1:]:
        if bit == '1':
            answer = np.mod(np.multiply(np.power(answer, 2), base), modulus)
            print(answer)
        elif bit == '0':
            answer = np.mod(np.power(answer, 2), modulus)
    return answer


def convert_bits(power):
    return bin(power)[2:]


def multiplicitve_inverse()