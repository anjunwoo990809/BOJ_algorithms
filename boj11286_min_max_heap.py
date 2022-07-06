# 절댓값 힙
import heapq as hq
import sys

# 빠른 입출력 - python은 느린 언어
input = sys.stdin.readline

# min heap과 max heap을 만들어 양수 음수 따로 저장
min_heap = [] # 1, 4, 7
max_heap = [] # -1, -4, -7

for _ in range(int(input())):
    x = int(input())
    if x:
        if x > 0:
            hq.heappush(min_heap, x)
        else:
            hq.heappush(max_heap, -x)
        
    else: # x == 0
        if min_heap:
            if max_heap:
                if min_heap[0] < max_heap[0]:
                    print(hq.heappop(min_heap))
                else:
                    print(-hq.heappop(max_heap))
            else:
                print(hq.heappop(min_heap))
        else:
            if max_heap:
                print(-hq.heappop(max_heap))
            else:
                print(0)