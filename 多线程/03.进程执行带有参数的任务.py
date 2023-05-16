# 1.导入进程包
# import multiprocessing
# 2.使用进程类创建进程对象
# sub_process = multiprocess.Process(target=任务名)
# 3.使用进程对象启动进程执行指定任务
# sub_process.start()

# 1.导入进程包
import multiprocessing
import time

# 唱歌
def sing(num, name):
    for i in range(num):
        print(name)
        print("唱歌...")
        time.sleep(0.5)
# 跳舞
def dance(num, name):
    for i in range(num):
        print(name)
        print("跳舞...")
        time.sleep(0.5)

if __name__ == '__main__':
    # 2.使用进程类创建进程对象
    # target:指定进程执行的函数名
    # args: 使用元组方式给指定任务传参，元组的元素顺序就是参数的顺序
    # kwargs: 使用字典的方式给指定任务传参，key名字就是参数的名称
    sing_process = multiprocessing.Process(target=sing, args=(3, "小明"))
    dance_process = multiprocessing.Process(target=dance, kwargs={"name":"xiaoming", "num": 2})

    # 3.使用进程对象启动进程执行指定任务
    sing_process.start()
    dance_process.start()
