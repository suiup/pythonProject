
"""
这几个方法都存在一个共性，我要对很多不同的 function 做同样的前后处理，这时，就是 Decorator 装饰器有用的时候了

"""

def inner_pre_fn(name):
    print(name+" say I'm in_pre")

def inner_post_fn(name):
    print(name+" say I'm in_post")

def outer_fn(name):
    inner_pre_fn(name)
    print(name+" say I'm out")
    inner_post_fn(name)

outer_fn("bob")