import concurrent.futures
import requests
import time


def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))
    return resp.headers


def download_all(sites):
    # 创建了一个线程池执行器 (ThreadPoolExecutor)，它会管理和调度多个线程来并发地执行任务。
    # 参数 max_workers=5 指定了线程池最多可以同时运行5个线程。
    # with 语句可以确保在代码块结束时，线程池被正确地关闭和清理
    with (concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor):
        # executor.submit 方法将 download_one 函数提交给线程池执行，并立即返回一个 Future 对象。
        to_do = [executor.submit(download_one, site) for site in sites]
        print(to_do)
        # concurrent.futures.as_completed 是一个生成器函数，
        # 它接收一个 Future 对象的迭代器，并在每个 Future 对象完成时，
        # 依次返回这些完成的 Future。这允许你以任意顺序处理这些完成的任务。
        for future in concurrent.futures.as_completed(to_do):
            result = future.result()
            print('Future Result: {}'.format(result))


def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        # 更多URL
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()
