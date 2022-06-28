import sys
n = int(input())

for _ in range(n):
    inputString = sys.stdin.readline().strip()
    total = 0
    score = 0
    for i in range(len(inputString)):
        if inputString[i] == "O":
            score += 1
            total += score
        else:
            score = 0
    print(total)