from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii


def get_valid_key():
    while True:
        key = input("Enter an 8-character key: ")

        if len(key) == 8:
            return key.encode("utf-8")

        print("Key must be exactly 8 characters long. Try again.\n")


def encrypt_des(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)

    padded_text = pad(plaintext.encode("utf-8"), DES.block_size)
    ciphertext = cipher.encrypt(padded_text)

    return ciphertext


def decrypt_des(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)

    padded_text = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_text, DES.block_size)

    return plaintext.decode("utf-8")


def main():
    print("=== DES Encryption / Decryption ===\n")

    plaintext = input("Enter the plain text you want to encrypt: ")
    key = get_valid_key()

    # Encryption
    ciphertext = encrypt_des(plaintext, key)

    print("\nOriginal Plain Text :", plaintext)
    print("Encrypted (hex)     :", binascii.hexlify(ciphertext).decode())

    # Decryption
    decrypted_text = decrypt_des(ciphertext, key)

    print("Decrypted Plain Text:", decrypted_text)

    # Verification
    if decrypted_text == plaintext:
        print("\n[OK] Decryption successful - matches original plaintext.")
    else:
        print("\n[FAIL] Decryption mismatch!")


if __name__ == "__main__":
    main()