import time
import base64
import string
from random import choice, randint

characters = string.ascii_letters + string.punctuation  + string.digits

password =  "".join(choice(characters) for x in range(16))

print("s-pass is a program that creates strong passwords and then encrypts the password and saves it to a file.\nTo see the encrypted password, execute the decrypt.py file and paste the password in the txt file into the incoming question.")

time.sleep(1)

for_what = input("\n\nPassword for what?\nEx: Gmail\n\ns-pass >>> ")

time.sleep(1)

print(f"\n{for_what} password is {password}")

file_message = f"{for_what} password is {password}\n\n"

message = file_message
message_bytes = message.encode('ascii')
base32_bytes = base64.b32encode(message_bytes)

base85_bytes = base64.b85encode(base32_bytes)

encoded_message = base85_bytes.decode('ascii')

encoded_message = encoded_message[3] + encoded_message[1:3] + encoded_message[0] + encoded_message[4:]

encoded_message = "D1?.F<&a3" + encoded_message + ".5F+t_/e^" + str(randint(13,17)) + str(randint(21,37))

file = open(f"{for_what}-password.txt", 'w')

file.write(encoded_message)

file.close()

time.sleep(1)

print(f"\n\nEncrypted password saved {for_what}-password.txt successfully!")

#Copyright© 2022 s-pass
#All rights of this software are protected by the GPL License.
