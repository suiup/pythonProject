"""
一个没有装饰器的方式

将 function 当成参数传入另一个function

"""
def decorator(fn, name):
    print(name+"say I'm in")    # 这是我的前处理
    return fn(name)

def outer_fn(name):
    print(name+"say I'm out")

decorator(outer_fn, "mofanpy")