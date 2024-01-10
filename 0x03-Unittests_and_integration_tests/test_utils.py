#!/usr/bin/env python3
"""testing the utitls file and working out what is going on"""
from unittest import mock, TestCase, main
import utils
import requests
from utils import memoize
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
    @parameterized.expand(
            [({"a": 1}, ("a",), 1),
                ({"a": {"b": 2}}, ("a",), {"b": 2}),
                ({"a": {"b": 2}},
                    ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> Any:
        """checks the input for validity of the values returned"""
        actual = utils.access_nested_map(nested_map, path)
        TestCase.assertEqual(self, actual, expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """testing if it raises a key error when the wrong inputs are"""
        self.assertRaises(KeyError)


class TestGetJson(TestCase):
    """
    implements a get_json test"""
    @parameterized.expand(
            [(("http://example.com"), {"payload": True}),
                (('http://holberton.io'), {"payload": False})])
    def test_get_json(self, value, expected):
        """testing for validity of get_json"""
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.json = lambda: expected
            result = utils.get_json(value)
            mock_get.assert_called_once_with(value)
            self.assertEqual(expected, result)


class TestMemoize(TestCase):
    """testing the memoize decorator to see if it does what is intended"""
    def test_memoize(self) -> Any:
        """actual testing of the func to """
        class TestClass:
            """tests that the method to see that its called only once"""
            def a_method(self):
                """this class is just for testing"""
                return 42

            @memoize
            def a_property(self):
                """the property is returned"""
                return self.a_method()
        a = TestClass()
        with mock.patch.object(a, 'a_method', return_value=42) as e:
            value_a = a.a_property
            value_b = a.a_property
            self.assertEqual(42, value_a)
            self.assertEqual(42, value_b)
            e.assert_called_once()
