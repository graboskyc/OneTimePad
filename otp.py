import random
import argparse

letters = "ABCDEFGHJLMNPRSTUVWXYZ"
numbers = "23456789"
charset = letters + numbers
def genMatrix():
    n = 11
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.choice(charset))
        matrix.append(row)
    return matrix


def printMatrix(matNumber):
    mat = genMatrix()
    letArr=list(letters)
    header = letArr[:11]
    columns = letArr[11:]
    print("\n")
    print("      ONE TIME PAD " + letArr[matNumber] + "\n")

    for i in range(10):
        printString = ""
        if i == 0:
            printString = "    " + " ".join(header)
            printString = printString + "\n  +-----------------------"
        else:
            printString = columns[i ] + " | " + " ".join(mat[i])
        print(printString)

    print("\n")

parser = argparse.ArgumentParser(description='One Time Pad')
parser.add_argument("count", type=int, help="Number of OTPs to generate, defaults to 1", nargs='?', default=1)
args = parser.parse_args()
for i in range(args.count):
    printMatrix(i)