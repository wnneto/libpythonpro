from libpythonpro.Spam.modelo import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Wilson', email='wn.nt3w@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Wilson', email='wn.nt3w@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
