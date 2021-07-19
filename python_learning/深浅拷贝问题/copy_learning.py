
"""
复制地址和复制值的问题

"""

l = [1,2,3]
_l = l.copy()
_l[0] = -1
print(_l)
print(l)

m = [[1],[2],3]
_m = m.copy()
_m[0][0] = -1
print(_m)
print(m)


"""
deep copy and shallow copy

Deep copy 就是我们通常意义上的复制，把东西全部再造了一遍，彻底成为了两个独立的个体。 

而 Shallow Copy, 其实也有一点影子拷贝的意思，我复制出来的是你的一个影子，一个投影成像。 所以真实的实体是没有被复制的，我只复制了这个实体的一个投影而已。

列表中直接存放的数值，字符，和存 class 实例，列表，字典不同。 对数值字符的复制，直接是复制的值，而不是一个投影。


Python 自带了一个 copy 的库，里面就有一个 deepcopy，用这个你就能实现完全的深拷贝


"""


from copy import deepcopy
l = [[1],[2],3]
_l = deepcopy(l)
_l[0][0] = -1
print(_l)
print(l)



