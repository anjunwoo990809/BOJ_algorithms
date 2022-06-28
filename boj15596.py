def solve(a):
    ans = 0
    for item in a:
        ans += item 
    return ans

a = [1, 2, 3]
print(solve(a))

b = [1, 2, 3, 4]
print(solve(b))