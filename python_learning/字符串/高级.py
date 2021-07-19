
'''

%百分号模式

'''

name = "Bob"

print("My name is " + name + "!")
print("My name is %s!" % name)


"""
方式	意思
%d	整数
%i	整数
%f	小数
%s	字符

"""

age = 18
gender = "male"
print("My name is %(nm)s ! and my age is %(age)d, I am %(gd)s" % {"nm": name, "age": age, "gd": gender})

height = 1.8
print("My name is %s! and I am %d years old. I'm %0.2f height" % (name, age, height))


"""
format 方式格式化字符串
"""
print("我的名字是 {} !我 {} 岁了，我 {} 米高~".format(name, age, height))

print("我的名字是 {0} !我 {1} 岁了，我 {2} 米高~我是{0}".format(name, age, height))




print("%f" % (1/3))     # 后面不限制
print("%.2f" % (1/3))   # 后面限制 2 个位置
print("%4d" % (1/3))    # 前面补全最大 4 个位置
print("%5d" % 12)       # 前面补全最大 5 个位置

print("我 {:.3f} 米高".format(1.12345))
print("我 {ht:.1f} 米高".format(ht=1.12345))
print("我 {:3d} 米高".format(1))
print("我 {:3d} 米高".format(21))

"""

方式	    意思
:,	    每 3 个 0 就用逗号隔开，比如 1,000
:b	    该数字的二进制
:d	    整数型
:f	    小数模式
:%	    百分比模式

"""
txt = "You scored {:%}"
print(txt.format(2.1234))

txt = "You scored {:.2%}"
print(txt.format(2.1234))

"""
f格式化字符串 
"""

print(f"我的名字是 {name} !我 {age} 岁了，我 {height} 米高~")

print(f"我 {age} 岁了，明年我就{age + 1}岁了~")

score = 2.1234
print(f"You scored {score:.2%}")
print(f"You scored {score:.3f}")
print(f"You scored {12:5d}")

"""

修改字符串

方式	        意思
strip	    去除两端的空白符
replace	    替换字符
lower	    全部做小写处理
upper	    全部做大写处理
title	    仅开头的字母大写
split	    按要求分割
join	    按要求合并
startswith	判断是否为某字段开头
endswith	判断是否为某字段结尾

"""

print("  我不想要前后的空白，但是  中间\n的可以有\n  ".strip())


print("帮我替换掉莫烦".replace("莫烦", "沫凡"))

print("How ABOUT lower CaSe?".lower())
print("And upper CaSe?".upper())
print("do tiTle For me".title())

print("你|帮|我|拆分|一下|这句话".split("|"))
print("|".join(["你","帮", "我", "重组", "一下", "这句话"]))

print("我在街头看到你".startswith("我在"))
print("我在街头看到你".startswith("街头"))
print("我在巷尾看到你".endswith("看到你"))
print("我在巷尾看到你".endswith("巷尾"))

