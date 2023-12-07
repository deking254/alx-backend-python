#!/usr/bin/env python3
"""more complex annotations using typevars"""

from typing import Mapping, Any, Union, T

def safely_get_value(dct:Mapping, key:Any, default:Union[T, None]) -> Union[Any, T]:
    """returns the either dct[key] or none"""
    if key in dct:
        return dct[key]
    else:
        return default
