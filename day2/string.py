"""字符串的操作"""

str1 = 'hello, world!'
print ("字符串的长度是：",len(str1))
print("单词首字母的大写：",str1.title())
print("字符串变大写：",str1.upper())
print('字符串是不是大写',str1.isupper())
print("字符串是不是以hello开头:",str1.startswith('hello'))
print("字符串是不是以hello结尾:",str1.endswith('hello'))
print("字符串是不是以感叹号开头：",str1.startswith('!'))
print("字符串是不是以感叹号结尾：",str1.endswith("!"))
str2 = '- \u9a86\u6601'
str3 = str1.title() + ' ' + str2.lower()
print(str3)
# 这段代码展示了一些常见的字符串操作：

# 1.`len(str1)`: 返回字符串的长度。
# 2.`str1.title()`: 返回每个单词的首字母大写的字符串。
# 3.`str1.upper()`: 返回字符串的大写形式。
# 4.`str1.isupper()`: 检查字符串是否全为大写。
# 5.`str1.startswith('hello')`: 检查字符串是否以指定的子字符串开头。
# 6. str1.endswith('hello')`: 检查字符串是否以指定的子字符串结尾。
# 7.`str2 = '- \u9a86\u6601'`: 创建一个包含特殊字符的字符串。
# 8.`str3 = str1.title() + ' ' + str2.lower()`: 将两个字符串合并，并将第二个字符串转换为小写。