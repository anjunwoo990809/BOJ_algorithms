def dn(n):
    tmp = n
    res = n
    n_length = 1
    while tmp >= 10:
        tmp = tmp // 10
        n_length += 1
    
    for _ in range(n_length):
        res += n % 10
        n = n//10
    return res

# print(dn(33)) # 39

# print(dn(39)) # 51

def self_number(m):
    i = 1
    dn_numbers=[]
    while i <= m:
        new = dn(i)
        if new not in dn_numbers:
            dn_numbers.append(new)
        i += 1
    for num in range(1, m+1):
        if num not in dn_numbers:
            print(num)

# self_number(100)
self_number(10000)