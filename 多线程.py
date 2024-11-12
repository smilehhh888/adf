
from threading import Thread # 线程类


# 方法一：
# def func():
#     for i in range(1000):
#         print("func",i)
#
# if __name__ =='__main__':
#     t=Thread(target=func) # 创建线程，并给线程安排任务
#     t.start()# 多线程状态为可以开始工作状态，具体执行时间由cpu决定
#     for i in range(1000):
#         print("main",i)

def func(name):
    for i in range(1000):
        print(name,i)

if __name__ == '__main__':
    t1 = Thread(target=func,args=("线程1",)) # 传递参数必须是元组
    t1.start()
    t2 = Thread(target=func,args=("线程2",))
    t2.start()




# # 方法二：
# class MYThread(Thread):
#     def run(self):  # 固定的  ->当线程被执行的时候，被执行的就是run()
#         for i in range(1000):
#             print("子线程",i)
#
# if __name__ =='__main__':
#     t = MYThread()
#     # t.run()  # 方法的调用了 -> 单线程
#     t.start()  # 开启线程
#
#     for i in range(1000):
#         print("主线程",i)