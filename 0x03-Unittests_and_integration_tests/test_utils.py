#!/usr/bin/env python3
"""testing the utitls file"""
import unittest
import utils
import mock
import requests
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
    a = ({"a": 1}, ("a",), 1)
    b = ({"a": {"b": 2}}, ("a",), {"b": 2})
    c = ({"a": {"b": 2}}, ("a", "b"), 2)

    @parameterized.expand([a, b, c])
    def test_access_nested_map(s, n_map: Mapping, p: Sequence, r: Any) -> Any:
        """checks the input for validity"""
        s.assertEqual(s, utils.access_nested_map(nested_map, path), r)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence
                                         ) -> Any:
        """testing if it raises a key error"""
        self.assertRaises(KeyError)
