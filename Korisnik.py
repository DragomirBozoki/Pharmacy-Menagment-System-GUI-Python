from datetime import datetime
from pickle import *

class Korisnik:

    def __init__(self, jmbg, ime, prezime, datum):
        self.__jmbg = jmbg
        self.__ime = ime
        self.__prezime = prezime
        self.__datum = datum


    @property
    def jmbg(self):
        return self.__jmbg

    @jmbg.setter
    def jmbg(self, jmbg):
        self.__jmbg = jmbg

    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def ime(self, ime):
        self.__ime = ime

    @property
    def prezime(self):
        return self.__prezime

    @prezime.setter
    def prezime(self, prezime):
        self.__prezime = prezime

    @property
    def datum(self):
        return self.__datum

    @datum.setter
    def datum(self, datum):
        self.__datum = datum

    def __str__(self):
            format_linije = "{}"
            return "\n".join([
                "",
                format_linije.format( self.__jmbg),
                format_linije.format( self.__ime), format_linije.format( self.__prezime),
                format_linije.format( self.__datum)
            ])

    @classmethod
    def prikazi_korisnike(cls, korisnici):
        format_linije = "{:13} {:10} {:10} {:13}"
        print()

        print(format_linije.format("JMBG", "Ime", "Prezime", "God. rodjenja"))
        print(format_linije.format("-" * 13, "-" * 10, "-" * 10, "-" * 13))

        for korisnik in korisnici:
            print(format_linije.format(
                korisnik.__jmbg,
                korisnik.__ime,
                korisnik.__prezime,
                korisnik.__datum

            ))






if __name__ == '__main__':

    korisnik1 = Korisnik("0609001800034", "Dragomir", "Bozoki", 2001)
    print(korisnik1)

    korisnici = [
        korisnik1
    ]

    print("")
    print("=================================")
    print("")
    Korisnik.prikazi_korisnike(korisnici)





