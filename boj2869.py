import sys

A, B, V = map(int, sys.stdin.readline().strip().split())

# 부등식을 세워 해결하는 문제
if (V-A)%(A-B) == 0:
    additional_steps = int((V-A)/(A-B))
else:
    additional_steps = int((V-A)/(A-B) + 1)

print(1+additional_steps)