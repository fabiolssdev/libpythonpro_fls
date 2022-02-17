from libpythonpro_fls.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'fabiocarini2003@gmail.com',
        'cariniefabio@gmail.com',
        'Curso PythonPro',
        'Turma Moacir Moda'
   )
    assert 'fabiocarini2003@gmail.com' in resultado
