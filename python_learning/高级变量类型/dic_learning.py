print("字典")

"""
字典
    可以用来存储多个数据
    
    可以存储无序的数据集合
    
    用 {} 定义
    
    使用键值对存储数据，键值对之间使用 "," 分隔    
    
    key value
    
    key 是索引
    value 是数据
    键和值之间用 : 分隔
    key 唯一
    value可以为任意的数据类型，但是key只能使用 字符串，数字或元组

应用场景
    描述一个物体的相关信息


常用操作：
    取值
    增加/修改
    删除
    
    len()
    
    update()
    
    clear()   


    
"""


dictionary_demo = {
    "name": "dic",
    "age": 10,
    "gender": "male",
    "show" : True
}

print(dictionary_demo)


# 取值
print(dictionary_demo["name"])

# 增加/修改
dictionary_demo["status"] = 0
dictionary_demo["name"] = "rose"
print(dictionary_demo)

# 删除
dictionary_demo.pop("name")
print(dictionary_demo)

# 统计键值对数量 len
print(len(dictionary_demo))

# 合并
temp_dic = {"height": 170}
dictionary_demo.update(temp_dic)
print(dictionary_demo)

# 清空
# dictionary_demo.clear()
# print(dictionary_demo)


"""
循环遍历
    for key in dic:
        print(key)


"""

for key in dictionary_demo:
    print("%s - %s" % (key, dictionary_demo[key]))
