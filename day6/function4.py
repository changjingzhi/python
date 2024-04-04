"""
Python常用模块
- 运行时服务相关模块: copy / pickle / sys / ...
- 数学相关模块: decimal / math / random / ...
- 字符串处理模块: codecs / re / ...
- 文件处理相关模块: shutil / gzip / ...
- 操作系统服务相关模块: datetime / os / time / logging / io / ...
- 进程和线程相关模块: multiprocessing / threading / queue
- 网络应用相关模块: ftplib / http / smtplib / urllib / ...
- Web编程相关模块: cgi / webbrowser
- 数据处理和编码模块: base64 / csv / html.parser / json / xml /

"""

import time
import shutil
import os

seconds = time.time()
#  time() 函数，用于获取当前时间戳（从 1970 年 1 月 1 日开始的秒数）。
# 具体来说，time.time() 返回的是一个浮点数，表示当前时间戳的秒数。
# 这个值通常用于计算时间间隔或者记录事件发生的时间。
print(seconds)
localtime = time.localtime(seconds)
# localtime(seconds) 接受一个时间戳作为参数，并返回一个包含本地时间信息的时间元组。
print(localtime)
print(localtime.tm_year)
# 通过索引 tm_year 可以获取时间元组中的年份信息。
print(localtime.tm_mon)

print(localtime.tm_mday)
asctime = time.asctime(localtime)
# asctime(localtime) 接受一个时间元组作为参数，
# 并返回一个字符串，表示该时间元组对应的时间信息。
print(asctime)
strtime = time.strftime('%Y-%m-%d %H:%M:%S',localtime)
# strftime(format, localtime) 接受一个格式化字符串 format 和一个时间元组 localtime，
# 并返回一个按照指定格式表示时间的字符串。
print(strtime)
mydate = time.strptime('2018-1-1','%Y-%d-%m')
# strptime(date_string, format) 接受一个时间字符串 date_string 
# 和一个格式化字符串 format，并返回一个时间元组，表示根据给定格式解析后的时间。
print(mydate)
print(mydate.tm_year)

shutil.copy('/Users/Hao/hello.py', '/Users/Hao/Desktop/first.py')
# 行代码使用 shutil.copy() 函数将 /Users/Hao/hello.py 文件复制到 
# /Users/Hao/Desktop/first.py。这个函数可以用于文件的复制操作。
os.system('ls -l')
# 使用 os.system() 函数执行系统命令 ls -l，显示当前目录下的文件和目录列表。
os.chdir('/Users/Hao')
# 使用 os.chdir() 函数改变当前工作目录到 /Users/Hao，即切换到指定目录。
os.system('ls -l')
# 执行系统命令 ls -l，显示 /Users/Hao 目录下的文件和目录列表。
os.mkdir('test')
