import base64
import time

crypted_message = input("\n\nEnter crypted message: ")

crypted_message = crypted_message[9:-13]

crypted_message = crypted_message[3] + crypted_message[1:3] + crypted_message[0] + crypted_message[4:]

base85_bytes = crypted_message.encode('ascii')

base32_bytes = base64.b85decode(base85_bytes)

message_bytes = base64.b32decode(base32_bytes)

message = message_bytes.decode('ascii')

time.sleep(1)

print(f"\n\n{message}\n \n")
