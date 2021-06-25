from Pacijent import Pacijent
from Datum_i_vreme import Datetime
from Lekar import Lekar
from Lek import Lek


class Recept:

    @property
    def pacijent(self):
        return Pacijent

    @pacijent.setter
    def pacijent(self, pacijent):
        self.__pacijent = pacijent

    @property
    def datum_i_vreme(self):
        return Datetime

    @datum_i_vreme.setter
    def datum_i_vreme(self, datum_i_vreme):
        self.__datum_i_vreme = Datetime

    @property
    def izvestaj(self):
        return self.__izvestaj

    @izvestaj.setter
    def izvestaj(self, izvestaj):
        self.__izvestaj = izvestaj

    @property
    def lekar(self):
        return Lekar

    @lekar.setter
    def lekar(self, lekar):
        self.__lekar = lekar

    @property
    def lek(self):
        return Lek

    @lek.setter
    def lek(self, lek):
        self.__lek = Lek

    @property
    def kolicina(self):
        return self.__kolicina

    @kolicina.setter
    def kolicina(self, kolicina):
        self.__kolicina = kolicina

    def _init_(self, pacijent, datum_i_vreme, izvestaj, lekar, lek, kolicina):
        self.__pacijent = pacijent
        self.__datum_i_vreme = datetime
        self.__izvestaj = izvestaj
        self.__lekar = lekar
        self.__lek = lek
        self.__kolicina = kolicina

    def _str_(self):
        format_linije = "{:15} {}"
        return "\n".join([
            "",
            format_linije.format("Pacijent: ", self.__pacijent),
            format_linije.format("Datum i vreme : ", self.__datum_i_vreme),
            format_linije.format("Izveštaj : ", self.__izvestaj),
            format_linije.format("Lekar: ", self.__lekar),
            format_linije.format("Lek: ", self.__lek),
            format_linije.format("Količina: ", self.__kolicina)
        ])


