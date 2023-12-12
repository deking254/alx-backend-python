#!/usr/bin/env python3
"""Creates coroutines by waiting 1 second 10 times"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """coroutine loops 10 times asynchronously wait 1
    second and return random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
