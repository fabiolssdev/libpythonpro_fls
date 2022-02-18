from libpythonpro_fls import github_api


def test_buscar_avatar():
    url = github_api.buscar_avatar('fabio1008')
    assert 'https://avatars.githubusercontent.com/u/83844802?v=4' == url