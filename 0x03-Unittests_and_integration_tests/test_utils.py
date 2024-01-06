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
class parameterize():
    def expand(method) -> Any:
        """extends the inputsi"""
        def para(self, nested_map: Mapping, path: Sequence):
            for key in path:
                nested_map = nested_map[key]
            unittest.TestCase.assertEqual(nested_map, utils.access_nested_map(nested_map, path))
        return para

class TestAccessNestedMap(unittest.TestCase):
    """
    implements methods to check
    utils.access_nested_map is working as expected
    """
    @parameterize.expand
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence) -> Any:
        """checks the input for validity"""
        pass
