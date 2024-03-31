import math

radius = float(input("请输入圆的半径： "))
perimeter = 2 * math.pi * radius
ares = math.pi * radius * radius
print("周长： %.2f " % perimeter) # 周长 2 pi r
print("面积： %.2f" % ares) # 面积 pi*r*r