import multiprocessing
import time

def work():
    # 子进程工作2s
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)

if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)
    # 设置守护主进程，主进程退出后子进程直接销毁，不再执行子进程中的代码
    work_process.daemon = True
    work_process.start()

    # 主进程睡眠1s
    time.sleep(1)
    print("主进程执行完成....")
