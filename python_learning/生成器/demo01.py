"""
拿到合适的才进入下一轮
这种需要先保存一个 items 的列表，但当你做机器学习或者数据处理的时候，
如果这个 items 列表的数据量很大，就会非常占内存。

所以生成器的一个重要目的就是避免在内存中记录这样的一个大数据，避免把内存撑爆
"""

items = []  # 假设这里在记录一个很大的列表
for item in range(5):
    if item % 2 == 0:
        items.append(item)

for i in items:
    print(i)

"""
我只在需要这个数据的时候生成它，生成完了我就不用了，也不需要记录。这种时候将会节约我很多内存的需求
"""

def need_return():
    for item in range(5):
        if item % 2 == 0:
            print("我要扔出去一个 item=%d 了" % item)
            yield item  # 这里就会返回给下面的 for 循环
            print("我又回到里面了")

for i in need_return():
    print("我在外面接到了一个 item=%d\n" % i)


"""
我能在主循环里拿到什么，其实是由 need_return 生成器决定的。

所以 need_return 可以是一个很复杂的功能。 比如下面这个，我往外扔什么数字，是取决于我内部的一个特殊运算的。
"""
def need_return02():
    tmp = 2
    for item in range(300):
        if item == tmp:
            tmp *= item
            yield tmp

for i in need_return02():
    print(i)

print("-----------------------------")

def need_return(init_value):
    tmp = init_value
    for item in range(300):
        if item == tmp:
            tmp *= 2
            yield item

for i in need_return(20):
    print(i)


