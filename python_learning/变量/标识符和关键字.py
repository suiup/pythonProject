import keyword
print("标识符和关键字")


"""
标识符：
    标识符就是程序员定义的变量名、函数名
    名字需要有见名知义的效果
    
    可以由 字母、下划线和数字组成
    不能以数字开头
    不能与关键字重名
    
关键字
    就是在python 内部已经使用的标识符
    具有特有的功能和含义
    开发者不允许定义和关键字相同名字的标识符
    
    通过以下命令可以查看python 的关键字
    
        import keyword
        print(keyword.kwlist)
        

"""

print(keyword.kwlist)