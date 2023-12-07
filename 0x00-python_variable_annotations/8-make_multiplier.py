#!/usr/bin/env python3
"""more complex functions and annotations"""
from typing import Callable


def multiply(c: float):
    """the function to return"""
    return c ** 2


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float and by multiplier in arg"""
    b: Callable = multiply
    return b
