from Pacijent import Pacijent
from Lek import Lek
from Lekar import Lekar
from datetime import datetime
import uuid

class Recept():

    @property
    def Pacijent(self):
        return self.__pacijent

    @property
    def datum(self):
        return self.__datum

    @property
    def Lekar(self):
        return self.__lekar

    @property
    def Lek(self):
        return self.__lek

    @property
    def izvestaj(self):
        return self.__izvestaj

    @property
    def kolicina(self):
        return self.__kolicina

    def sadrzi(self, pacijent):
        return pacijent in self.__pacijent


    def __init__(self,Pacijent, Lek, Lekar, datum, kolicina):
        self.__pacijent = Pacijent
        self.__datum = datum
        self.__lekar = Lekar
        self.__lek = Lek
        self.__izvestaj = uuid.uuid4()
        self.__kolicina = kolicina

    def __str__(self):
        format_linije = "{:13}: {}"

        return "\n".join([
            "",
            format_linije.format("Pacijent", self.__pacijent),
            format_linije.format("Lek:", self.__lek),
            format_linije.format("Lekar:", self.__lekar),
            format_linije.format("Datum:", self.__datum),
            format_linije.format("Izvestaj: ", self.__izvestaj),
            format_linije.format("Kolicina", self.__kolicina, " mg")

        ])