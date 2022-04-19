import requests


def buscar_avatar(usuario):
    """
    Buscar o avatar de um usuário no Github
    :param usuario:str com o nome de usuário no Github
    :return: str com link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']

