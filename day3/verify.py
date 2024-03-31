"""用户身份验证"""

import getpass
username = input('请输入用户名')

# 不显示密码
passward = getpass.getpass('请输入口令')

if username == 'admin' and passward=='123456':
    print('身份验证成功')
else:
    print('身份验证失败')