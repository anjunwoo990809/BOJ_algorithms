N = 123456 * 2 + 1 # maximum number in program
# 범위 제한 내의 Boolean list를 생성함
arr = [True] * N

# by aristotle do the calculation first
for i in range(2, int(N**0.5)+1):
    if arr[i]:
        # i의 배수표현
        for j in range(2*i, N, i):
            arr[j] = False

def cnt_prime_number(res):
    cnt = 0
    for i in range(res+1, res*2 + 1):
        if arr[i]:
            cnt+=1
    print(cnt)

while True :
    a = int(input())
    if a == 0:
        break
    cnt_prime_number(a)
