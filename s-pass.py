import time
import base64
import string
from random import *

characters = string.ascii_letters + string.punctuation  + string.digits

password =  "".join(choice(characters) for x in range(randint(16, 16)))

print("s-pass is a program that creates strong passwords and then encrypts the password and saves it to a file. To see the encrypted password, execute the decrypt.py file and paste the password in the txt file into the incoming question.")

time.sleep(1)

for_what = input("\n\nPassword for what?\nEx: Gmail\n\ns-pass >>> ")

time.sleep(1)

print(f"\n{for_what} password is {password}")

file_message = f"{for_what} password is {password}"

message = file_message
message_bytes = message.encode('ascii')
base32_bytes = base64.b32encode(message_bytes)

base85_bytes = base64.b85encode(base32_bytes)

encoded_message = base85_bytes.decode('ascii')


file = open(f"{for_what}-password.txt", "w")

file.write(encoded_message)

file.close()

time.sleep(1)

print(f"\n\nEncrypted password saved {for_what}-password.txt successfully!")
