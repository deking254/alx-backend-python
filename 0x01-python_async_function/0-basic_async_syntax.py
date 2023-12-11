#!/usr/bin/env python3
"""creates an asynchronous coroutine"""

import random
import asyncio


async def wait_random(max_delay=10) -> int:
    """a coroutine that returns a random number"""
    wait: int = random.random()
    if (wait <= max_delay):
        await asyncio.sleep(wait)
        return wait
