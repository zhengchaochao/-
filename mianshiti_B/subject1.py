'''
题目：
    给定一组数字， 一组有9个数字，将这9个数字填写到3*3的九宫格内;使得横，竖，斜对角一条线上的三个数字之和相等;如果无解则打印无解;
'''

'''
整体思路:
    对给定的列表排序
    判断是否满足组成九宫格的基本条件
    满足后按'二,四为肩,六,八为足。上九下一，左七右三'进行填充二维列表,并做进一步的判断
'''


def list_confirmation(li):
    # 使用冒泡排序法对列表进行排序
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]

    # 将九个数字放在一个二维的列表中
    new_li = [[li[1], li[8], li[3]],
              [li[6], li[4], li[2]],
              [li[5], li[0], li[7]]]
    sum_li = [0 for i in range(8)]
    for j in range(3):
        sum_li[0] += new_li[0][j]
        sum_li[1] += new_li[1][j]
        sum_li[2] += new_li[2][j]
        sum_li[3] += new_li[j][0]
        sum_li[4] += new_li[j][1]
        sum_li[5] += new_li[j][2]
        sum_li[6] += new_li[j][j]
        sum_li[7] += new_li[j][2 - j]
    if sum_li[0] == sum_li[1] == sum_li[2] == sum_li[3] == sum_li[4] == sum_li[5] == sum_li[6] == sum_li[7]:
        print(new_li)
        print('成功')
    else:
        print('失败')


if __name__ == '__main__':
    # 此处修改 li进行测试,能组成九宫格返回成功,否则返回失败
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_confirmation(li)
