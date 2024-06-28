import asyncio
import time

import aiofiles


async def read_file(filename):
    async with aiofiles.open(filename, mode='r') as file:
        contents = await file.read()
    print(contents)


async def aiofiles_method():
    start_time = time.time()
    await read_file('temp.txt')
    end_time = time.time()
    print('aiofiles_method task took: {}'.format(end_time - start_time))


def builtins_read_file(filename):
    with open(filename, mode='r') as file:
        contents = file.read()
    print(contents)


def builtins_method():
    start_time = time.time()
    builtins_read_file('temp.txt')
    end_time = time.time()
    print('builtins_method task took: {}'.format(end_time - start_time))


if __name__ == '__main__':
    asyncio.run(aiofiles_method())

    builtins_method()
