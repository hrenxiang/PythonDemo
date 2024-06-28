import threading
import time
import multiprocessing

count = 10000000
count_lock = threading.Lock()


# CPU 密集型任务
def cpu_bound_task(n):
    global count
    if count == 0:
        count = 10000000
    print(count)
    while n > 0:
        with count_lock:
            count -= 1
            n -= 1
    else:
        print(count)


# I/O 密集型任务
def io_bound_task(n):
    while n > 0:
        with open('temp.txt', 'a') as f:
            f.write('Hello, world!\n')
        n -= 1


# 测试 CPU 密集型任务(多线程)
def test_cpu_bound(thread_num):
    start_time = time.time()
    threads = [threading.Thread(target=cpu_bound_task, args=(10000000 / thread_num,)) for _ in range(thread_num)]
    print(threads)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print('CPU bound task took:', time.time() - start_time)


# 测试 CPU 密集型任务(多进程)
def test_cpu_bound_multiprocess(processNum):
    start_time = time.time()
    processes = [multiprocessing.Process(target=cpu_bound_task, args=(10000000 / processNum,)) for _ in
                 range(processNum)]
    print(processes)
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    print('CPU bound Multi-process task took:', time.time() - start_time)


# 测试 I/O 密集型任务
def test_io_bound():
    start_time = time.time()
    threads = [threading.Thread(target=io_bound_task, args=(1000,)) for _ in range(5)]
    print(threads)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("""I/O bound task took: %.8f, threadNum=%d""" % (time.time() - start_time, 5))


if __name__ == '__main__':
    # 单进程
    start_time = time.time()
    cpu_bound_task(10000000)
    print('Single process took:', time.time() - start_time)

    test_cpu_bound(1)
    test_cpu_bound(5)
    test_cpu_bound_multiprocess(1)
    test_cpu_bound_multiprocess(5)
    test_io_bound()
