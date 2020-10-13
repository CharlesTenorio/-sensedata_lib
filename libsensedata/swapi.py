import requests
from abc import ABCMeta, abstractclassmethod

URL_BASE_API = 'https://swapi.dev/api/'


class UniversoStarWar(metaclass=ABCMeta):
    def __init__(self):
        self.url = URL_BASE_API

    @abstractclassmethod
    def retorna_lista(self, recurso):
        pass


class Personagens(UniversoStarWar):
    def retorna_lista(self, recurso):
        url = self.url + recurso
        list_personagen = requests.get(url)
        return list_personagen


class Naves(UniversoStarWar):
    def retorna_lista(self, recurso):
        url = self.url + recurso
        list_naves = requests.get(url)
        return list_naves


class StarWarFactory(object):
    def criar_ojb_stawar(self, object_type, recurso):
        return eval(object_type)().retorna_lista(recurso)
