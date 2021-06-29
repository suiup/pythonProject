print("变量格式化输出")
"""
%s 字符串
%d 有符号十进制整数，%06d 表示输出的整数显示位数，不足的地方用0补全
%f 浮点数， %.02f 表示小数点后只显示两位
%% 输出%

语法格式：
    print("格式化字符串" % 变量1)
    print("格式化字符串" % (变量1, 变量2...))

"""

color = "red"

print("this color is %s" % color)

number = 10

print("The number is %06d " % number)

price = 12.3
weight = 20.5
print("The price is %.2f, The weight is %.3f" % (price, weight))


scale = 0.25
print("The rate is %.2f%%" % (scale * 100))









