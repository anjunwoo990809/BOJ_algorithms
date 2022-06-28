import sys
c = int(input())

for _ in range(c):
    info = list(map(int, sys.stdin.readline().strip().split()))
    n = info[0]
    scores = info[1:]
    avg = sum(scores)/n
    cnt = 0
    for score in scores:
        if score > avg:
            cnt += 1
        else:
            cnt += 0
    print(f'{cnt/n*100:.3f}%')