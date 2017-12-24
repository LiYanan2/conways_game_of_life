# 1.   当前细胞为存活状态时，当周围低于2个（不包含2个）存活细胞时，该细胞变成死亡状态。（模拟生命数量稀少）
#
# 2.   当前细胞为存活状态时，当周围有2个或3个存活细胞时，该细胞保持原样。
#
# 3.   当前细胞为存活状态时，当周围有3个以上的存活细胞时，该细胞变成死亡状态。（模拟生命数量过多）
#
# 4.   当前细胞为死亡状态时，当周围有3个存活细胞时，该细胞变成存活状态。（模拟繁殖）
import random
import numpy as np

#定义一个10*10的生命棋盘table
b=[]
for row in range(10):
    a=[]
    for colum in range(10):
        a.append(random.choice([0,1]))
    b.append(a)
table=(np.array(b,dtype=int))





