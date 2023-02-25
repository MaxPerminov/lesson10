import asyncio
from asyncio import sleep


async def running():
    print("First line of execution(1)")
    await sleep(3)
    print("Second line of execution(1)")


async def running2():
    print("First line of execution(2)")
    await sleep(2)
    print("Second line of execution(2)")


async def running3():
    print("First line of execution(3)")
    await sleep(1)
    print("Second line of execution(3)")


ioLoop = asyncio.get_event_loop()
tasks = [
    ioLoop.create_task(running()),
    ioLoop.create_task(running2()),
    ioLoop.create_task(running3())
]
wait_tasks = asyncio.wait(tasks)
ioLoop.run_until_complete(wait_tasks)
ioLoop.close()
