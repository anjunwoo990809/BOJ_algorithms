import sys
    
def is_primary(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else: # n over 2
        divider = n-1 # 2 이상
        res = True
        while divider > 1:
            if n % divider != 0:
                divider -= 1
            else:
                res = False
                break
        if res == True:
            return True
        else:
            return False

N = int(input())
# 1000 이하의 자연수
nums = list(map(int, sys.stdin.readline().strip().split()))
cnt = 0
for num in nums:
    if is_primary(num) == True:
        cnt += 1

print(cnt)
