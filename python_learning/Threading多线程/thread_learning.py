import threading

"""
线程
多线程 Threading 是一种让程序拥有分身效果. 能同时处理多件事情. 
一般的程序只能从上到下一行行执行代码, 不过 多线程 (Threading) 就能打破这种限制. 让你的程序鲜活起来.

    开启线程
    查看当前线程
    线程个数

"""

def thread_job():
    print("This is an added thread, number is %s" % threading.current_thread())


def main():
    added_thread = threading.Thread(target=thread_job)
    added_thread.start()

    # 当前线程个数
    print(threading.active_count())
    # 当前的线程列表
    print(threading.enumerate())
    # 当前线程
    print(threading.currentThread())



if __name__ == '__main__':
    main()