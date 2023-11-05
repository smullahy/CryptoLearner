from Elgamal import *
from Digital_Signatures import *
from Diffie_Hellman import *
from Encoding_scheme import *
import sympy as sy


message = "Hello, I am Shane Mullahy, Computer Science aficionado."

ascii_list = []
for char in message:
    ascii_list.append(ord(char))
print(f"\nMessage in numeric form: {ascii_list}\n")

prime = generate_prime()
prim_root = generate_prim_root(prime)

big_x, x = diffie_hellman_key_setup(prime, prim_root)
big_y, y = diffie_hellman_key_setup(prime, prim_root)

true_key = square_multiply(big_x, y, prime)
true_key_alt = square_multiply(big_y, x, prime)

print("\nThe key has been generated correctly: " + str(true_key == true_key_alt))

prime, prim_root, pub_key = elgamal_key_creation(prime, prim_root, true_key)

ciphertext = []
for char in ascii_list:
    ciphertext.append(elgamal_encryption(prime, prim_root, pub_key, char))
print(f"\n\nEncrypted message: {ciphertext}\n")

(signature_mod, verification_key), signing_key = signature_key_creation(generate_prime(), generate_prime())
signature_message = np.random.randint(1, np.floor(signature_mod / 2))
signed_message = sign_message(signature_message, signature_mod, signing_key)
validity = is_valid_signature(signature_message, signed_message, verification_key, signature_mod)
print(f"\nThe signature is valid: {validity}\n")

decrypted_message = []
for char in ciphertext:
    decrypted_message.append(elgamal_decryption(char[0], char[1], prime, true_key))

print(f"\nDecrypted message: {decrypted_message}\n")

translation = ""
for int_char in ascii_list:
    translation += chr(int_char)

print(f"\nTranslated message: {translation}\n")
