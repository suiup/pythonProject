import threading
import time

"""
线程 joint
    添加到主线程

"""

def thread_job():
    print("T1 start\n")

    for i in range(10):
        time.sleep(0.1)

    print("T1 finish\n")

def T2_job():
    print("T2 start \n")
    print("T2 finish\n")

def main():
    # 添加线程并命名
    added_thread = threading.Thread(target=thread_job, name="T1")
    thread2 = threading.Thread(target=T2_job, name="T2")
    # 开启线程
    added_thread.start()
    thread2.start()
    # 需要等待所有线程执行结束之后,再运行 join() 之后的语句
    added_thread.join()
    thread2.join() # join 添加到主线程上

    print("all done\n")



if __name__ == '__main__':
    main()