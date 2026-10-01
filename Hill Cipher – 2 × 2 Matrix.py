from math import gcd


def mod_inverse(a, m=26):
    a %= m

    for x in range(1, m):
        if (a * x) % m == 1:
            return x

    return None


def matrix_inverse(matrix):
    a, b = matrix[0]
    c, d = matrix[1]

    determinant = (a * d - b * c) % 26

    if gcd(determinant, 26) != 1:
        return None, determinant

    det_inverse = mod_inverse(determinant)

    inverse = [
        [
            (det_inverse * d) % 26,
            (det_inverse * -b) % 26
        ],
        [
            (det_inverse * -c) % 26,
            (det_inverse * a) % 26
        ]
    ]

    return inverse, determinant


def process_text(text, matrix):
    text = "".join(
        ch for ch in text.upper()
        if ch.isalpha()
    )

    if len(text) % 2 != 0:
        text += "X"

    result = ""

    for i in range(0, len(text), 2):
        x1 = ord(text[i]) - 65
        x2 = ord(text[i + 1]) - 65

        y1 = (
            matrix[0][0] * x1 +
            matrix[0][1] * x2
        ) % 26

        y2 = (
            matrix[1][0] * x1 +
            matrix[1][1] * x2
        ) % 26

        result += chr(y1 + 65)
        result += chr(y2 + 65)

    return result


print("Enter the 2 x 2 key matrix:")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

key_matrix = [
    [a, b],
    [c, d]
]

inverse_matrix, determinant = matrix_inverse(key_matrix)

print("\nKey Matrix:")
for row in key_matrix:
    print(row)

print("\nDeterminant mod 26:", determinant)

if inverse_matrix is None:
    print("Invalid key matrix!")
    print("The matrix is NOT invertible modulo 26.")

else:
    print("Matrix is invertible modulo 26.")

    print("\nInverse Matrix:")
    for row in inverse_matrix:
        print(row)

    plaintext = input("\nEnter plaintext: ")

    ciphertext = process_text(plaintext, key_matrix)
    print("Encrypted text:", ciphertext)

    decrypted = process_text(ciphertext, inverse_matrix)
    print("Decrypted text:", decrypted)