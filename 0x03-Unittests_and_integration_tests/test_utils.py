#!/usr/bin/env python3
"""testing the utitls file"""
import unittest
import utils
from typing import (
                    Callable,
                    Mapping,
                    Sequence,
                    Any
                   )


def parameterized(method: Callable) -> Callable:
    """checks for th inputs validity"""
    def expand(self, nested_map, path) -> Any:
        """extends the inputs"""
        map(unittest.TestCase.assertEqual, nested_map, path)
    return expand


class TestAccessNestedMap(unittest.TestCase):
    """
    implements methods to check
    utils.access_nested_map is working as expected
    """
    @parameterized.expand
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence) -> Any:
        """checks the input for validity"""
