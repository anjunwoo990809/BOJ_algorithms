x = int(input())

i = 0
num = 0
while x > num:
    i += 1
    num += i

# x <= num
# tmp >= 0
tmp = num - x

if i % 2 == 1:
    a = tmp + 1
    b = i - tmp
    
else:
    a = i - tmp
    b = tmp + 1

print(f'{a}/{b}')