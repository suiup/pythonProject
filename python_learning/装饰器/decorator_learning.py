def decorator(fn):
    def wrapper(name):
        print(name + " say I'm in") # 前处理
        return fn(name)
    return wrapper

@decorator
def outer_fn(name):
    print(name + " say I'm out")

outer_fn("bob")

print("---------------")

"""

我要对很多 function 做同样汉堡操作的时候，不如说验证一个用户有没有权限使用这个 function。 
有权限就在 wrapper 中调用 fn，没权限就跳出。

"""

def authorization(fn):
    def check_and_do(name):
        if name != "mofanpy":   # 鉴权
            print(name + " has no right!")
            return
        res = fn(name)
        return res
    return check_and_do

@authorization
def outer1(name):
    print(name+" outer1")

@authorization
def outer2(name):
    print(name+" outer2")

@authorization
def outer3(name):
    print(name+" outer3")

outer1("mofanpy")
outer2("morgan")
outer3("mofanpy")




