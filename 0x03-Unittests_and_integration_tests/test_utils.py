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

class parameterized():

    def expand(method) -> Any:
        """extends the inputsi"""
        def para(self, nested_map: Mapping, path: Sequence):
            """nitty gritty"""
            test1 = utils.access_nested_map({"a": 1}, ("a",))
            test2 = utils.access_nested_map({"a": {"b": 2}}, ("a",))
            test3 = utils.access_nested_map({"a": {"b": 2}}, ("a", "b"))
            unittest.TestCase.assertEqual(test1, 1)
            unittest.TestCase.assertEqual(test2, {"b": 2})
            unittest.TestCase.assertEqual(test3, 2)
    return para


class TestAccessNestedMap(unittest.TestCase):
    """
    implements methods to check
    utils.access_nested_map is working as expected
    """
    @parameterized.expand
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence
                               ) -> Any:
        """checks the input for validity"""
        pass
