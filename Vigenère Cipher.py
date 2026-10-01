def prepare(text):
    return "".join(ch for ch in text.upper() if ch.isalpha())


def encrypt(plaintext, keyword):
    ciphertext = ""
    key_values = []

    for i, ch in enumerate(plaintext):
        p = ord(ch) - 65
        k = ord(keyword[i % len(keyword)]) - 65

        key_values.append(k)

        c = (p + k) % 26
        ciphertext += chr(c + 65)

    return ciphertext, key_values


def decrypt(ciphertext, keyword):
    plaintext = ""

    for i, ch in enumerate(ciphertext):
        c = ord(ch) - 65
        k = ord(keyword[i % len(keyword)]) - 65

        p = (c - k) % 26
        plaintext += chr(p + 65)

    return plaintext


plaintext = prepare(input("Enter plaintext: "))
keyword = prepare(input("Enter keyword: "))

if not keyword:
    print("Keyword cannot be empty.")
else:
    ciphertext, key_values = encrypt(plaintext, keyword)

    plaintext_values = [ord(ch) - 65 for ch in plaintext]
    ciphertext_values = [ord(ch) - 65 for ch in ciphertext]

    repeated_key = "".join(
        keyword[i % len(keyword)]
        for i in range(len(plaintext))
    )

    print("\nPlaintext: ", plaintext)
    print("Key:       ", repeated_key)
    print("Ciphertext:", ciphertext)

    print("\nPlaintext values: ", plaintext_values)
    print("Key values:       ", key_values)
    print("Ciphertext values:", ciphertext_values)

    decrypted = decrypt(ciphertext, keyword)
    print("\nDecrypted text:", decrypted)