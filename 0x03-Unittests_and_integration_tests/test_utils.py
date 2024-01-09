#!/usr/bin/env python3
"""testing the utitls file"""
from unittest import mock, TestCase
import utils
import requests
from parameterized import parameterized
from typing import (
                    Callable,
                    Mapping,
                    Sequence,
                    Any
                   )

class TestAccessNestedMap(TestCase):
    """
    implements methods to check
    utils.access_nested_map is working as expected
    """
    @parameterized.expand([({"a": 1}, ("a",), 1), ({"a": {"b": 2}}, ("a",), {"b": 2}), ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: Any) -> Any:
        """checks the input for validity"""
        actual = utils.access_nested_map(nested_map, path)
        TestCase.assertEqual(self, actual, expected)
    
    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """testing if it raises a key error"""
        self.assertRaises(KeyError)
    

class TestGetJson(TestCase):
    """
    implements a get_json test"""
    @parameterized.expand([(("http://example.com"), {"payload": True}),(('http://holberton.io'), {"payload": False})])
    def test_get_json(self, value, expected):
        """testing for validity of get_json"""
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.json = lambda : expected
            result = utils.get_json(value)
            mock_get.assert_called_once_with(value)
            self.assertEqual(expected, result)
TestGetJson().test_get_json_0_http_example_com()
