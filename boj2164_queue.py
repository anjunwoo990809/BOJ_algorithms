# 카드2 : queue에 대한 문제

# 6
# 123456 -> 23456 -> 34562
# 34562 -> 4562 -> 5624
# 5624 -> 624 -> 246
# 246 -> 46 -> 64
# 64 -> 4

from collections import deque

N = int(input())

deq = deque()

for i in range(1,N+1):
    deq.append(i)
# deque([1, 2, ..., N])

while True:
    if len(deq) == 1:
        break
    elif len(deq) > 1:
        deq.popleft()
        tmp = deq.popleft()
        deq.append(tmp)

print(deq[0]) # deque의 첫 번쨰 element