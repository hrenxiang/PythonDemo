import multiprocessing

# 定义一个共享整数
shared_value = multiprocessing.Value('i', 100)
count_lock = multiprocessing.Lock()


# CPU 密集型任务
def cpu_bound_task(n, shared_value, count_lock):
    while n > 0:
        with count_lock:
            shared_value.value -= 1
            n -= 1
    print(shared_value.value)


if __name__ == '__main__':
    num_processes = 5
    processes = []
    task_size = 100 // num_processes

    for _ in range(num_processes):
        p = multiprocessing.Process(target=cpu_bound_task, args=(task_size, shared_value, count_lock))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print('Final shared value:', shared_value.value)
