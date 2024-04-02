""""输入一个正整数判断它是不是素数"""

from math import sqrt

num = int(input('请输入一个正整数:'))
end = int(sqrt(num))
is_prime = True
for x in range(2,end+1):
    if num %x == 0:
        is_prime =False
        break
if is_prime and num != 1:
    print('%d是素数'%num)
else:
    print("%d不是素数"%num)
# 质数（prime number）又称素数，有无限个。一个大于1的自然数，
# 除了1和它本身外，不能被其他自然数（质数）整除，
# 换句话说就是该数除了1和它本身以外不再有其他的因数；否则称为合数。