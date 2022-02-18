import pytest

from libpythonpro_fls.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['fabiocarini2003@gmail.com', 'cariniefabio@gmail.com']
)

def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'fabiocarini2003@gmail.com',
        'Curso PythonPro',
        'Turma Moacir Moda'
    )
    assert remetente in resultado

@pytest.mark.parametrize(
    'remetente',
    ['', 'fabio']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'fabiocarini2003@gmail.com',
            'Curso PythonPro',
            'Turma Moacir Moda'
        )
