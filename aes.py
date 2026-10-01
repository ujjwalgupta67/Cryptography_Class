from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii


def get_valid_key():
    """AES-256 requires a 32-byte (256-bit) key."""
    while True:
        key = input("Enter a 32-character key (used as the AES-256 key): ")
        if len(key) == 32:
            return key.encode('utf-8')
        print(f"  Key must be exactly 32 characters long (you entered {len(key)}). Try again.\n")


def encrypt_aes(plaintext: str, key: bytes):
    iv = get_random_bytes(AES.block_size)          # random 16-byte IV for CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext, iv


def decrypt_aes(ciphertext: bytes, key: bytes, iv: bytes) -> str:
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_text, AES.block_size)
    return plaintext.decode('utf-8')


def main():
    print("=== AES-256 Encryption / Decryption ===\n")

    # 1. Get plaintext and key from the user
    plaintext = input("Enter the plain text you want to encrypt: ")
    key = get_valid_key()

    # 2. Encrypt
    ciphertext, iv = encrypt_aes(plaintext, key)
    print("\nOriginal Plain Text : ", plaintext)
    print("IV (hex)             : ", binascii.hexlify(iv).decode())
    print("Encrypted (hex)      : ", binascii.hexlify(ciphertext).decode())

    # 3. Decrypt (IV must be sent/stored along with the ciphertext to decrypt later)
    decrypted_text = decrypt_aes(ciphertext, key, iv)
    print("Decrypted Plain Text : ", decrypted_text)

    # 4. Verify
    if decrypted_text == plaintext:
        print("\n[OK] Decryption successful - matches original plaintext.")
    else:
        print("\n[FAIL] Decryption mismatch!")


if __name__ == "__main__":
    main()