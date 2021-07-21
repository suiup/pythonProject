import multiprocessing as mp


"""
多进程  Queue
    把每个核运算出来的结果放到队列当中，所有进程运算完了之后，再从队列中取出结果进行继续加载运算
    
"""

# job 里面不能有返回值 需要放到queue中
def job(q):
    res = 0
    for i in range(1000):
        res += i + i**2 + i**3
    # queue
    q.put(res)

if __name__ == "__main__":
    q = mp.Queue()
    # 需要在 main 中调用才行  如果args 里边只有一个值，需要在参数后边加一个逗号，说明这是一个可以迭代的值，之后可能还会输入别的
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1)
    print(res2)












