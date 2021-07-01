print("函数")
"""
函数，就是把 具有独立功能的代码块 组织为一个小模块，在需要的时候调用

函数使用分两步：
    定义函数： 封装独立的功能
    调用函数： 享受封装的成果

语法：
    def 函数名():
        代码
        ... ...


"""


def print_add(num1, num2):
    print(num1 + num2)
    print("add")
    return num1 + num2

result = print_add(10, 20)
print("result: ", result)


def print_line(char):
    print(char * 50)


print_line("a")
