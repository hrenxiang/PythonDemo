import time


def crawl_page(url):
    print('Crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))


# def main(urls):
#     for url in urls:
#         crawl_page(url)
#
#
# if __name__ == "__main__":
#     start_time = time.time()  # 开始计时
#     main(['url_1', 'url2_1', 'url3_1', 'url4_1'])
#     end_time = time.time()  # 结束计时
#     # {:.2f} 是 Python 格式化字符串的方法之一，用于控制浮点数的显示格式。具体来说：
#     print("总耗时: {:.2f} 秒".format(end_time - start_time))

# ============================================================================================


import asyncio


async def crawl_page2(url):
    print('Crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


# async def main(urls):
#     for url in urls:
#         await crawl_page2(url)

async def main(urls):
    tasks = [asyncio.create_task(crawl_page2(url)) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.time()  # 开始计时
    asyncio.run(main(['url_1', 'url2_1', 'url3_1', 'url4_1']))
    end_time = time.time()  # 结束计时
    print("总耗时: {:.2f} 秒".format(end_time - start_time))
