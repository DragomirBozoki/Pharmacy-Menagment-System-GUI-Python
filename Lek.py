class Lek:

    @property
    def jkl(self):
        return self.__jkl

    @jkl.setter
    def jkl(self, jkl):
        self.__jkl = jkl

    @property
    def naziv(self):
        return self.__naziv

    @naziv.setter
    def naziv(self, naziv):
        self.__naziv = naziv

    @property
    def proizvodjac(self):
        return self.__proizvodjac

    @proizvodjac.setter
    def proizvodjac(self, proizvodjac):
        self.__proizvodjac = proizvodjac

    @property
    def tip_leka(self):
        return self.__tip_leka

    @tip_leka.setter
    def tip_leka(self, tip_leka):
        self.__tip_leka = tip_leka

    @naziv.setter
    def naziv(self, naziv):
        self.__naziv = naziv

    def __init__(self, jkl, naziv, proizvodjac, tip_leka):
        self.__jkl = jkl
        self.__naziv = naziv
        self.__tip_leka = tip_leka
        self.__proizvodjac = proizvodjac

    def __str__(self):
        format_linije = "{:15} {}"

        return "\n".join([
            format_linije.format("JKL:", self.__jkl),
            format_linije.format("Naziv: ", self.__naziv),
            format_linije.format("Tip Leka: ", self.__tip_leka),
            format_linije.format("Proizvodjac: ", self.__proizvodjac)
        ])



