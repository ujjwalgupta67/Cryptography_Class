from math import gcd

def mod_inverse(a, m=26):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt(text, a, b):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            x = ord(ch) - ord('A')
            result += chr(((a * x + b) % 26) + ord('A'))
        else:
            result += ch
    return result

def decrypt(text, a, b):
    a_inv = mod_inverse(a)

    result = ""
    for ch in text.upper():
        if ch.isalpha():
            y = ord(ch) - ord('A')
            result += chr(((a_inv * (y - b)) % 26) + ord('A'))
        else:
            result += ch
    return result


text = input("Enter plaintext: ")
a = int(input("Enter multiplicative key (a): "))
b = int(input("Enter additive key (b): "))

if gcd(a, 26) != 1:
    print("Invalid multiplicative key!")
    print("gcd(a, 26) must be 1.")
else:
    inverse = mod_inverse(a)
    print("Modular inverse of", a, "=", inverse)

    cipher = encrypt(text, a, b)
    print("Encrypted text:", cipher)

    plain = decrypt(cipher, a, b)
    print("Decrypted text:", plain)