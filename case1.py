from AsyncExecutionTime import AsyncExecutionTime
import asyncio
import time


def sync_api(n: int):
    time.sleep(1)
    print(f"sync_api {n} Finished")


async def async_api(n: int):
    await asyncio.sleep(1)
    print(f"async_api {n} Finished")


@AsyncExecutionTime("Main")
async def main1():
    for i in range(10):
        sync_api(i)


@AsyncExecutionTime("Main")
async def main2():
    for i in range(10):
        await async_api(i)


@AsyncExecutionTime("Main")
async def main3():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.create_task(async_api(i)))
    await asyncio.gather(*tasks)


@AsyncExecutionTime("Main")
async def main4():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.create_task(async_api(i)))
    for task in tasks:
        await task

# asyncio.run(main1())
# asyncio.run(main2())
# asyncio.run(main3())
asyncio.run(main4())
