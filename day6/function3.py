"""
Python的内置函数
- 数学相关: abs / divmod / pow / round / min / max / sum
- 序列相关: len / range / next / filter / map / sorted / slice / reversed
- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
- 数据结构: dict / list / set / tuple
- 其他函数: all / any / id / input / open / print / type
"""

def myfilter(mystr):
    return len(mystr) == 0

print(chr(0x9648))
print(hex(ord('陈')))
print(abs(-1.2345))
print(round(-1.2345)) # 向上取整
print(pow(1.2345, 5))
fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(1, 3)])
# print(fruits[slice(1, 3)])：这行代码使用 slice(1, 3) 创建了一个切片对象，
# 表示从索引 1（包括）到索引 3（不包括）的切片。
# 然后将这个切片对象应用到 fruits 列表上，输出结果为 ['peach', 'durian']，
# 即切片后的结果。
fruits2 = list(filter(myfilter, fruits))
#  filter 函数对 fruits 列表进行过滤。
# filter 函数接受一个函数（myfilter）和一个可迭代对象（fruits），
# 并返回一个迭代器，该迭代器生成使得函数返回值为 True 的元素。
print(fruits)
print(fruits2)