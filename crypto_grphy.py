from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

# Encrypt the msg
encrpyt_msg = f.encrypt(b"Hii I am mohit")
print(encrpyt_msg)

# decrypt the msg through key
decrypt_msg = f.decrypt(encrpyt_msg)
print(decrypt_msg)
