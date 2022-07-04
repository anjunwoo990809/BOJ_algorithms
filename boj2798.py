# brute force algorithm
import sys

N, M = map(int, sys.stdin.readline().strip().split())

numbers = list(map(int, sys.stdin.readline().strip().split()))

max_sum = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            sum = numbers[i] + numbers[j] + numbers[k]
            if (sum <= M) and (max_sum<sum):
                max_sum = sum

print(max_sum)