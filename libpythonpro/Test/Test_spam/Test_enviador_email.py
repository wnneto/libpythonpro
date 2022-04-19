from libpythonpro.Spam.Enviador.enviador_email import Enviador, EmailInvalido
import pytest

def test_enviador_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['wn.nt3w@gmail.com', 'wnobreganeto@gmail.com']
)

def test_enviador(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'wn.nt3w@gmail.com',
        'Teste',
        'Corpo do Teste'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'wnobreganeto']
)

def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'wn.nt3w@gmail.com',
            'Teste',
            'Corpo do Teste'
        )