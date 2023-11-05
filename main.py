from Elgamel import *
from Digital_Signatures import *
from Diffie_Hellman import *
from Encoding_scheme import *
import sympy as sy

example_message = 1231

p = 13
b = 6

message = "Hello"
ascii_message = convert_to_ascii(message)

encrypted = []
for char in ascii_message:
    (_, __, pub_key), priv_key = elgamel_key_creation(p, b)
    cipher1, cipher2 = elgamel_encryption(p, b,pub_key, char)
    encrypted.append(((cipher1, cipher2), priv_key))

decrypted = []
for item in encrypted:
    elgamel_decryption(item[0][0], item[0][1],p,item[1])

print(decrypted)