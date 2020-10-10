from libsensedata.swapi import Personagens


def test_api_metodo_get():
    api_presonagem = Personagens(10)
    request = api_presonagem.lista_todos_personagens()
    assert request.status_code == 200
