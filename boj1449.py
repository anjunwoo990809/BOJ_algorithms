import sys
input = sys.stdin.readline
n, l = map(int, input().split())

# boolean list로 탐색 범위를 지정하는 skill
coord = [False] * 1001
for i in map(int, input().split()):
    coord[i] = True

# point 변수 x
x = 0
cnt = 0
# True 이면 테이프의 길이 만큼은 더이상 신경쓰지 않아도 되므로 jump
while x < 1001:
    if coord[x]:
        x += l
        cnt += 1
    else:
        x += 1
print(cnt)

# 좌표가 1000이 아닌 매우 큰 수일때
# 위와 같은 방법을 쓸 수 없음.
# 그렇다면 구멍이 난 위치만을 가지고 문제를 접근