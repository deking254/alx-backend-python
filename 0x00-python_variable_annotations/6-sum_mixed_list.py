#!/usr/bin/env python3
"""mixed lists and annotations"""

from typing import List, Union

def sum_mixed_list(mxd_lst:List[Union[int,float]]) -> float:
    """returns the sum of ints and floats in a list as float"""
    a:float = 0.0
    for value in mxd_lst:
        a = a + value
    return a;
