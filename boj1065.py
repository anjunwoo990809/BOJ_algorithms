N = int(input())

def num_hansu(x):
    cnt = 0
    for i in range(1, x+1):
        if i < 100:
            cnt += 1
        else:
            x_list = list(map(int, str(i)))
            if x_list[0] - x_list[1] == x_list[1] - x_list[2]:
                cnt += 1
    return cnt

print(num_hansu(N))
# print(num_hansu(110))
# print(num_hansu(210)) # 105
# print(num_hansu(1000)) # 144
# print(num_hansu(500)) # 119