from Korisnik import *


class Lekar(Korisnik):

    @property
    def specijalizacija(self):
        return self.__specijalizacija

    @specijalizacija.setter
    def specijalizacija(self, specijalizacija):
        self.__specijalizacija = specijalizacija


    def __init__(self, jmbg, ime, prezime, datum, specijalizacija):
        super().__init__(jmbg, ime, prezime, datum)
        self.__specijalizacija = specijalizacija

    def __str__(self):
        format_linije = "{:15} {}"
        return "\n".join([
            super().__str__(),
            format_linije.format("Specijalizacija", self.__specijalizacija)
        ])
    