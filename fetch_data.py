import time
import urllib.request
import asyncio
import aiohttp

URL = "https://api.github.com/events"
MAX_CLIENTS = 3


def fetch_sync(proc):
    print(f"Fetch sync {proc} process")


    start_time = time.time()
    response = urllib.request.urlopen(URL)
    datetime = response.getheader("Date")
    print(f"Process {proc}:  header: {datetime}; start_time: {start_time}")


    return datetime


def synchronous():
    start_time = time.time()
    print(f"start: {start_time}")
    for i in range(MAX_CLIENTS):
        fetch_sync(i)


def asynchronous():
    start_time = time.time()
    print(f"start: {start_time}")
    for i in range(MAX_CLIENTS):
        fetch_sync(i)

# fetch_sync("pro")
synchronous()
