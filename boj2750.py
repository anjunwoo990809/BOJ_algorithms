lst = []
for _ in range(int(input())):
    num = int(input())
    lst.append(num)

for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

for n in lst:
    print(n)