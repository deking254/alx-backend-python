#!/usr/bin/env python3
"""list of floats and annotations"""
from typing import List
def sum_list(input_list:List[float]) -> float:
    """returns the sum of the floats in the list of floats passed"""
    a:float = 0.0
    for value in input_list:
        a = a + value;
    return a
