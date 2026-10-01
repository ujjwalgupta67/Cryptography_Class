import os
import base64

def generate_key(length):
    return os.urandom(length)

def apply_xor(data, key):
    return bytes(data[i] ^ key[i] for i in range(len(data)))

def encrypt(plaintext):
    data = plaintext.encode("utf-8")
    key = generate_key(len(data))

    encrypted = apply_xor(data, key)

    encrypted_text = base64.b64encode(encrypted).decode()
    key_text = base64.b64encode(key).decode()

    return encrypted_text, key_text

def decrypt(encrypted_text, key_text):
    encrypted = base64.b64decode(encrypted_text)
    key = base64.b64decode(key_text)

    decrypted = apply_xor(encrypted, key)

    return decrypted.decode("utf-8")


print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice: ")

if choice == "1":
    plaintext = input("Enter plaintext: ")

    encrypted, key = encrypt(plaintext)

    print("\nEncrypted text:")
    print(encrypted)

    print("\nCryptographic key:")
    print(key)

elif choice == "2":
    encrypted = input("Enter encrypted text: ")
    key = input("Enter cryptographic key: ")

    try:
        plaintext = decrypt(encrypted, key)
        print("\nOriginal plaintext:")
        print(plaintext)
    except:
        print("Invalid encrypted text or key.")

else:
    print("Invalid choice.")