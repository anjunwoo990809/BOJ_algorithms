import sys
input = sys.stdin.readline
# N <= 1000
# 50000 * O(1) * O(1)
books = {}
for _ in range(int(input())):
    # name <= 50
    name = input()
    if name in books:
        books[name] += 1
    else:
        books[name] = 1

fam = max(books.values())
candidate = []
for key, val in books.items():
    if val == fam:
        candidate.append(key)

print(sorted(candidate)[0])