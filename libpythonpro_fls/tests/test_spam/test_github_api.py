from unittest.mock import Mock

import pytest

from libpythonpro_fls import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/83844802?v=4'
    resp_mock.json.return_value = {
        'login': 'fabio1008', 'id': 83844802,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonpro_fls.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('fabio1008')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('fabio1008')
    assert 'https://avatars.githubusercontent.com/u/83844802?v=4' == url