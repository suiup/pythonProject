print("while 循环演练")

"""
语法：
    while 条件(判断 计数器 是否达到 目标次数):
        条件满足 xxx
        条件满足 xxx
        ... ...
        
        处理条件（计数器 + 1）
        
        
        
"""

i = 0
while i <= 5:
    print("Hello world")

    if i == 3:
        i = i + 1
        continue
    i= i + 1