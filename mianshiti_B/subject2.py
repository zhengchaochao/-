'''
题目：
    上面矩阵的中的1代表海岸线，0代表小岛。求第二岛的面积(即被1中包围的0的个数，如果只有一个小岛，输出最大岛的面积)。
    注意:1. 仅求这样的0，该0所在行中被两个1包围，该0所在列中被两个1包围;
    2. 输入矩阵中包含的小岛K >= 1;样例输入 :
    1 1 1 1 1 1
    1 1 0 0 0 1
    1 0 0 0 1 0
    1 1 0 1 1 1
    0 1 0 1 0 0
    1 1 1 1 1 1
    样例输出:8
'''

'''
整体思路:
    这里将目标放在了一个二维数组中,然后遍历这个数组,将符合条件的小岛的编号设置为8
    计算总面积只需要计算8的个数就行了
    计算每个面积运用递归,计算该小岛与四周的符合条件的小岛的距离,最后返回的是一个列表,里面包含每个小岛的面积
'''


#  首先遍历整个二维数组,将符合条件的小岛设置为8
def target(my_target):
    for i in range(1, 6):
        for j in range(1, 6):
            # 满足是0(小岛)
            if my_target[i][j] == 0:
                # 判断 小岛 左右上下是否都含有1(海岸线)
                my_left = [my_target[i][x] for x in range(j)]
                my_right = [my_target[i][x] for x in range(j + 1, 6)]
                my_top = [my_target[x][j] for x in range(i)]
                my_bottom = [my_target[x][j] for x in range(i + 1, 6)]
                if 1 in my_left and 1 in my_right and 1 in my_top and 1 in my_bottom:
                    my_target[i][j] = 8


# 如果只是计算总小岛的面积的话,只需要计算所有8的个数就可以了
# 这里要计算第二个小岛的面积,我这里不知道第二个小岛是怎么定义的,因此计算出了每个小岛的面积
# 计算小岛的面积,这里为了避免重复计算一个小岛群的面积,将已经计算的面积重新设置为1
# 主要用了递归,计算了该岛群 上下左右符合条件的个数
def area(my_target, i, j):
    if 0 <= i < 6 and 0 <= j < 6 and my_target[i][j] == 8:
        my_target[i][j] = 1
        return 1 + area(my_target, i - 1, j) + area(my_target, i + 1, j) + area(my_target, i, j - 1) + area(my_target,
                                                                                                            i, j + 1)
    else:
        return 0


# 计算每个岛群的面积
def area_list(my_target):
    my_area = []
    for i in range(1, 6):
        for j in range(1, 6):
            if my_target[i][j] == 8:
                # 将每个岛群的面积放在列表中
                my_area.append(area(my_target, i, j))
    return my_area


if __name__ == '__main__':
    # 随意的二维数组,可以更改进行测试
    my_target = [
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 1]
    ]
    target(my_target)
    # 最终的岛群的面积放在列表中,有几个岛群列表中有几个元素
    area_list = area_list(my_target)
    print(area_list[0])
