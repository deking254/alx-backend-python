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
    @parameterized.expand([({"a": 1}, ("a",)), ({"a": {"b": 2}},("a",)), ({"a": {"b": 2}},("a", "b"))])
    def test_access_nested_map(name, input, expected) -> Any:
        """checks the input for validity"""
        actual = utils.access_nested_map(input)
        unittest.TestCase.assertEqual(actual, expected)
