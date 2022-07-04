# 소인수분해의 대칭성
import math
# 에라토스테네스의 체 알고리즘
def is_primary(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else: # n over 2
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

import sys

M, N = map(int, sys.stdin.readline().strip().split())

for num in range(M, N+1):
    if is_primary(num) == True:
        print(num)