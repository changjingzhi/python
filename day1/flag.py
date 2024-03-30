import turtle

def draw_rectangle(x,y,width,height):
    """绘制矩形，红旗的红色底面"""
    turtle.goto(x,y) # turtle.goto()将海龟运动到指定坐标
    turtle.pencolor('red') # turtle.(方法) 这个是类中定义的函数的访问方法
    turtle.fillcolor('red') # 将填充颜色设置为红色
    turtle.begin_fill() # 用于填充一个图形
    for i in range(2):
        turtle.forward(width)
        turtle.left(90) # 用于将海龟向左旋转一定角度
        turtle.forward(height) # forward用于让海龟向当前方向前进一定距离，distance 可以随意指定
        turtle.left(90)
    turtle.end_fill() # 停止begin_fill的填充

def draw_star(x,y,radius):
    """绘制五角星"""
    turtle.setpos(x,y) # 将海龟移动到指定位置，不在画布上留下痕迹
    pos1 = turtle.pos() # 用于获取当前海龟位置，返回元组（x,y）
    turtle.circle(-radius,72) # circle用于绘制一个圆或近似圆，radius表示圆弧的半径，extent是圆弧的角度
    pos2 = turtle.pos()
    turtle.circle(-radius,72)
    pos3 = turtle.pos()
    turtle.circle(-radius,72)
    pos4 = turtle.pos()
    turtle.circle(-radius,72)
    pos5 = turtle.pos()
    turtle.color('yellow','yellow')
    turtle.begin_fill()
    turtle.goto(pos3)
    turtle.goto(pos1)
    turtle.goto(pos4)
    turtle.goto(pos2)
    turtle.goto(pos5)
    turtle.end_fill()

def main():
    """主函数"""
    turtle.speed(10) # 用于设置海龟绘制的速度，0最快，5非常慢，0-10范围内的时速
    turtle.penup()
    x,y = -270,-180
    # 画国旗主体，
    width, height = 540,360
    draw_rectangle(x,y,width,height)
    # 画大星星
    pice = 22
    center_x, center_y = x +5 *pice, y + height - pice*5
    turtle.goto(center_x,center_y)
    turtle.left (90)
    turtle.forward(pice*3) # 让海龟向当前方向前进指定的像素距离。
    turtle.right(90)
    draw_star(turtle.xcor(),turtle.ycor(),pice*3)
    # x用于获取海龟的x坐标，返回当前x坐标的浮点数值
    # ycor()用于获取当前海龟的y坐标 
    x_poses, y_poses = [10,12,12,10],[2,4,7,9]
    #画小星星
    for x_pos,y_pos in zip(x_poses,y_poses):
        # zip()是python内置函数之一，可以将对象值的元素打包成一个个元组，
        turtle.goto(x+ x_pos*pice,y+height-y_pos*pice)
        turtle.left(turtle.towards(center_x,center_y)-turtle.heading())
        # heading用于获取当前海龟朝向的角度，这个角度表示海龟当前的正方向。
        turtle.forward(pice)
        turtle.right(90)
        draw_star(turtle.xcor(),turtle.ycor(),pice)
    # 显示小海龟
    turtle.ht()
    turtle.mainloop()

if __name__ == '__main__':
    main()
# python常见的代码块，用于在模块被直接运行时执行一些代码，而在模块被导入时不执行这些代码
# 



