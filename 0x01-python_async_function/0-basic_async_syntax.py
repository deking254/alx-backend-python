#!/usr/bin/env python3
"""creates an asynchronous coroutine"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """a coroutine that returns a random number"""
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
