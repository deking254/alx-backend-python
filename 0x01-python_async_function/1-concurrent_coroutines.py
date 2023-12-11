#!/usr/bin/env python3
"""creating multiple coroutines"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """the coroutine for execute multiple coroutines"""
    futures = []
    list_delays = []
    for _ in range(n):
        futures.append(wait_random(max_delay))
    futures = asyncio.as_completed(futures)
    for future in futures:
        list_delays.append(await future)
    return list_delays
