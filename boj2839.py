N = int(input())

# N = 3*x + 5*y 부정방정식 풀기
# 5에 우선순위가 부여됨
# 가능한 y에 대해 N - 5*Y == 3 * x인 정수 x
# 
def minimum_bags(n):
    
    if N % 5 == 0:
        return int(N/5)

    five_max = int(N/5) # maximum y
    three_cnt = 0 # initial
    while five_max >= 0:
        # y를 최대로 하면서 만족시키는 첫번째 x값을 찾기
        if (N-5*five_max) % 3 == 0:
            three_cnt = int((N-5*five_max)/3)
            break
        else:
            five_max -= 1

    if (five_max == 0) and (N % 3 != 0):
        return -1

    else:
        return five_max + three_cnt

print(minimum_bags(N))