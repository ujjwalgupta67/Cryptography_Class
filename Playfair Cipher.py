def generate_matrix(key):
    key = key.upper().replace("J", "I")

    letters = []

    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch.isalpha() and ch not in letters:
            letters.append(ch)

    matrix = []

    for i in range(0, 25, 5):
        matrix.append(letters[i:i + 5])

    return matrix


def find_position(matrix, letter):
    if letter == "J":
        letter = "I"

    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col


def prepare_plaintext(text):
    text = "".join(
        ch for ch in text.upper().replace("J", "I")
        if ch.isalpha()
    )

    pairs = []
    i = 0

    while i < len(text):
        first = text[i]

        if i + 1 >= len(text):
            second = "X"
            i += 1

        elif text[i + 1] == first:
            second = "X"
            i += 1

        else:
            second = text[i + 1]
            i += 2

        pairs.append(first + second)

    return pairs


def encrypt_pair(pair, matrix):
    r1, c1 = find_position(matrix, pair[0])
    r2, c2 = find_position(matrix, pair[1])

    if r1 == r2:
        return (
            matrix[r1][(c1 + 1) % 5] +
            matrix[r2][(c2 + 1) % 5]
        )

    elif c1 == c2:
        return (
            matrix[(r1 + 1) % 5][c1] +
            matrix[(r2 + 1) % 5][c2]
        )

    else:
        return matrix[r1][c2] + matrix[r2][c1]


def decrypt_pair(pair, matrix):
    r1, c1 = find_position(matrix, pair[0])
    r2, c2 = find_position(matrix, pair[1])

    if r1 == r2:
        return (
            matrix[r1][(c1 - 1) % 5] +
            matrix[r2][(c2 - 1) % 5]
        )

    elif c1 == c2:
        return (
            matrix[(r1 - 1) % 5][c1] +
            matrix[(r2 - 1) % 5][c2]
        )

    else:
        return matrix[r1][c2] + matrix[r2][c1]


key = input("Enter key: ")
plaintext = input("Enter plaintext: ")

matrix = generate_matrix(key)

print("\n5 x 5 Key Matrix:")
for row in matrix:
    print(" ".join(row))

pairs = prepare_plaintext(plaintext)

print("\nLetter pairs:", " ".join(pairs))

ciphertext = ""

for pair in pairs:
    ciphertext += encrypt_pair(pair, matrix)

print("Encrypted text:", ciphertext)

decrypted = ""

for i in range(0, len(ciphertext), 2):
    decrypted += decrypt_pair(ciphertext[i:i + 2], matrix)

print("Decrypted text:", decrypted)