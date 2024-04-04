"""
作用域问题

"""
# 局部作用域
def fool():
    a = 5

fool()

# 全局作用域
b = 10

def foo2():
    print(b)

foo2()

def foo3():
    b = 100 # 局部变量
    print(b)
foo3()
print(b)

def foo4():
    global b
    b =200
    print(b)

foo4()
print(b)