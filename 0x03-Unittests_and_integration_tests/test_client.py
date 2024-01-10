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
        with mock.patch('client.get_json', return_value = {"repos_url": expected_url}) as mock_get_json:
            client_instance = client.GithubOrgClient(company)
            client_instance.org
            mock_get_json.assert_called_once_with(expected_url)
    def test_public_repos_url(self):
        """method to unit-test GithubOrgClient._public_url"""
        with mock.patch('client.GithubOrgClient.org', new_callable=mock.PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "google.your"}
            a = client.GithubOrgClient('google')._public_repos_url
            self.assertEqual(a, "google.your")

if __name__ == '__main__':
    main()
