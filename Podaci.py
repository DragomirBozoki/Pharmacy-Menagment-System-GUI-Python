from Lekar import Lekar
from Pacijent import Pacijent
from Lek import Lek
from Recept import Recept
import pickle

import traceback

class Podaci:

    @property
    def lekari(self):
        return self.__lekari

    @property
    def pacijenti(self):
        return self.__pacijenti

    @property
    def lekovi(self):
        return self.__lekovi

    @property
    def recepti(self):
        return self.__recepti

    def dodaj_pacijenta(self, pacijent):
        self.__pacijenti.append(pacijent)

    def obrisi_pacijenta(self, indeks):
        self.__pacijenti.pop(indeks)



    def obrisi_lekara(self, indeks):
        self.__lekari.pop(indeks)

    def obrisi_lek(self, indeks):
        self.__lekovi.pop(indeks)

    def obrisi_recept(self, indeks):
        self.__recepti.pop(indeks)

    def __init__(self):
        self.__lekari = []
        self.__pacijenti = []
        self.__lekovi = []
        self.__recepti = []


    __datoteka = "podaci.txt"

    @classmethod
    def sacuvaj(cls, podaci):
        try:
           datoteka = open(cls.__datoteka, "wb")
           pickle.dump(podaci, datoteka)
           datoteka.close()
        except OSError as e:
            print(traceback.format_exc(e))


    @classmethod
    def ucitaj(cls):
        try:
             datoteka = open(cls.__datoteka, "rb")
             podaci = pickle.load(datoteka)
             datoteka.close()

        except FileNotFoundError:
             return Podaci.napravi_pocetne()

        return podaci



def test():
    podaci = Podaci()

    lekari = podaci.lekari

    recepti = podaci.recepti




    pacijenti = podaci.pacijenti





    print("====Cuvanje=====")
    Podaci.sacuvaj(podaci)
    print("...")
    print("Done!")




if __name__ == '__main__':
    test()








