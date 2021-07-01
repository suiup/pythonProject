print("元组")

"""
元组的元素不能修改
    元组： 表示多个元组组成的序列
    用 () 定义
    索引从0开始
    
    元组可以保存不同类型的数据
    
应用场景：
    函数的参数或者返回值
    格式字符串： 格式化字符串后面的 () 本质上就是元组
    保护列表的数据安全    


元组和列表之间的转换

    list(tuple)
    
    tuple(list)


"""

info_tuple = ("Rose",18, 1.80 )
print(type(info_tuple))

# 获取数据
print(info_tuple[0])

# 空元组
empty_tuple = ()

# 只有一个元素的元组 需要加一个逗号
single_tuple = (10,)

print(type(single_tuple))



"""
常用操作

    count 
    index

"""
demo_tuple = ("Rose",18, 1.80, "Rose")

# 取值和索引
print(demo_tuple[0])
print(demo_tuple.index(18))

# 统计计数
print(demo_tuple.count("Rose"))

print(len(demo_tuple))


for _ in demo_tuple:
    print(_)



print_tuple = ("Rose",18, 1.80)
print("name is %s age is %d height is %.2f " % print_tuple)

print_str = "name is %s age is %d height is %.2f " % print_tuple
print(print_str)




