"""
定义生成器类

用一个 class 也是可以表示一个迭代器，生成器的。 如果我们将上面的逻辑转化成 class，
    这个 class 可能相对比较复杂，但是也意味着你可以有更多设置和控制发生在这个 class 里面。
    里面我们申明了用于生成器的两个 method，__iter__ 和 __next__。

__iter__ 的意思是，当我在外面 for 循环进行迭代时，我返回什么？在下面例子中，我就把自己这个 class 本身返回回去，
    继续让自己做迭代就好了。

__next__ 的意思是每次迭代的时候，我的函数会放出来什么元素。
    下面的功能中实现的就是放出来一个被计算过的 item 元素。

"""

class NeedReturn:
    def __init__(self, init_value=0):
        self.tmp = init_value
        self.item = 0

    def __iter__(self): #在外面有for循环迭代的时候，返回什么
        print("This is in iter")
        return self

    def __next__(self): # 每次迭代的时候，我的函数会放出来什么元素。下面的功能中实现的就是放出来一个被计算过的 item 元素。
        while True:
            if self.item == self.tmp:
                self.tmp *= 2
                return self.item
            self.item += 1
            if self.item == 300:
                raise StopIteration

for i in NeedReturn(10):
    print(i)