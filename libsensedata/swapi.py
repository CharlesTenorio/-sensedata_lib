import httpx
from abc import ABCMeta, abstractclassmethod

URL_BASE_API = 'https://swapi.dev/api/'


class UniversoStarWar(metaclass=ABCMeta):
    def __init__(self):
        self.url = URL_BASE_API
        self.num_pagina = 10

    @abstractclassmethod
    def retorna_lista(self, recurso):
        pass


class Personagens(UniversoStarWar):
    def retorna_lista(self, recurso):
        url = self.url + recurso
        list_personagen = httpx.get(url)
        return list_personagen


class Naves(UniversoStarWar):
    def retorna_lista(self, recurso):
        url = self.url + recurso
        list_naves = httpx.get(url)
        return list_naves


class StarWarFactory(object):
    def criar_ojb_stawar(self, object_type, recurso):
        return eval(object_type)().retorna_lista(recurso)
