from libpythonpro_fls.spam.models import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Fabio', email='fabiocarini2003@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Fabio', email='fabiocarini2003@gmail.com'),
        Usuario(nome='Carini', email='cariniefabio@gmail.com')
        ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
