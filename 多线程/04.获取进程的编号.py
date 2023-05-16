# 导包： import os
# 获取当前进程pid： os.getpid（）
# 获取父进程pid： os.getppid（）


# 1.导入进程包
import multiprocessing
import time
import os
# 唱歌
def sing(num, name):
    print("唱歌进程的父进程pid：", os.getppid())
    print("唱歌进程的pid：", os.getpid())
    for i in range(num):
        print(name)
        print("唱歌...")
        time.sleep(0.5)
# 跳舞
def dance(num, name):
    print("跳舞进程的父进程pid：", os.getppid())
    print("跳舞进程的pid：", os.getpid())
    for i in range(num):
        print(name)
        print("跳舞...")
        time.sleep(0.5)

if __name__ == '__main__':
    print("主进程的pid:", os.getpid())
    # 2.使用进程类创建进程对象
    # target:指定进程执行的函数名
    # args: 使用元组方式给指定任务传参，元组的元素顺序就是参数的顺序
    # kwargs: 使用字典的方式给指定任务传参，key名字就是参数的名称
    sing_process = multiprocessing.Process(target=sing, args=(3, "小明"))
    dance_process = multiprocessing.Process(target=dance, kwargs={"name":"xiaoming", "num": 2})

    # 3.使用进程对象启动进程执行指定任务
    sing_process.start()
    dance_process.start()
