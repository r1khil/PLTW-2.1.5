#   a212_rsa_encrypt.py
import rsa as rsa

key = input("Enter the Encryption Key: " )

if key.isdigit():
  mod_value = (input("Enter the Modulus: " ))
else:
  


plaintext = input("Enter a message to encrypt: ")
encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
print("Encrypted Message:", encrypted_msg)
