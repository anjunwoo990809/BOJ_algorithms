# 절댓값 힙
import heapq as hq
import sys

# 빠른 입출력 - python은 느린 언어
input = sys.stdin.readline

pq = []
for _ in range(int(input())):
    x = int(input())
    if x != 0:
        # tuple을 우선순위큐에 저장함.
        hq.heappush(pq, (abs(x),x))
    
    else: # x == 0
        print(hq.heappop(pq)[1] if pq else 0)
    
