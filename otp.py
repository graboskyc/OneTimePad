import random

letters = "ABCDEFGHJLMNPRSTUVWXYZ"
numbers = "23456789"
charset = letters + numbers
def generate_matrix():
    n = 11
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.choice(charset))
        matrix.append(row)
    return matrix

mat = generate_matrix()
letters=list(letters)
header = letters[:11]
columns = letters[11:]

print("\n")
print("        ONE TIME PAD\n")

for i in range(10):
    printString = ""
    if i == 0:
        printString = "    " + " ".join(header)
        printString = printString + "\n  +-----------------------"
    else:
        printString = columns[i ] + " | " + " ".join(mat[i])
    print(printString)

print("\n")