#!/usr/bin/env python3
"""deals with advanced tasks in the asyncio module"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """the coroutine for execute multiple coroutines"""
    futures = []
    list_delays = []
    for _ in range(n):
        futures.append(task_wait_random(max_delay))
    futures = asyncio.as_completed(futures)
    for future in futures:
        list_delays.append(await future)
    return list_delays
