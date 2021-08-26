import base64
import time

crypted_message = input("\n\nEnter crypted message: ")

base85_bytes = crypted_message.encode('ascii')

base32_bytes = base64.b85decode(base85_bytes)

message_bytes = base64.b32decode(base32_bytes)

message = message_bytes.decode('ascii')

time.sleep(1)

print(f"\n\n{message}\n\n")
