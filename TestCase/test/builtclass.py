# -*- coding: UTF-8 -*-
def remove_duplicates(items):
    # TODO(You): 实现去重
    # res = list(set(items))
    # return res
    res = []
    for item in items:
        if not item in res:
            res.append(item)
    return res

# def filter_element(items, bound):
#     # TODO(You): 实现过滤
#     res = [item for item in items if item < bound]
#     return res
def filter_element(items, bound):
    res = []
    for item in items:
        if item >= bound:
            res.append(item)
    return res

if __name__ == '__main__':
    a = [1, 2, 3, 4, 4, 5, 5]
    print('输入: {}'.format(a))

    res = remove_duplicates(a)
    print('去重后的结果：{}'.format(res))

    bound = 3
    res = filter_element(a, bound)
    print('过滤小于{}的元素:{}'.format(bound, res))