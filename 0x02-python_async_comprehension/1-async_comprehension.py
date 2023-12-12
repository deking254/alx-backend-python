#!/usr/bin/env python3
"""using async comprehension in this task"""
import asyncio
import random
from typing import AsyncIterator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> AsyncIterator:
    """collects 10 random numbers comprehense them and return them"""
    return [i async for i in async_generator()]
