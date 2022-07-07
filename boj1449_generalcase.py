import sys
input = sys.stdin.readline
n, l = map(int, input().split())

# 좌표 압축
coord = list(map(int, input().split()))
coord = sorted(coord)

# point 변수 i
i = 0
cnt = 0

while i <= coord[-1]:
    if i in coord:
        i += l
        cnt += 1
    else:
        i += 1
print(cnt)