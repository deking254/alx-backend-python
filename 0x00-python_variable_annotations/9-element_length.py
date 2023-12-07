#!/usr/bin/env python3
"""annotation task on a function"""
from typing import Iterable, Sequence, List, Tuple

def element_length(lst:Iterable[Sequence]) -> List[Tuple[(Sequence, int)]]:
    """returns whatever it returns"""
    return [(i, len(i)) for i in lst]
