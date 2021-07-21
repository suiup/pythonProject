import multiprocessing as mp

"""
多进程 进程池

"""

def job(x):
    return x * x


def multicore():
    # 在pool中有返回值 可以指定用到核的数量
    pool = mp.Pool(processes=3)
    res = pool.map(job,range(10))
    print(res)
    res = pool.apply_async(job,(2,))# 在一个进程中计算， 只能用一个值
    print(res.get())
    # 用迭代的方式 进行计算
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])


if __name__ == '__main__':
    multicore()