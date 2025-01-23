import base64

SECRET_KEY = "supersecretkey"

def decrypt_data(encrypted_data):
    encrypted = base64.b64decode(encrypted_data).decode()
    decrypted = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(encrypted, SECRET_KEY))
    return decrypted

encrypted_data = "YOUR_ENCRYPTED_DATA_HERE"
decrypted_data = decrypt_data(encrypted_data)
print(f"Decrypted Data: {decrypted_data}")