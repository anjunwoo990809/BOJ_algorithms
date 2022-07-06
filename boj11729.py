# 하노이탑
# N <= 20
N = int(input())

# a -> c 가 목적인 프로그램.

def hanoi_move(N, a=1, b=2, c=3):
    if N == 1:
        print(a, c)
    else: #  N > 1
        # 1 ~ N-1의 이동
        hanoi_move(N-1, a, c, b)
        print(a, c) # N의 이동
        hanoi_move(N-1, b, a, c)

# 옮긴 횟수 K
K = 1
for _ in range(N-1):
    K = K*2 + 1
print(K)
# moving procedures
hanoi_move(N)