import turtle as tl

def draw_rectangle(x,y,width,height):
    tl.goto(x,y) # 到x,y位置
    tl.pencolor('red')
    tl.fillcolor('red')
    tl.begin_fill() # 填充颜色开始
    for i in range(2):
        tl.forward(width)
        tl.left(90)
        tl.forward(height)
        tl.left(90)
    tl.end_fill() # 填充颜色结束

def draw_star(x,y,radius):
    tl.setpos(x,y)
    pos1 = tl.pos() # pos 获取当前海龟的位置
    tl.circle(-radius,72)
    pos2 = tl.pos()
    tl.circle(-radius,72)
    pos3 = tl.pos()
    tl.circle(-radius,72)
    pos4 = tl.pos()
    tl.circle(-radius,72)
    pos5 = tl.pos()
    tl.color('yellow','yellow')
    tl.begin_fill()
    tl.goto(pos3)
    tl.goto(pos1)
    tl.goto(pos4)
    tl.goto(pos2)
    tl.goto(pos5)
    tl.end_fill()


def main():
    tl.speed(5)
    tl.penup()
    x, y = -270,-180
    width,height = 540,360
    draw_rectangle(x,y,width,height)

    pice = 22
    center_x,center_y = x + 5*pice,y+height-pice*5
    tl.goto(center_x,center_y)
    tl.left(90)
    tl.forward(pice*3)
    tl.right(90)
    draw_star(tl.xcor(),tl.ycor(),pice*3)
    
    x_poses, y_poses = [10,12,12,10],[2,4,7,9]

    for x_pos,y_pos in zip(x_poses,y_poses):
        tl.goto(x+x_pos*pice,y+height-y_pos*pice)
        tl.left(tl.towards(center_x,center_x)-tl.heading())
        tl.forward(pice)
        tl.right(90)
        draw_star(tl.xcor(),tl.ycor(),pice)
    
    tl.ht()
    
    tl.mainloop()

if __name__ == '__main__':
    main()

