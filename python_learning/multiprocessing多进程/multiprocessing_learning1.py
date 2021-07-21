import multiprocessing as mp
import threading as td

"""
多进程  多核运算
    我们在多线程 (Threading) 里提到过, 它是有劣势的, GIL 让它没能更有效率的处理一些分摊的任务.
    而现在的电脑大部分配备了多核处理器, 多进程 Multiprocessing 能让电脑更有效率的分配任务给每一个处理器,
    这种做法解决了多线程的弊端. 也能很好的提升效率.

"""

def job(a,b):
    print("a")

if __name__ == "__main__":
    # 需要在 main 中调用才行
    p1 = mp.Process(target=job, args=(1, 2))
    p1.start()
    p1.join()








