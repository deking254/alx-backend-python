#!/usr/bin/env python3
"""multiple possible annotations for a variable"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns tuple with k and square of v as float"""
    return tuple((k, v**2))
