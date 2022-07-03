M = int(input())
N = int(input())

def is_primary(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else: # n over 2
        divider = n-1 # 2 이상
        res = True
        while divider > 1:
            if num % divider != 0:
                divider -= 1
            else:
                res = False
                break
        if res == True:
            return True
        else:
            return False
        
# suppose M <= N

primary = []
candidate = [i for i in range(M, N+1)]    
for num in candidate:
    if is_primary(num) == True:
        primary.append(num) # already increasing state

if len(primary) == 0:
    print(-1)

else:
    print(sum(primary))
    print(primary[0])
