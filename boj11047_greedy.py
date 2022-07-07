# N types of coin
import sys

input = sys.stdin.readline
N, K = map(int, input().strip().split())

# x = deque()
x = [int(input()) for _ in range(N)]
x.reverse()

cnt = 0

for coin in x:
    cnt += K // coin
    K %= coin
print(cnt)