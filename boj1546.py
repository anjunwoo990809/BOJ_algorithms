import sys

n = int(input()) # number of tests
first_score = list(map(int, sys.stdin.readline().strip().split()))

first_score = sorted(first_score)

max = first_score[-1]

sum = 0
for i, score in enumerate(first_score):
    sum += score/max * 100

print(sum/n)