from unittest.mock import Mock

from libpythonpro_fls import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'fabio1008', 'id': 83844802,
        'avatar_url': 'https://avatars.githubusercontent.com/u/83844802?v=4',
    }
    get_original=github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('fabio1008')
    assert 'https://avatars.githubusercontent.com/u/83844802?v=4' == url
    github_api.requests.get = get_original

def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('fabio')
    assert 'https://avatars.githubusercontent.com/u/83844802?v=4' == url