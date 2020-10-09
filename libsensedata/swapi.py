import httpx

URL_API = 'https://swapi.dev/api/'


class Personagens(object):
    def __init__(self, num_paginas):
        self.url = URL_API
        self.paginacao = num_paginas

    def lista_todos_personagens(self):
        recurso = 'people/'
        url = self.url + recurso
        list_todos = httpx.get(url)
        return list_todos
