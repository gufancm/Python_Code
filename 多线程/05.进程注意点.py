import multiprocessing
import time

def work():
    # 子进程工作2s
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)

if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)
    work_process.start()

    # 主进程睡眠1s
    time.sleep(1)
    print("主进程执行完成....")
