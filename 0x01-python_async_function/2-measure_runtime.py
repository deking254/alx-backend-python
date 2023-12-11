#!/usr/bin/env python3
"""measuring  the time it takes to excecute a coroutine"""
wait_n = __import__('1-concurrent_coroutines').wait_n
import time
import asyncio

def measure_time(n: int, max_delay: int) ->float:
    """returns a float that reps time of excecution"""
    start_time: float = time.perf_counter()
    asyncio.run(wait_n(n,  max_delay))
    end_time: float = time.perf_counter()
    return (end_time - start_time) / n
