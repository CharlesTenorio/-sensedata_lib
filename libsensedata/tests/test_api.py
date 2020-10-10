from libsensedata.swapi import StarWarFactory


def test_api_retorna_personagen():
    fabrica = StarWarFactory()
    objeto = 'Personagens'
    request = fabrica.criar_ojb_stawar(objeto, 'people/')
    assert request.status_code == 200


def test_api_retorna_naves():
    fabrica = StarWarFactory()
    objeto = 'Naves'
    request = fabrica.criar_ojb_stawar(objeto, 'starships/')
    assert request.status_code == 200
