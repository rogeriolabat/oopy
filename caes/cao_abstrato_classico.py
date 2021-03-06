# coding: utf-8

class CaoBase(object):
    qt_patas = 4
    carnivoro = True
    nervoso = False

    def __init__(self, nome):
        self.nome = nome

    def latir(self, vezes=1):
        raise NotImplementedError('responsabilidade da sub-classe')

    def detectar_intruso(self):
        self.latir()
        # mais alguma ação...

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Cao(%r)' % self.nome

    def __eq__(self, outro):
        return (isinstance(outro, Cao) and
            self.__dict__ == outro.__dict__)

class Cao(CaoBase):

    def latir(self, vezes=1):
        # quando nervoso, late o dobro
        vezes = vezes + (self.nervoso * vezes)
        print(self.nome + ':' + ' Au!' * vezes)


