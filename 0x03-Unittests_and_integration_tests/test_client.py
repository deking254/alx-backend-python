#!/usr/bin/env python3
"""this is a module with a series of tests relatig to client side"""
from unittest import TestCase, mock, main
from parameterized import parameterized
import client


class TestGithubOrgClient(TestCase):
    """testing the that the githuborgclient works as expected"""
    @parameterized.expand(
            [(('google'), 'https://api.github.com/orgs/google'),
                (('abc'), 'https://api.github.com/orgs/abc')])
    def test_org(self, company, expected_url):
        """testing the org function in client file"""
        with mock.patch('client.get_json') as mock_org:
            client_instance = client.GithubOrgClient(company)
            a = client_instance.org
            mock_org.assert_called_once_with(expected_url)
if __name__ == '__main__':
    main()
