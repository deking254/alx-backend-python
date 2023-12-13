#!/usr/bin/env python3
"""creating four parallel comprehensions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """execute async_comprehension four times in parallel"""
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    stop_time = time.perf_counter()
    return stop_time - start_time
