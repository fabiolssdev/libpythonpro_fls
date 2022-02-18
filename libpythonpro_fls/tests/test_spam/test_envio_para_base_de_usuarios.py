from unittest.mock import Mock

import pytest

from libpythonpro_fls.spam.enviador_de_email import Enviador
from libpythonpro_fls.spam.main import EnviadorDeSpam
from libpythonpro_fls.spam.models import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Fabio', email='fabiocarini2003@gmail.com'),
            Usuario(nome='Carini', email='cariniefabio@gmail.com')
        ],
        [
            Usuario(nome='Fabio', email='fabiocarini2003@gmail.com'),
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'fabiocarini2003@gmail.com',
        'Curso Phython Pro',
        'Confira os modulos fantasticos'
    )
    assert len(usuarios) == enviador.enviar.call_count

def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Fabio', email='fabiocarini2003@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'cariniefabio@gmail.com',
        'Curso Phython Pro',
        'Confira os modulos fantasticos'
    )
    enviador.enviar.assert_called_once_with(
        'cariniefabio@gmail.com',
        'fabiocarini2003@gmail.com',
        'Curso Phython Pro',
        'Confira os modulos fantasticos'
    )