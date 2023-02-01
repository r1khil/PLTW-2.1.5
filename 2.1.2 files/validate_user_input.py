#   a212_rsa_encrypt.py
import rsa as rsa

#creates input
key = input("Enter the Encryption Key: " )

# if not a digit, then it will ask for input again 
while not key.isdigit():
  print("That was not a number, please try again.")
  key = input("Enter the Encryption Key: " )

#if it is digit, it will change assign the value
key = int(key)

mod_value = input("Enter the Modulus: " )

while not mod_value.isdigit():
  print("That was not a number, please try again.")
  mod_value = input("Enter the Modulus: " )

mod_value = int(mod_value)

plaintext = input("Enter a message to encrypt: ")


encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
print("Encrypted Message:", encrypted_msg)

# .isalpha() checks if something uses alphanumeric charcters (a-z, A-Z)