def caesar_encrypt(text, shift):
    result = ""

    for ch in text.upper():
        if ch.isalpha():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)

    return result


def caesar_decrypt(text, shift):
    result = ""

    for ch in text:
        result += chr((ord(ch) - 65 - shift) % 26 + 65)

    return result


def transpose_encrypt(text, columns):
    rows = []

    for i in range(0, len(text), columns):
        row = text[i:i + columns]

        if len(row) < columns:
            row += "X" * (columns - len(row))

        rows.append(row)

    result = ""

    for col in range(columns):
        for row in rows:
            result += row[col]

    return result


def transpose_decrypt(text, columns):
    rows = len(text) // columns

    matrix = [[""] * columns for _ in range(rows)]

    index = 0

    for col in range(columns):
        for row in range(rows):
            matrix[row][col] = text[index]
            index += 1

    result = ""

    for row in matrix:
        result += "".join(row)

    return result


plaintext = input("Enter plaintext: ")
shift = int(input("Enter substitution shift: "))
columns = int(input("Enter number of transposition columns: "))

# Encryption
stage1 = caesar_encrypt(plaintext, shift)
print("\nAfter substitution:", stage1)

stage2 = transpose_encrypt(stage1, columns)
print("After transposition:", stage2)

# Decryption
reverse_stage1 = transpose_decrypt(stage2, columns)
print("\nAfter reversing transposition:", reverse_stage1)

reverse_stage2 = caesar_decrypt(reverse_stage1, shift)
print("Decrypted text:", reverse_stage2)