from Korisnik import *


class Pacijent(Korisnik):

    @property
    def lbo(self):
        return self.__lbo

    @lbo.setter
    def lbo(self, lbo):
        self.__lbo = lbo

    def __init__(self, jmbg, ime, prezime, datum, lbo):
        super().__init__(jmbg, ime, prezime, datum)
        self.__lbo = lbo

    def __str__(self):
        format_linije = "{}"

        return "\n".join([
            " ",
            super().__str__()+"\t",
            format_linije.format( self.__lbo),

        ])

def test():

    pacijent1 = Pacijent("0906001800034", "Dragomir", "Bozoki","5,10.2001.", "1234567")

    pacijenti = []

  

test()