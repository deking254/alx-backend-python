#!/usr/bin/env python3
"""creates an asynchronous coroutine"""

import random
import asyncio
async def wait_random(max_delay=10):
    wait = random.random()
    if (wait <= max_delay):
        """await asyncio.wait_for(500, 5000)"""
        await asyncio.sleep(wait)
        return wait;
