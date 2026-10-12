import math

n = int(input("Enter a number: "))

count = 0

print("Relatively prime numbers are:")

for i in range(1, n + 1):
    if math.gcd(n, i) == 1:
        print(i, end=" ")
        count += 1

print("\nEuler's Totient Function φ(", n, ") =", count)