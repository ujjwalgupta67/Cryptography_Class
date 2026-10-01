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


def rail_fence_encrypt(text, rails):
    if rails <= 1:
        return text

    fence = [""] * rails
    rail = 0
    direction = 1

    for ch in text:
        fence[rail] += ch

        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1

        rail += direction

    return "".join(fence)


def rail_fence_decrypt(cipher, rails):
    if rails <= 1:
        return cipher

    pattern = []
    rail = 0
    direction = 1

    for _ in cipher:
        pattern.append(rail)

        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1

        rail += direction

    counts = [pattern.count(r) for r in range(rails)]

    fence = []
    index = 0

    for count in counts:
        fence.append(list(cipher[index:index + count]))
        index += count

    positions = [0] * rails
    result = ""

    for r in pattern:
        result += fence[r][positions[r]]
        positions[r] += 1

    return result


plaintext = input("Enter plaintext: ")
shift = int(input("Enter Caesar shift: "))
rails = int(input("Enter number of rails: "))

# Encryption
caesar_result = caesar_encrypt(plaintext, shift)
print("\nAfter Caesar Cipher:", caesar_result)

ciphertext = rail_fence_encrypt(caesar_result, rails)
print("After Rail Fence Cipher:", ciphertext)

# Decryption - reverse order
rail_result = rail_fence_decrypt(ciphertext, rails)
print("\nAfter Rail Fence Decryption:", rail_result)

decrypted = caesar_decrypt(rail_result, shift)
print("After Caesar Decryption:", decrypted)