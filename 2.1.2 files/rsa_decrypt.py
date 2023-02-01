#   a212_rsa_decrypt.py
import rsa as rsa

key = int(input("Enter the Decryption Key: " ))

while not key.isdigit():
  print("That was not a number, please try again.")
  key = input("Enter the Decryption Key: " )

key = int(key)

mod_value = int(input("Enter the Modulus: " ))

while not mod_value.isdigit():
  print("That was not a number, please try again.")
  mod_value = input("Enter the Modulus: " )

mod_value = int(mod_value)

encrypted_msg = input("What message would you like to decrypt (No brackets): ")

#break apart the list that is cut/copied over on ", "
msg = encrypted_msg.split(", ")
print (rsa.decrypt(key,mod_value , msg))
