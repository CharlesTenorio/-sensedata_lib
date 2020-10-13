from libsensedata.swapi import StarWarFactory
from operator import itemgetter

fabrica = StarWarFactory()
nave = 'Naves'
paneta = 'Planeta'

lista_de_naves = fabrica.criar_ojb_stawar(nave, 'starships/')


class PersonagenStarwa(object):
    def __init__(self):
        self.personagen = 'Personagens'  # nome da classe
        self.recurso = 'people/'
        self.lista_personagen = fabrica.criar_ojb_stawar(self.personagen,
                                                         self.recurso)
        self.personagens = dict(self.lista_personagen.json())
        self.lista = self.personagens['results']

    def ordenar(self, campo):
        lista_ordenada = sorted(self.lista, key=itemgetter(campo))
        return lista_ordenada

    def buscar(self, campo, busca):
        personagem_filter = list(filter(lambda p: p[campo] in p[busca],
                                        self.lista))
        return personagem_filter
