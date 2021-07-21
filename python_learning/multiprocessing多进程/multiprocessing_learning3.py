import multiprocessing as mp
import threading as td
import time

"""
多进程  和 多进程的对比

"""


# job 里面不能有返回值 需要放到queue中
def job(q):
    res = 0
    for i in range(100000):
        res += i + i ** 2 + i ** 3
    # queue
    q.put(res)

def multicore():
    q = mp.Queue()
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

def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i + i ** 2 + i ** 3
    # queue
    print("normal: ", res)

def multithread():
    q = mp.Queue()
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print("multithread: ", res1 + res2)

if __name__ == "__main__":
    st = time.time()
    normal()
    st1 = time.time()
    print("normal time: ",st1-st)
    multithread()
    st2 = time.time()
    print("multithread time: ", st2 - st1)
    multicore()
    print("multcore time: ", time.time() - st2)













