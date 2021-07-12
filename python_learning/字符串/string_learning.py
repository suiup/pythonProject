print("字符串")

"""
特性： 
    用 双引号("") 或 单引号('') 定义字符串
    
    大多数编程语言都使用双引号 ("") 定义字符串
        
    可以使用索引获取一个字符串中指定位置的字符，索引计数从 0 开始
    也可以使用 for循环遍历 字符串中的每个字符

常用操作：
    len(str) 获取字符串长度
    
    str1.count(str2) 小字符串在大字符串中出现的次数
    
    str1.index(str2)
    
    ... ...
    
切片操作
    切片使用索引值来限定范围，从一个大字符串中切出小字符串
    
    语法：
        字符串[开始索引:结束索引:步长]    
    



"""

str1 = "This is a 'test' demo"
print(str1)
print(str1[1])

for _ in str1:
    print(_)

print("---------------------------------------")

print("常用操作")
print(len(str1))

print(str1.count("st"))

print(str1.index("s"))
# 如果不存在会报错
# print(str1.index("ew"))

str_num = "01234567"
print(str_num)
print(str_num[1:3])
print(str_num[3:])
print(str_num[:3])
print(str_num[:])
print(str_num[::2])
print(str_num[1::2])
print(str_num[2:-1])
print(str_num[-2:])
print(str_num[-1::-1])
print(str_num[::-1])





