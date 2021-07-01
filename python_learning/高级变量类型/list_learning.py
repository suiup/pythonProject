print("列表")

"""

ctrl + q  / ctrl + p 提示

用于存储一串信息
列表用[]定义，在数据之间用 "," 分隔
索引从0开始, 如果超出索引会报错

可以存储不同类型的数据

一般都存储相同类型的数据


常用操作

    增 
    删 
    查
    len() 列表长度    
    count() 统计列表中某一个数据出现的次数

del 关键字，从内存中将变量删除，后面的代码就不能使用这个变量了

"""

list = ["a", "b", "c"]

print(list)
# 取值
print(list[0])

# 取索引
print(list.index("b"))

# 在列表末尾增加数据
list.append("d")
print(list)
# 插入数据
list.insert(1, "insert")
print(list)

# 加入列表
temp_list = ["e","f","g"]

list.extend(temp_list)
print(list)


# 删除第一次出现的数据
list.remove("a")
print(list)
# 删除最后一个元素
list.pop()
print(list)
# 指定索引进行删除
list.pop(0)
print(list)

# 删除所有
# list.clear()
# print(list)


# 用关键字删除列表中元素  del   本质为将一个变量从内存中删除
del list[0]
print(list)


print(len(list))

print(list.count("c"))


"""
列表排序

sort

reverse

"""
num_list = [2,3,4,1,7,3,4,5]
# 升序
num_list.sort()
print(num_list)

# 降序
num_list.sort(reverse=True)
print(num_list)


# 反转
num_list.reverse()
print(num_list)

"""
循环遍历

for i in range(10):
    print(i)
"""

for _ in num_list:
    print(_)






