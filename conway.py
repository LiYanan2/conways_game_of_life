# 1.   当前细胞为存活状态时，当周围低于2个（不包含2个）存活细胞时，该细胞变成死亡状态。（模拟生命数量稀少）
#
# 2.   当前细胞为存活状态时，当周围有2个或3个存活细胞时，该细胞保持原样。
#
# 3.   当前细胞为存活状态时，当周围有3个以上的存活细胞时，该细胞变成死亡状态。（模拟生命数量过多）
#
# 4.   当前细胞为死亡状态时，当周围有3个存活细胞时，该细胞变成存活状态。（模拟繁殖）
import random
import numpy as np
import time

# 定义一个10*10的生命棋盘table
size = 10
i = 1
b = []  # 临时生命棋盘
for row in range(size):
    a = []
    for colum in range(size):
        a.append(random.choice([0, 1]))
    b.append(a)
table = np.array(b, dtype=int)

# conway函数
while True:
    for row in range(size):
        for colum in range(size):
            value = table[row][colum]
            total = table[(row - 1) % size][(colum - 1) % size] + table[(row - 1) % size][colum % size] + \
                    table[(row - 1) % size][
                        (colum + 1) % size] + \
                    table[row % size][(colum - 1) % size] + \
                    table[row % size][(colum + 1) % size] + table[(row + 1) % size][(colum - 1) % size] + \
                    table[(row + 1) % size][colum % size] + \
                    table[(row + 1) % size][(colum + 1) % size]
            if value == 0 and total == 3:
                table[row][colum] = 1
            else:
                if total < 2:
                    table[row][colum] = 0
                elif total == 2 or total == 3:
                    pass
                else:
                    table[row][colum] = 0
    print("***********************")
    print(i)
    print(table)
    time.sleep(0)
    i = i + 1
