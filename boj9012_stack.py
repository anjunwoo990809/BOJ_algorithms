# 올바른 괄호쌍 찾기 : stack

# (가 먼저 나와야 하고, )는 앞서 나온 (의 개수와 매칭이 됨.
# stack을 쓰는 이유는 
# | 1  2  3  이라는 (에 대한 stack을 만들고
# )가 들어올 시 stack의 값을 하나씩 소진하는
# 방법으로 stack을 empty하게 만들면 vps 구현

import sys
# T = int(sys.stdin.readline().strip())
# T를 다시 쓸 것이 아니라면 굳이 선언할 필요 없음

for _ in range(int(sys.stdin.readline().strip())):
    res = "YES"
    stack = []
    # inputs = list(map(str, sys.stdin.readline().strip()))
    # for item in list(map(str, sys.stdin.readline().strip())):
    # 위처럼 list 형태로 iterm을 받아도 되지만 str의 한글자씩을 받자.
    for item in sys.stdin.readline().strip():
        if item == "(":
            stack.append(True)    
        else:
            if len(stack) == 0:            
                res = "NO"
                break
            else:
                stack.pop()
    if len(stack) > 0:
        res = "NO"
    print(res)

# 정리
# 굳이 불필요한 변수 선언 줄이기