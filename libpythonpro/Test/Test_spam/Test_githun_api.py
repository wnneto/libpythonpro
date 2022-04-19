from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/100881405?v=4'
    resp_mock.json.return_value = {
        'login': 'wnneto', 'id': 100881405,
        'node_id': 'U_kgDOBgNT_Q',
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('wnneto')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('wnneto')
    assert 'https://avatars.githubusercontent.com/u/100881405?v=4' == url