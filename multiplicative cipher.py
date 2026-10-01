from math import gcd

def modular_inverse(key):
    for i in range(1, 26):
        if (key * i) % 26 == 1:
            return i
    return None


letter = input("Enter a single plaintext letter: ").upper()
key = int(input("Enter the key: "))

if len(letter) != 1 or not letter.isalpha():
    print("Invalid input! Please enter a single alphabetic letter.")

elif gcd(key, 26) != 1:
    print("Invalid key!")
    print("gcd(", key, ", 26 ) =", gcd(key, 26))
    print("Modular inverse does not exist.")

else:
    inverse = modular_inverse(key)

    print("\ngcd(", key, ", 26 ) = 1")
    print("Modular inverse of", key, "is", inverse)

    plaintext_value = ord(letter) - ord('A')

    encrypted_value = (plaintext_value * key) % 26
    encrypted_letter = chr(encrypted_value + ord('A'))

    decrypted_value = (encrypted_value * inverse) % 26
    decrypted_letter = chr(decrypted_value + ord('A'))

    print("\nPlaintext:", letter)
    print("Plaintext numeric value:", plaintext_value)

    print("\nEncrypted value:", encrypted_value)
    print("Ciphertext:", encrypted_letter)

    print("\nDecrypted value:", decrypted_value)
    print("Decrypted letter:", decrypted_letter)