#!/usr/bin/env python3
"""testing the utitls file"""
import unittest
import utils
from parameterized import parameterized
from typing import (
                    Callable,
                    Mapping,
                    Sequence,
                    Any
                   )

class TestAccessNestedMap(unittest.TestCase):
    """
    implements methods to check
    utils.access_nested_map is working as expected
    """
    @parameterized.expand([({"a": 1}, ("a",), 1), ({"a": {"b": 2}}, ("a",), {"b": 2}), ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: Any) -> Any:
        """checks the input for validity"""
        actual = utils.access_nested_map(nested_map, path)
        unittest.TestCase.assertEqual(self, actual, expected)
