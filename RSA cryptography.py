import math


def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3

    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


def modular_inverse(e, phi):
    gcd, x, y = extended_gcd(e, phi)

    if gcd != 1:
        return None

    return x % phi


def generate_keys(p, q):
    n = p * q

    phi = (p - 1) * (q - 1)

    e = 65537

    if math.gcd(e, phi) != 1:
        e = 3

        while math.gcd(e, phi) != 1:
            e += 2

    d = modular_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


def encrypt(plaintext, public_key):
    e, n = public_key

    encrypted = []

    for char in plaintext:
        number = ord(char)

        if number >= n:
            raise ValueError(
                "Prime numbers are too small for this plaintext."
            )

        encrypted_char = pow(number, e, n)

        encrypted.append(encrypted_char)

    return encrypted


def decrypt(ciphertext, private_key):
    d, n = private_key

    decrypted = ""

    for number in ciphertext:
        decrypted_number = pow(number, d, n)

        decrypted += chr(decrypted_number)

    return decrypted


print("========== RSA CRYPTOGRAPHIC SOFTWARE ==========")

plaintext = input("\nEnter plaintext: ")

p = int(input("Enter first large prime number (p): "))
q = int(input("Enter second large prime number (q): "))

if not is_prime(p):
    print("\nError: First number is not prime.")

elif not is_prime(q):
    print("\nError: Second number is not prime.")

elif p == q:
    print("\nError: p and q must be different prime numbers.")

else:
    public_key, private_key = generate_keys(p, q)

    e, n = public_key
    d, _ = private_key

    print("\n========== KEY GENERATION ==========")

    print("Prime p:", p)
    print("Prime q:", q)

    print("\nn = p × q")
    print("n =", n)

    print("\nPublic Key:")
    print("(e, n) =", public_key)

    print("\nPrivate Key:")
    print("(d, n) =", private_key)

    try:
        ciphertext = encrypt(plaintext, public_key)

        print("\n========== ENCRYPTION ==========")

        print("Original Plaintext:")
        print(plaintext)

        print("\nEncrypted Ciphertext:")
        print(ciphertext)

        decrypted_text = decrypt(ciphertext, private_key)

        print("\n========== DECRYPTION ==========")

        print("Decrypted Plaintext:")
        print(decrypted_text)

    except ValueError as error:
        print("\nError:", error)