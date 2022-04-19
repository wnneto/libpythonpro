from unittest.mock import Mock

import pytest

from libpythonpro.Spam.Enviador.enviador_email import Enviador
from libpythonpro.Spam.main import EnviadorDeSpam
from libpythonpro.Spam.modelo import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
       [
        Usuario(nome='Wilson', email='wn.nt3w@gmail.com'),
        Usuario(nome='Karollyne', email='wnobreganeto@gmail.com')
        ],
        [
        Usuario(nome='Wilson', email='wn.nt3w@gmail.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'wn.nt3w@gmail.com',
        'Teste Spam',
        'Spam enviado corretamente'
    )
    assert len(usuarios) == enviador.enviar.call.count


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_paramentos_de_spam(sessao):
    usuario = Usuario(nome='Wilson', email='wn.nt3w@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'wnobreganeto@gmail.com',
        'Teste Spam',
        'Spam enviado corretamente'
    )
    enviador.enviar.assert_called_once_with(
        'wnobreganeto@gmail.com',
        'wn.nt3w@gmail.com',
        'Teste Spam',
        'Spam enviado corretamente'
    )
