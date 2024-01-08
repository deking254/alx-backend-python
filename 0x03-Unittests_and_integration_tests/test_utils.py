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
                    Any,
                    Text
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

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """testing if it raises a key error"""
        self.assertRaises(KeyError)

class TestGetJson(unittest.TestCase):
    """
    implements the methods to check
    utils.utils.get_json function
    """
    def tiest_get_json(self, mock_get):
        """
        test that utils.get_json returns the expected result
        """

        
