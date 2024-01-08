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
    @parameterized.expand([('http://example.com', {"payload": True}),('http://holberton.io', {"payload": False})])
    def test_get_json(self, url, expected):
        """
        test that utils.get_json returns the expected result
        """
        result = None

        def json_func():
            return expected
        with unittest.mock.patch('requests.get') as e:
            e.return_value.json = json_func
            result = utils.get_json(url)
        self.assertEqual(result, expected)
        e.assert_called_once_with(url)
