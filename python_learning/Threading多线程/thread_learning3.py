import threading
from queue import Queue
import time


"""
Thread Queue

    多线程的功能没有返回值，需要将运算出来的结果放在一个长的队列中，对每个线程的队列到主线程之后，拿出来，再进行运算

"""

def job(l, q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)

def multithreading():
    q = Queue()
    threads = []
    data = [[1,2,3],[3,4,5],[4,5,6],[5,6,7]]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)


if __name__ == '__main__':
    multithreading()