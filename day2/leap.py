"""输入年份,如果是闰年输出True 否则输出False"""

year = int(input("请输入年份： "))
# 如果代码太长写成一行显示不方便的画可以使用\或（）折行
is_leap = (year % 4 ==0 and year %100 !=0 or 
            year % 400 ==0)
#年一闰百年不闰：即如果year能够被4整除，但是不能被100整除，
# 则year是闰年。 （2）每四百年再一闰：如果year能够被400整除，则year是闰年。
print(is_leap)