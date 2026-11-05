import math
def emerald(N, W):
    x = 0
    list = []
    for i in range(N):
        if W[i] % 2 == 0:
            x = sum(W[i], x)
        if W[i] % 2 != 0:
            list.append(x)
            x = 0
    list.append(x)
    print(max(list))
emerald(13, [2, 3, 4, 4, 5, 6, 1, 2, 2, 2, 1, 8, 2])