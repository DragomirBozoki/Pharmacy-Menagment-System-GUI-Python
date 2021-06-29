import time
from tkinter import *
import tkinter.messagebox
from Podaci import *
from tkinter.ttk import Combobox


def main():

    root = Tk()
    app = windows1(root)
    root.mainloop()

class windows1:


    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Menagment System")
        self.master.geometry("1350x800+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.master.configure(bg = "white smoke")
        self.frame.configure(bg = "white smoke")

        self.LabelTitle = Label(self.frame,bg = "whitesmoke", text = "Pharmacy Menagment System", font = ("arial", 42, "bold")
                              , fg = "black" , bd = 10, relief = "groove").grid(row = 0, columnspan = 2, pady = 20)

#===============================FRAMES====================================

        self.prozor = Frame(self.frame,bg = "whitesmoke", width = 1000, height = 100, bd = 10, relief = "groove").grid(row = 6,
                                                                                                     column = 0, pady = 5)

        Label(self.frame,bg = "whitesmoke", text = "Version 1.8 By Dragomir", fg = "black", font=("arial", 10, "bold")).grid(row = 6,pady =15, column = 0, columnspan = 3 )

        self.butoni = Frame(self.frame, bg = "white smoke", width = 1000, height = 700, bd = 0, relief = "groove")
        self.butoni.grid(row = 10, column = 0, pady = 150)

        self.okvir = Frame(self.frame, bg = "whitesmoke", width=1000, height=300, bd=0, relief="groove")
        self.okvir.grid(row=11, column=0, pady=2)

#==================Buttons===========================

        self.button_pacijent = Button(self.butoni,width = 10,bd = 5, height = 2, text = "Patients", font = ("arial", 15, "bold"), command = self.pacijent_window)
        self.button_pacijent.grid(row = 3 , column = 0, sticky = "", padx = 30)

        self.button_lek = Button(self.butoni, bd = 5, width = 10, height = 2,text="Drugs", font=("arial", 15, "bold"),
                                     command=self.lekovi_window)
        self.button_lek.grid(row=3, column=1, padx = 30, sticky = "")

        self.button_doktori = Button(self.butoni, bd = 5,width=10, height=2, text="Doctors", font=("arial", 15, "bold"),
                                      command=self.lekar_window)
        self.button_doktori.grid(row=3, column=2, padx=30, sticky = "")

        self.button_recept = Button(self.butoni,bd = 5, width=10, height=2, text="Prescription", font=("arial", 15, "bold"),
                                      command=self.recepti_window)
        self.button_recept.grid(row=3, column=3, padx=30)

        self.button_izlaz = Button(self.okvir, bd = 5, width = 10, height = 2,text="Quit", font=("arial", 15, "bold"),
                                      command=self.izlaz).grid(row = 0, column = 0)

        moj_meni = Menu(master)
        master.config(menu=moj_meni)

        file_meni = Menu(moj_meni)
        option_meni = Menu(moj_meni)
        moj_meni.add_cascade(label="File", menu=file_meni)
        moj_meni.add_cascade(label = "Navigate", menu=option_meni)
        option_meni.add_cascade(label = "Exit", command=self.izlaz)
        file_meni.add_command(label="Pacijenti", command=self.pacijent_window)
        file_meni.add_command(label = "Lekari", command=self.lekar_window)
        file_meni.add_command(label = "Lekovi", command=self.lekovi_window)
        file_meni.add_command(label = "Prescription", command=self.recepti_window)

    #===============FUNCTIONS====================================

    def pacijent_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = PacijentWindow(self.newWindow, Podaci)

    def lekar_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = DoctorWindow(self.newWindow, Podaci)

    def lekovi_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = LekWindow(self.newWindow, Podaci)

    def recepti_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = ReceptWindow(self.newWindow, Podaci)


    def izlaz(self):
        odgovor = tkinter.messagebox.askokcancel("Proizvodi", "Da li ste sigurni da želite da napustite aplikaciju?", icon="warning")
        if odgovor:
            quit()



class PacijentWindow():


    def __init__(self, master, Podaci):
        self.master = master
        self.master.title("Patient Menagment System")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.__jmbgTxt = StringVar()
        self.__imeTxt = StringVar()
        self.__prezimeTxt = StringVar()
        self.__lboTxt = StringVar()
        sorterTxt = StringVar()
        self.__datumTxt = StringVar()
        self.__datumTxt.set(time.strftime("%d/%m/%Y"))

        Label(self.frame, text ="Patient Menagment System", font=("arial", 15, "bold")).grid(row=0, column = 0)

        self.__podaci = Podaci()
        self.__podaciUcitaj = Podaci.ucitaj()





#=================Frames==========================

        pacijentFrame = Frame(self.master, bd = 4, relief = "groove", bg = "whitesmoke")
        pacijentFrame.place(x = 20, y = 40, width = 450, height = 630)

        listboxFrame = Frame(self.master, bd = 0, relief = "groove", bg = "whitesmoke")
        listboxFrame.place(x = 500, y = 150, width = 630, height = 300)

        prikazFrame = Frame(self.master, bd = 5, relief = "groove", bg = "whitesmoke")
        prikazFrame.place (x = 500 , y = 475 , width = 630 , height = 150)

        sorterFrame = Frame(self.master, relief = "groove", bg = "whitesmoke")
        sorterFrame.place(x = 500, y = 90, width = 630, height = 50)

        self.e_sorter = Entry(sorterFrame,width = 90,  textvariable = sorterTxt, bd = 2, font = ("arial", 12, "bold"))
        self.e_sorter.grid(row=2, column=1, pady=10, sticky = "")


        self.scrollbar = Scrollbar(listboxFrame, orient=VERTICAL)
        self.scrollbar.pack(fill=Y)

        self.listapacijenata = Listbox(listboxFrame, bd=5, relief="groove", width=250, height=300,
                                font=("arial", 12, "bold"), yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command=self.listapacijenata.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.listapacijenata.pack()



        #====================LABEL===============================

        l_jmbg = Label(pacijentFrame, text="JMBG: ", font=("arial", 10, "bold"))
        l_jmbg.grid(row=1, column=0, pady=5, padx=10, sticky="W")

        self.e_jmbg = Entry(pacijentFrame, textvariable= self.__jmbgTxt, bd=5, font=("arial", 12, "bold"), width = 30)
        self.e_jmbg.grid(row=1, column=1, pady=5, padx=10, sticky="E")

        l_ime = Label(pacijentFrame, text = "Ime: ", font = ("arial", 10, "bold"))
        l_ime.grid(row = 2, column =  0, pady = 5, padx = 10, sticky = "W")

        self.e_ime = Entry(pacijentFrame, textvariable = self.__imeTxt, bd = 5, font = ("arial",12, "bold"), width = 30)
        self.e_ime.grid(row = 2, column = 1,  pady = 5, padx = 10, sticky = "E")

        l_prezime = Label(pacijentFrame, text="Prezime: ", font=("arial", 10, "bold"))
        l_prezime.grid(row=3, column=0, pady=5, padx=10, sticky="W")

        self.e_prezime = Entry(pacijentFrame, textvariable= self.__prezimeTxt, bd=5, font=("arial", 12, "bold"), width = 30)
        self.e_prezime.grid(row=3, column=1, pady=5, padx=10, sticky="E")

        l_datum = Label(pacijentFrame, text="Datum: ", font=("arial", 10, "bold"))
        l_datum.grid(row=4, column=0, pady=5, padx=10, sticky="W")

        self.e_datum = Entry(pacijentFrame, textvariable=self.__datumTxt, bd=5, font=("arial", 12, "bold"), width = 30)
        self.e_datum.grid(row=4, column=1, pady=5, padx=10, sticky="E")

        l_lbo = Label(pacijentFrame, text="LBO: ", font=("arial", 10, "bold"))
        l_lbo.grid(row= 5, column=0, pady=5, padx=10, sticky="W")

        self.e_lbo = Entry(pacijentFrame, textvariable = self.__lboTxt ,font=("arial", 12, "bold"), bd =5, width = 30)
        self.e_lbo.grid(row= 5, column=1, pady=5, padx=10, sticky="W")

        b_clear = Button(pacijentFrame, text="Reset", font=("arial", 10, "bold"), command=self.clear)
        b_clear.grid(row=8, column=0, pady=5, padx=10)

        self.b_accept = Button(pacijentFrame, text="Accept", font=("arial", 10, "bold"), command=self.accept)
        self.b_accept.grid(row=8, column=1, pady=5, padx=0)

        self.b_izmeni = Button(pacijentFrame, text="Izmeni/Obrisi", font=("arial", 10, "bold"),
                          command=self.izmeni_pacijenta)
        self.b_izmeni.grid(row=9, column=1, pady=25, padx=10, sticky = "")

        self.b_prihvati_izmenu = Button(pacijentFrame, command=self.prihvati_izmenu, text="Prihvati Izmenu",
                                        font=("arial", 10, "bold"), state=DISABLED)
        self.b_prihvati_izmenu.grid(row=10, column=1, pady=25)

        self.b_obrisi = Button(pacijentFrame, command=self.izbrisi_komanda, text="Obrisi Pacijenta", font=("arial", 10, "bold"),
                               state=DISABLED)
        self.b_obrisi.grid(row=11, column=1, pady=25)

        jmbg_pLabel = Label(prikazFrame, text = "JMBG: ", font = ("arial", 10, "bold"))
        jmbg_pLabel.grid(row = 0, column = 0, sticky = "E")

        ime_pLabel = Label(prikazFrame, text="Ime: ", font=("arial", 10, "bold"))
        ime_pLabel.grid(row=1, column=0, sticky = "E")

        prezime_pLabel = Label(prikazFrame, text="Prezime: ", font=("arial", 10, "bold"))
        prezime_pLabel.grid(row=2, column=0, sticky = "E")

        datum_pLabel = Label(prikazFrame, text="Datum rodj: ", font=("arial", 10, "bold"))
        datum_pLabel.grid(row=3, column=0, sticky = "E")

        lbo_pLabel = Label(prikazFrame, text="LBO: ", font=("arial", 10, "bold"))
        lbo_pLabel.grid(row=4, column=0, sticky = "E")


        self.__jmbg_labela = Label(prikazFrame, font = ("arial", 12, "bold"))
        self.__jmbg_labela.grid(row =0 , column = 1)

        self.__ime_labela = Label(prikazFrame, font=("arial", 12, "bold"))
        self.__ime_labela.grid(row=1, column=1)

        self.__prezime_labela = Label(prikazFrame, font=("arial", 12, "bold"))
        self.__prezime_labela.grid(row=2, column=1)

        self.__datum_labela = Label(prikazFrame, font=("arial", 12, "bold"))
        self.__datum_labela.grid(row=3, column=1)

        self.__lbo_labela = Label(prikazFrame, font=("arial", 12, "bold"))
        self.__lbo_labela.grid(row=4, column=1)




        self.popuni_listbox(self.__podaciUcitaj.pacijenti)

        self.e_sorter.bind("<KeyRelease>", self.check)

        self.listapacijenata.bind("<<ListboxSelect>>", self.promena_selekcije_u_listbox)

   # ===============Functions=======================

    def check(self, event=None):

        typed = self.e_sorter.get()

        pacijenti = self.__podaciUcitaj.pacijenti

        if typed == "":
            data = pacijenti
        else:
            data = []
            for pacijent in pacijenti:
                if typed.lower() in  pacijent.prezime.lower() or typed.lower() in pacijent.ime.lower():
                    data.append(pacijent)
                    #=========#
        self.popuni_listbox(data)

    def clear(self):
        self.__jmbgTxt.set("")
        self.__imeTxt.set("")
        self.__prezimeTxt.set("")
        self.__lboTxt.set("")

        self.e_jmbg.config(state = "normal")
        self.e_lbo.config(state = "normal")

        self.e_jmbg.config(state="normal")
        self.b_accept.config(state=NORMAL)
        self.b_izmeni.config(state=NORMAL)
        self.b_obrisi.config(state=DISABLED)
        self.b_prihvati_izmenu.config(state=DISABLED)

    def accept(self):

        pacijenti = self.__podaciUcitaj.pacijenti

        jmbg = self.__jmbgTxt.get()
        duzina1 = self.__imeTxt.get()
        duzina2 = self.__prezimeTxt.get()
        lbo = self.__lboTxt.get()

        if len(jmbg) != 13 or not jmbg.isdigit():
            tkinter.messagebox.showwarning("Greska", "JMBG mora  biti broj i imati 13 karaktera!")
            return

        if len(duzina1) < 2 or duzina1.isdigit():
            tkinter.messagebox.showwarning("Greska", "Ime mora imati bar 2 karaktera i ne imati brojeve!")
            return

        if len(duzina2) < 2 or duzina2.isdigit():
            tkinter.messagebox.showwarning("Greska", "Prezime mora imati bar 2 karaktera i ne imati brojeve!")
            return

        if len(lbo) != 7 or not lbo.isdigit():
            tkinter.messagebox.showwarning("Greska", "LBO mora imati 7 cifara")
            return

        else:
             for pacijent in pacijenti:
                 if pacijent.jmbg == jmbg:
                     tkinter.messagebox.showwarning("Greska", "Osoba sa ovim JMBG-om vec postoji!")
                     return

             for pacijent in pacijenti:
                 if pacijent.jmbg == lbo:
                     tkinter.messagebox.showwarning("Greska", "Osoba sa ovim LBO-om vec postoji!")
                     return

             pacijent = Pacijent(self.__jmbgTxt.get(), self.__imeTxt.get(), self.__prezimeTxt.get(),self.__datumTxt.get(), self.__lboTxt.get())
             self.listapacijenata.insert(END,  "  "+ pacijent.prezime +"  " + pacijent.ime)

             self.__podaciUcitaj.pacijenti.append(pacijent)

             Podaci.sacuvaj(self.__podaciUcitaj)

             self.__jmbgTxt.set("")
             self.__imeTxt.set("")
             self.__prezimeTxt.set("")
             self.__lboTxt.set("")




             print("=================")
             print(pacijent)

    def izmeni_pacijenta(self):

        if not self.listapacijenata.curselection():
            tkinter.messagebox.showinfo("Greska", "Niste selektovali pacijenta za izmenu")
            return
        if  self.listapacijenata.curselection():

            self.b_prihvati_izmenu['state'] = NORMAL
            self.b_obrisi['state'] = NORMAL
            self.e_jmbg.config(state=DISABLED)
            self.e_lbo.config(state=DISABLED)
            self.b_accept.config(state=DISABLED)
            pacijent = self.__podaciUcitaj.pacijenti[self.listapacijenata.curselection()[0]]

            self.__jmbgTxt.set(pacijent.jmbg)
            self.__imeTxt.set(pacijent.ime)
            self.__prezimeTxt.set(pacijent.prezime)
            self.__datumTxt.set(pacijent.datum)
            self.__lboTxt.set(pacijent.lbo)



    def prihvati_izmenu(self):



             ime = self.__imeTxt.get()
             prezime = self.__prezimeTxt.get()
             datum = self.__datumTxt.get()
             jmbg = self.__jmbgTxt.get()

             if len(ime) < 2 or ime.isdigit():
                 tkinter.messagebox.showwarning("Greska", "Ime mora imati bar 2 karaktera i ne imati brojeve!")
                 return

             if len(prezime) < 2 or prezime.isdigit():
                 tkinter.messagebox.showwarning("Greska", "Prezime mora imati bar 2 karaktera i ne imati brojeve!")
                 return

             pacijenti = self.__podaciUcitaj.pacijenti

             if not self.listapacijenata.curselection():
                 tkinter.messagebox.showinfo("Greska", "Deselektovali ste pacijenta za izmenu")
                 return


             for pacijent in pacijenti:

                 if pacijent.jmbg == jmbg:
                     pacijent_izmena = pacijent
                     break

             pacijent_izmena.ime = ime
             pacijent_izmena.prezime = prezime
             pacijent_izmena.datum = datum

             #onemoguciti deselekciju dok traje izmena(listbox)

             #izmena pacijenata u labelu

             indeks = self.listapacijenata.curselection()[0]

             self.listapacijenata.delete(indeks)
             self.listapacijenata.insert(indeks, " - " + pacijent_izmena.prezime + " |  " + pacijent_izmena.ime)
             self.listapacijenata.selection_set(indeks)


             Podaci.sacuvaj(self.__podaciUcitaj)

             self.__jmbg_labela["text"] = pacijent.jmbg
             self.__ime_labela["text"] = pacijent.ime
             self.__prezime_labela["text"] = pacijent.prezime
             self.__datum_labela["text"] = pacijent.datum
             self.__lbo_labela["text"] = pacijent.lbo




             self.b_prihvati_izmenu['state'] = DISABLED
             self.b_obrisi.config(state=DISABLED)
             self.e_jmbg.config(state=NORMAL)
             self.e_lbo.config(state=NORMAL)
             self.b_accept.config(state=NORMAL)

             self.__jmbgTxt.set("")
             self.__imeTxt.set("")
             self.__prezimeTxt.set("")
             self.__lboTxt.set("")


    def ocisti_labele(self):
        self.__jmbg_labela['text'] = ""
        self.__ime_labela['text'] = ""
        self.__prezime_labela['text'] = ""
        self.__datum_labela['text'] = ""
        self.__lbo_labela['text'] = ""
        self.e_jmbg.config(state="normal")
        self.e_lbo.config(state="normal")

    def izbrisi_komanda(self):

        jmbg = self.__jmbgTxt.get()


        if tkinter.messagebox.askyesno("Upozorenje", "Ovom komandom cete obrisati pacijenta", icon = 'warning') == "no":
            return


        pacijent_izmena = self.listapacijenata.curselection()[0]
        self.__podaciUcitaj.obrisi_pacijenta(pacijent_izmena)




        Podaci.sacuvaj(self.__podaciUcitaj)

        self.listapacijenata.delete(pacijent_izmena)
        self.listapacijenata.selection_set(pacijent_izmena)



    def popuni_labele(self, pacijent):
        self.__jmbg_labela["text"] = pacijent.jmbg
        self.__ime_labela["text"] = pacijent.ime
        self.__prezime_labela["text"] = pacijent.prezime
        self.__datum_labela["text"] = pacijent.datum
        self.__lbo_labela["text"] = pacijent.lbo

    def promena_selekcije_u_listbox(self, event=None):
        if not self.listapacijenata.curselection():
            self.ocisti_labele()
            return


        indeks = self.listapacijenata.curselection()[0]
        pacijent = self.__podaciUcitaj.pacijenti[indeks]
        self.popuni_labele(pacijent)

    def popuni_listbox(self, pacijenti):
        format_linije = "{:10} | {:13}"
        self.listapacijenata.delete(0, END)
        for pacijent in pacijenti:
            self.listapacijenata.insert(END,  " - "+ format_linije.format(pacijent.prezime, pacijent.ime))


class DoctorWindow:


    def __init__(self, master, Podaci):
        self.master = master
        self.master.title("Doctors Menagment System")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.__jmbgTxt = StringVar()
        self.__imeTxt = StringVar()
        self.__prezimeTxt = StringVar()
        self.__specijalizacijaTxt = StringVar()
        sorterTxt = StringVar()
        self.__datumTxt = StringVar()
        self.__datumTxt.set(time.strftime("%d/%m/%Y"))

        Label(self.frame, text="Doctor Menagment System", font=("arial", 15, "bold")).grid(row=0, column=0)

        self.__podaci = Podaci()
        self.__podaciUcitaj = Podaci.ucitaj()

        # =================Frames==========================

        pacijentFrame = Frame(self.master, bd=4, relief="groove", bg="whitesmoke")
        pacijentFrame.place(x=20, y=40, width=450, height=630)

        listboxFrame = Frame(self.master, bd=0, relief="groove", bg="whitesmoke")
        listboxFrame.place(x=500, y=150, width=630, height=300)

        prikazFrame = Frame(self.master, bd=5, relief="groove", bg="whitesmoke")
        prikazFrame.place(x=500, y=475, width=630, height=150)

        sorterFrame = Frame(self.master, relief="groove", bg="whitesmoke")
        sorterFrame.place(x=500, y=90, width=630, height=50)


        self.e_sorter = Entry(sorterFrame, width=90, textvariable=sorterTxt, bd=2, font=("arial", 12, "bold"))
        self.e_sorter.grid(row=3, column=1, pady=0, sticky="")


        self.scrollbar = Scrollbar(listboxFrame, orient=VERTICAL)
        self.scrollbar.pack(fill=Y)

        self.listalekara = Listbox(listboxFrame, bd=5, relief="groove", width=250, height=300,
                                font=("arial", 12, "bold"), yscrollcommand=self.scrollbar.set)

        self.scrollbar.config(command=self.listalekara.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.listalekara.pack()
        # ====================LABEL===============================

        l_jmbg = Label(pacijentFrame, text="JMBG: ", font=("arial", 10, "bold"))
        l_jmbg.grid(row=1, column=0, pady=5, padx=10, sticky="W")

        self.e_jmbg = Entry(pacijentFrame, textvariable=self.__jmbgTxt, bd=5, font=("arial", 12, "bold"), width = 30)
        self.e_jmbg.grid(row=1, column=1, pady=5, padx=10, sticky="E")

        l_ime = Label(pacijentFrame, text="Ime: ", font=("arial", 10, "bold"))
        l_ime.grid(row=2, column=0, pady=5, padx=10, sticky="W")

        self.e_ime = Entry(pacijentFrame, textvariable=self.__imeTxt, bd=5, font=("arial", 12, "bold"),width = 30)
        self.e_ime.grid(row=2, column=1, pady=5, padx=10, sticky="E")

        l_prezime = Label(pacijentFrame, text="Prezime: ", font=("arial", 10, "bold"))
        l_prezime.grid(row=3, column=0, pady=5, padx=10, sticky="W")

        self.e_prezime = Entry(pacijentFrame, textvariable=self.__prezimeTxt, bd=5, font=("arial", 12, "bold"),width = 30)
        self.e_prezime.grid(row=3, column=1, pady=5, padx=10, sticky="E")

        l_datum = Label(pacijentFrame, text="Datum: ", font=("arial", 10, "bold"))
        l_datum.grid(row=4, column=0, pady=5, padx=10, sticky="W")

        self.e_datum = Entry(pacijentFrame, textvariable=self.__datumTxt, bd=5, font=("arial", 12, "bold"),width = 30)
        self.e_datum.grid(row=4, column=1, pady=5, padx=10, sticky="E")

        l_lbo = Label(pacijentFrame, text="Spec: ", font=("arial", 10, "bold"))
        l_lbo.grid(row=5, column=0, pady=5, padx=10, sticky="W")

        self.e_specijalizacija = Entry(pacijentFrame, textvariable=self.__specijalizacijaTxt, font=("arial", 12, "bold"), bd=5,width = 30)
        self.e_specijalizacija.grid(row=5, column=1, pady=5, padx=10, sticky="W")

        b_clear = Button(pacijentFrame, text="Reset", font=("arial", 10, "bold"), command=self.clear)
        b_clear.grid(row=8, column=0, pady=5, padx=10)

        self.b_accept = Button(pacijentFrame, text="Accept", font=("arial", 10, "bold"), command=self.accept)
        self.b_accept.grid(row=8, column=1, pady=5, padx=10)

        self.b_izmeni = Button(pacijentFrame, text="Izmeni/Obrisi", font=("arial", 10, "bold"),
                          command=self.izmeni_lekara)
        self.b_izmeni.grid(row=9, column=1, pady=25, padx=10)

        self.b_prihvati_izmenu = Button(pacijentFrame, command=self.prihvati_izmenu, text="Prihvati Izmenu",
                                        font=("arial", 10, "bold"), state=DISABLED)
        self.b_prihvati_izmenu.grid(row=10, column=1, pady=25)

        self.b_obrisi = Button(pacijentFrame, command=self.izbrisi_komanda, text="Obrisi Doktora", font=("arial", 10, "bold"),
                               state=DISABLED)
        self.b_obrisi.grid(row=11, column=1, pady=25)

        jmbg_pLabel = Label(prikazFrame, text="JMBG: ", font=("arial", 10, "bold"))
        jmbg_pLabel.grid(row=0, column=0, sticky="E")

        ime_pLabel = Label(prikazFrame, text="Ime: ", font=("arial", 10, "bold"))
        ime_pLabel.grid(row=1, column=0, sticky="E")

        prezime_pLabel = Label(prikazFrame, text="Prezime: ", font=("arial", 10, "bold"))
        prezime_pLabel.grid(row=2, column=0, sticky="E")

        datum_pLabel = Label(prikazFrame, text="Datum rodj: ", font=("arial", 10, "bold"))
        datum_pLabel.grid(row=3, column=0, sticky="E")

        lbo_pLabel = Label(prikazFrame, text="Spec: ", font=("arial", 10, "bold"))
        lbo_pLabel.grid(row=4, column=0, sticky="E")

        self.__jmbg_labela = Label(prikazFrame, font=("arial", 12, "bold"))
        self.__jmbg_labela.grid(row=0, column=1)

        self.__ime_labela = Label(prikazFrame, font=("arial", 12, "bold"))
        self.__ime_labela.grid(row=1, column=1)

        self.__prezime_labela = Label(prikazFrame, font=("arial", 12, "bold"))
        self.__prezime_labela.grid(row=2, column=1)

        self.__datum_labela = Label(prikazFrame, font=("arial", 12, "bold"))
        self.__datum_labela.grid(row=3, column=1)

        self.__lbo_labela = Label(prikazFrame, font=("arial", 12, "bold"))
        self.__lbo_labela.grid(row=4, column=1)

        self.listalekara.bind("<<ListboxSelect>>", self.promena_selekcije_u_listbox)

        self.popuni_listbox(self.__podaciUcitaj.lekari)

        self.e_sorter.bind("<KeyRelease>", self.check)

    # ===============Functions=======================

    def check(self, event = None):

        typed = self.e_sorter.get()

        lekari = self.__podaciUcitaj.lekari

        if typed == "":
           data = lekari
        else:
            data = []
            for lekar in lekari:
                if typed.lower() in lekar.prezime.lower() or typed.lower() in lekar.ime.lower():
                    data.append(lekar)

        self.popuni_listbox(data)

    def clear(self):
        self.__jmbgTxt.set("")
        self.__imeTxt.set("")
        self.__prezimeTxt.set("")
        self.__specijalizacijaTxt.set("")

        self.e_jmbg.config(state="normal")
        self.e_specijalizacija.config(state="normal")

        self.e_jmbg.config(state="normal")
        self.b_accept.config(state=NORMAL)
        self.b_izmeni.config(state=NORMAL)
        self.b_obrisi.config(state=DISABLED)
        self.b_prihvati_izmenu.config(state=DISABLED)

    def accept(self):

        lekari = self.__podaciUcitaj.lekari
        jmbg = self.__jmbgTxt.get()
        duzina1 = self.__imeTxt.get()
        duzina2 = self.__prezimeTxt.get()
        duzina3 = self.__specijalizacijaTxt.get()

        if len(jmbg) != 13 or not jmbg.isdigit():
            tkinter.messagebox.showwarning("Greska", "JMBG mora  biti broj i imati 13 karaktera!")
            return

        if len(duzina1) < 2 or duzina1.isdigit():
            tkinter.messagebox.showwarning("Greska", "Ime mora imati bar 2 karaktera i ne imati brojeve!")
            return

        if len(duzina2) < 2 or duzina2.isdigit():
            tkinter.messagebox.showwarning("Greska", "Prezime mora imati bar 2 karaktera i ne imati brojeve!")
            return

        if len(duzina3) < 2 or  duzina3.isdigit():
            tkinter.messagebox.showwarning("Greska", "Specijalizacija mora imati bar 2 simbola i ne sme biti broj")
            return

        else:

            for lekar in lekari:
                if lekar.jmbg == jmbg:
                    tkinter.messagebox.showwarning("Greska", "Osoba sa ovim JMBG-om vec postoji!")
                    return



            lekar = Lekar(self.__jmbgTxt.get(), self.__imeTxt.get(), self.__prezimeTxt.get(),
                                self.__datumTxt.get(), self.__specijalizacijaTxt.get())
            self.listalekara.insert(END, "  " + lekar.prezime + "  " + lekar.ime)

            self.__podaciUcitaj.lekari.append(lekar)

            Podaci.sacuvaj(self.__podaciUcitaj)

            self.__jmbgTxt.set("")
            self.__imeTxt.set("")
            self.__prezimeTxt.set("")
            self.__specijalizacijaTxt.set("")

            print("=================")
            print(lekar)

    def izmeni_lekara(self):

        if not self.listalekara.curselection():
            tkinter.messagebox.showinfo("Greska", "Niste selektovali pacijenta za izmenu")
            return
        if self.listalekara.curselection():
            self.b_prihvati_izmenu['state'] = NORMAL
            self.b_obrisi['state'] = NORMAL
            self.e_jmbg.config(state=DISABLED)
            self.b_accept.config(state=DISABLED)

            lekar = self.__podaciUcitaj.lekari[self.listalekara.curselection()[0]]

            self.__jmbgTxt.set(lekar.jmbg)
            self.__imeTxt.set(lekar.ime)
            self.__prezimeTxt.set(lekar.prezime)
            self.__datumTxt.set(lekar.datum)
            self.__specijalizacijaTxt.set(lekar.specijalizacija)



    def prihvati_izmenu(self):



        ime = self.__imeTxt.get()
        prezime = self.__prezimeTxt.get()
        datum = self.__datumTxt.get()
        jmbg = self.__jmbgTxt.get()
        specijalizacija = self.__specijalizacijaTxt.get()

        if len(ime) < 2 or ime.isdigit():
            tkinter.messagebox.showwarning("Greska", "Ime mora imati bar 2 karaktera i ne imati brojeve!")
            return

        if len(prezime) < 2 or prezime.isdigit():
            tkinter.messagebox.showwarning("Greska", "Prezime mora imati bar 2 karaktera i ne imati brojeve!")
            return

        if len(specijalizacija) < 2 or specijalizacija.isdigit():
            tkinter.messagebox.showwarning("Greska", "Specijalizacija mora imati bar 2 karaktera i ne sme biti broj!")


        lekari = self.__podaciUcitaj.lekari

        for lekar in lekari:

            if lekar.jmbg == jmbg:
                lekar_izmena = lekar
                break

        if not self.listalekara.curselection():
            tkinter.messagebox.showinfo("Greska", "Deselektovali ste lekara za izmenu")
            return

        lekar_izmena.ime = ime
        lekar_izmena.prezime = prezime
        lekar_izmena.datum = datum
        lekar_izmena.specijalizacija = specijalizacija



        indeks = self.listalekara.curselection()[0]

        self.listalekara.delete(indeks)
        self.listalekara.insert(indeks, "  " + lekar_izmena.prezime + "  " + lekar_izmena.ime)
        self.listalekara.selection_set(indeks)

        Podaci.sacuvaj(self.__podaciUcitaj)



        self.__jmbg_labela["text"] = lekar.jmbg
        self.__ime_labela["text"] = lekar.ime
        self.__prezime_labela["text"] = lekar.prezime
        self.__datum_labela["text"] = lekar.datum
        self.__lbo_labela["text"] = lekar.specijalizacija

        self.b_prihvati_izmenu['state'] = DISABLED
        self.b_obrisi.config(state=DISABLED)
        self.e_jmbg.config(state=NORMAL)
        self.b_accept.config(state=NORMAL)



        self.b_prihvati_izmenu['state'] = DISABLED

        self.__jmbgTxt.set("")
        self.__imeTxt.set("")
        self.__prezimeTxt.set("")
        self.__specijalizacijaTxt.set("")

    def ocisti_labele(self):
        self.__jmbg_labela['text'] = ""
        self.__ime_labela['text'] = ""
        self.__prezime_labela['text'] = ""
        self.__datum_labela['text'] = ""
        self.__lbo_labela['text'] = ""
        self.e_jmbg.config(state="normal")
        self.e_specijalizacija.config(state="normal")


    def izbrisi_komanda(self):
            jmbg = self.__jmbgTxt.get()

            if tkinter.messagebox.askyesno("Upozorenje", "Ovom komandom cete obrisati pacijenta",
                                           icon='warning') == "no":
                return

            lekar_izmena = self.listalekara.curselection()[0]
            self.__podaciUcitaj.obrisi_lekara(lekar_izmena)

            Podaci.sacuvaj(self.__podaciUcitaj)

            self.listalekara.delete(lekar_izmena)
            self.listalekara.selection_set(lekar_izmena)

    def popuni_labele(self, lekar):
        self.__jmbg_labela["text"] = lekar.jmbg
        self.__ime_labela["text"] = lekar.ime
        self.__prezime_labela["text"] = lekar.prezime
        self.__datum_labela["text"] = lekar.datum
        self.__lbo_labela["text"] = lekar.specijalizacija

    def promena_selekcije_u_listbox(self, event=None):
        if not self.listalekara.curselection():
            self.ocisti_labele()
            return

        indeks = self.listalekara.curselection()[0]
        lekar = self.__podaciUcitaj.lekari[indeks]
        self.popuni_labele(lekar)

    def popuni_listbox(self, lekari):
        self.listalekara.delete(0, END)
        for lekar in lekari:
            self.listalekara.insert(END, "  " + lekar.prezime + "  |  " + lekar.ime)

class LekWindow:

    def __init__(self, master, Podaci):
        self.master = master
        self.master.title("Drugs Menagment System")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.__jklTxt = StringVar()
        self.__nazivTxt = StringVar()
        self.__proizvodjacTxt = StringVar()
        self.__tiplekaTxt = StringVar()
        self.__sorterTxt = StringVar()

        Label(self.frame, text="Drugs Menagment System", font=("arial", 15, "bold")).grid(row=0, column=0)

        self.__podaci = Podaci()
        self.__podaciUcitaj = Podaci.ucitaj()

        # =================Frames==========================

        pacijentFrame = Frame(self.master, bd=4, relief="groove", bg="whitesmoke")
        pacijentFrame.place(x=20, y=40, width=450, height=630)

        listboxFrame = Frame(self.master, bd=0, relief="groove", bg="whitesmoke")
        listboxFrame.place(x=500, y=150, width=630, height=300)

        prikazFrame = Frame(self.master, bd=5, relief="groove", bg="whitesmoke")
        prikazFrame.place(x=500, y=475, width=630, height=150)

        sorterFrame = Frame(self.master, relief="groove", bg="whitesmoke")
        sorterFrame.place(x=500, y=90, width=630, height=50)

        self.e_sorter = Entry(sorterFrame, width=90, textvariable=self.__sorterTxt, bd=2, font=("arial", 12, "bold"))
        self.e_sorter.grid(row=2, column=1, pady=10, sticky="")

        self.scrollbar = Scrollbar(listboxFrame, orient=VERTICAL)
        self.scrollbar.pack(fill=Y)

        self.listalek = Listbox(listboxFrame, bd=5, relief="groove", width=250, height=300,
                                       font=("arial", 12, "bold"), yscrollcommand = self.scrollbar.set)

        self.scrollbar.config(command = self.listalek.yview)
        self.scrollbar.pack(side = RIGHT, fill = Y)

        self.listalek.pack()


        # ====================LABEL===============================

        l_jmbg = Label(pacijentFrame, text="JKL: ", font=("arial", 10, "bold"))
        l_jmbg.grid(row=1, column=0, pady=5, padx=10, sticky="W")

        self.e_jkl = Entry(pacijentFrame, textvariable=self.__jklTxt, bd=5, font=("arial", 12, "bold"), width = 30)
        self.e_jkl.grid(row=1, column=1, pady=5, padx=10, sticky="E")

        l_ime = Label(pacijentFrame, text="Naziv: ", font=("arial", 10, "bold"))
        l_ime.grid(row=2, column=0, pady=5, padx=10, sticky="W")

        self.e_naziv = Entry(pacijentFrame, textvariable=self.__nazivTxt, bd=5, font=("arial", 12, "bold"), width = 30)
        self.e_naziv.grid(row=2, column=1, pady=5, padx=10, sticky="E")

        l_prezime = Label(pacijentFrame, text="Prozivodjac: ", font=("arial", 10, "bold"))
        l_prezime.grid(row=3, column=0, pady=5, padx=10, sticky="W")

        self.e_proizvodjac = Entry(pacijentFrame, textvariable=self.__proizvodjacTxt, bd=5, font=("arial", 12, "bold"), width = 30)
        self.e_proizvodjac.grid(row=3, column=1, pady=5, padx=10, sticky="E")

        l_datum = Label(pacijentFrame, text="Tip Leka: ", font=("arial", 10, "bold"))
        l_datum.grid(row=4, column=0, pady=5, padx=10, sticky="W")

        self.e_tipLeka = Entry(pacijentFrame, textvariable=self.__tiplekaTxt, bd=5, font=("arial", 12, "bold"), width = 30)
        self.e_tipLeka.grid(row=4, column=1, pady=5, padx=10, sticky="E")


        b_clear = Button(pacijentFrame, text="Reset", font=("arial", 10, "bold"), command=self.clear)
        b_clear.grid(row=7, column=0, pady=0, padx=10)

        self.b_accept = Button(pacijentFrame, text="Accept", font=("arial", 10, "bold"), command=self.accept)
        self.b_accept.grid(row=7, column=1, pady=15, padx=10)

        self.b_izmeni = Button(pacijentFrame, text="Izmeni/Obrisi", font=("arial", 10, "bold"),
                          command=self.izmeni_lek)
        self.b_izmeni.grid(row=8, column=1, pady=15, padx=10)

        self.b_prihvati_izmenu = Button(pacijentFrame, command=self.prihvati_izmenu, text="Prihvati Izmenu",
                                        font=("arial", 10, "bold"), state=DISABLED)
        self.b_prihvati_izmenu.grid(row=9, column=1, pady=15)

        self.b_obrisi = Button(pacijentFrame, command=self.izbrisi_komanda, text="Obrisi Lek", font=("arial", 10, "bold"),
                               state=DISABLED)
        self.b_obrisi.grid(row=10, column=1, pady=15)

        jmbg_pLabel = Label(prikazFrame, text="JKL: ", font=("arial", 10, "bold"))
        jmbg_pLabel.grid(row=0, column=0, sticky="E")

        ime_pLabel = Label(prikazFrame, text="Naziv: ", font=("arial", 10, "bold"))
        ime_pLabel.grid(row=1, column=0, sticky="E")

        prezime_pLabel = Label(prikazFrame, text="Prozivodjac: ", font=("arial", 10, "bold"))
        prezime_pLabel.grid(row=2, column=0, sticky="E")

        datum_pLabel = Label(prikazFrame, text="Tip Leka: ", font=("arial", 10, "bold"))
        datum_pLabel.grid(row=3, column=0, sticky="E")




        self.__jkl_labela = Label(prikazFrame, font=("arial", 12, "bold"))
        self.__jkl_labela.grid(row=0, column=1)

        self.__naziv_labela = Label(prikazFrame, font=("arial", 12, "bold"))
        self.__naziv_labela.grid(row=1, column=1)

        self.__proizvodjac_labela = Label(prikazFrame, font=("arial", 12, "bold"))
        self.__proizvodjac_labela.grid(row=2, column=1)

        self.__tipLeka_labela = Label(prikazFrame, font=("arial", 12, "bold"))
        self.__tipLeka_labela.grid(row=3, column=1)

        self.__lbo_labela = Label(prikazFrame, font=("arial", 12, "bold"))
        self.__lbo_labela.grid(row=4, column=1)


        self.listalek.bind("<<ListboxSelect>>", self.promena_selekcije_u_listbox)

        self.popuni_listbox(self.__podaciUcitaj.lekovi)

        self.e_sorter.bind("<KeyRelease>", self.check)

    # ===============Functions=======================

    def check(self, event=None):

        typed = self.e_sorter.get()

        lekovi = self.__podaciUcitaj.lekovi

        if typed == "":
            data = lekovi
        else:
            data = []
            for lek in lekovi:
                if typed.lower() in lek.proizvodjac.lower() or typed.lower() in lek.naziv.lower():
                    data.append(lek)

        self.popuni_listbox(data)

    def clear(self):
        self.__jklTxt.set("")
        self.__nazivTxt.set("")
        self.__proizvodjacTxt.set("")
        self.__tiplekaTxt.set("")


        self.e_jkl.config(state="normal")
        self.b_accept.config(state = NORMAL)
        self.b_izmeni.config(state=NORMAL)
        self.b_obrisi.config(state=DISABLED)
        self.b_prihvati_izmenu.config(state=DISABLED)


    def accept(self):

        lekovi = self.__podaciUcitaj.lekovi
        jkl = self.__jklTxt.get()
        duzina1 = self.__nazivTxt.get()
        duzina2 = self.__proizvodjacTxt.get()
        duzina3 = self.__tiplekaTxt.get()

        if len(jkl) != 7 or not jkl.isdigit():
            tkinter.messagebox.showwarning("Greska", "JKL mora  biti broj i imati 7 karaktera!")
            return

        if len(duzina1) < 2 or duzina1.isdigit():
            tkinter.messagebox.showwarning("Greska", "Naziv mora imati bar 2 karaktera i ne imati brojeve!")
            return

        if len(duzina2) < 2 or duzina2.isdigit():
            tkinter.messagebox.showwarning("Greska", "Proizvodjac mora imati bar 2 karaktera i ne imati brojeve!")
            return

        if len(duzina3) < 2 or  duzina3.isdigit():
            tkinter.messagebox.showwarning("Greska", "Tip Leka mora imati bar 2 simbola i ne sme biti broj")
            return

        else:
            for lek in lekovi:
                if lek.jkl == jkl:
                    tkinter.messagebox.showwarning("Greska", "Uneti JKL je vec u upotrebi!")

            lek = Lek(self.__jklTxt.get(), self.__nazivTxt.get(), self.__proizvodjacTxt.get(),
                                self.__tiplekaTxt.get())
            self.listalek.insert(END, "  " + lek.proizvodjac + " | " + lek.naziv)

            self.__podaciUcitaj.lekovi.append(lek)

            Podaci.sacuvaj(self.__podaciUcitaj)

            self.__jklTxt.set("")
            self.__nazivTxt.set("")
            self.__proizvodjacTxt.set("")
            self.__tiplekaTxt.set("")


            print("=================")
            print(lek)

    def izmeni_lek(self):

        if not self.listalek.curselection():
            tkinter.messagebox.showinfo("Greska", "Niste selektovali lek za izmenu")
            return
        if self.listalek.curselection():
            self.b_prihvati_izmenu['state'] = NORMAL
            self.b_obrisi['state'] = NORMAL
            self.e_jkl.config(state=DISABLED)
            self.b_accept['state'] = DISABLED
            lek = self.__podaciUcitaj.lekovi[self.listalek.curselection()[0]]

            self.__jklTxt.set(lek.jkl)
            self.__nazivTxt.set(lek.naziv)
            self.__proizvodjacTxt.set(lek.proizvodjac)
            self.__tiplekaTxt.set(lek.tip_leka)


    def prihvati_izmenu(self):

        jkl = self.__jklTxt.get()
        naziv = self.__nazivTxt.get()
        proizvodjac = self.__proizvodjacTxt.get()
        tip_leka = self.__tiplekaTxt.get()



        if len(naziv) < 2 or naziv.isdigit():
            tkinter.messagebox.showwarning("Greska", "Naziv leka mora imati bar 2 karaktera i ne imati brojeve!")
            return

        if len(proizvodjac) < 2 or proizvodjac.isdigit():
            tkinter.messagebox.showwarning("Greska", "Proizvodjac mora imati bar 2 karaktera i ne imati brojeve!")
            return

        lekovi = self.__podaciUcitaj.lekovi

        for lek in lekovi:

            if lek.jkl == jkl:
                lek_izmena = lek
                break
        if not self.listalek.curselection():
            tkinter.messagebox.showwarning("Greska", "Deselektoval iste lek iz liste.")
            return

        lek_izmena.naziv = naziv
        lek_izmena.tip_leka = tip_leka
        lek_izmena.proizvodjac = proizvodjac


        indeks = self.listalek.curselection()[0]

        Podaci.sacuvaj(self.__podaciUcitaj)

        self.__jkl_labela["text"] = lek.jkl
        self.__naziv_labela["text"] = lek.naziv
        self.__proizvodjac_labela["text"] = lek.proizvodjac
        self.__tipLeka_labela["text"] = lek.tip_leka

        self.listalek.delete(indeks)
        self.listalek.insert(indeks, "  " + lek_izmena.proizvodjac + "  " + lek_izmena.naziv)
        self.listalek.selection_set(indeks)

        self.b_prihvati_izmenu['state'] = DISABLED

        self.__jklTxt.set("")
        self.__nazivTxt.set("")
        self.__proizvodjacTxt.set("")
        self.__tiplekaTxt.set("")
        self.b_accept.config(state = NORMAL)

    def ocisti_labele(self):
        self.__jkl_labela['text'] = ""
        self.__naziv_labela['text'] = ""
        self.__proizvodjac_labela['text'] = ""
        self.__tipLeka_labela['text'] = ""
        self.__lbo_labela['text'] = ""
        self.e_jkl.config(state="normal")

    def izbrisi_komanda(self):

        jkl = self.__jklTxt.get()

        if not self.listalek.curselection():
            tkinter.messagebox.showwarning("Greska", "Deselektoval iste lek iz liste.")
            return

        if tkinter.messagebox.askyesno("Upozorenje", "Ovom komandom cete obrisati lek", icon='warning') == "no":
            return



        lek_izmena = self.listalek.curselection()[0]
        self.__podaciUcitaj.obrisi_lek(lek_izmena)

        Podaci.sacuvaj(self.__podaciUcitaj)

        self.listalek.delete(lek_izmena)
        self.listalek.selection_set(lek_izmena)

    def popuni_labele(self, lek):
        self.__jkl_labela["text"] = lek.jkl
        self.__naziv_labela["text"] = lek.naziv
        self.__proizvodjac_labela["text"] = lek.proizvodjac
        self.__tipLeka_labela["text"] = lek.tip_leka

    def promena_selekcije_u_listbox(self, event=None):
        if not self.listalek.curselection():
            self.ocisti_labele()
            return

        indeks = self.listalek.curselection()[0]
        lekovi = self.__podaciUcitaj.lekovi[indeks]
        self.popuni_labele(lekovi)

    def popuni_listbox(self, lekovi):
        self.listalek.delete(0, END)
        for lek in lekovi:
            self.listalek.insert(END, "  " + lek.proizvodjac + "  |  " + lek.naziv)





class ReceptWindow():

        def __init__(self, master, Podaci):
            self.master = master
            self.master.title("Prescription Menagment System")
            self.master.geometry("1350x750+0+0")
            self.frame = Frame(self.master)
            self.frame.pack()

            self.__pacijentTxt = StringVar()
            self.__imeTxt = StringVar()
            self.__prezimeTxt = StringVar()
            self.__kolicinaInt = IntVar()
            sorterTxt = StringVar()
            self.__datumTxt = StringVar()
            self.__datumTxt.set(time.strftime("%d.%m.%Y. %H:%M:%S"))

            Label(self.frame, text="Prescription Menagment System", font=("arial", 15, "bold")).grid(row=0, column=0)

            self.__podaci = Podaci()
            self.__podaciUcitaj = Podaci.ucitaj()

            # =================Frames==========================

            receptFrame = Frame(self.master, bd=4, relief="groove", bg="whitesmoke")
            receptFrame.place(x=20, y=40, width=450, height=630)

            listboxFrame = Frame(self.master, bd=0, relief="groove", bg="whitesmoke")
            listboxFrame.place(x=500, y=150, width=630, height=300)

            prikazFrame = Frame(self.master, bd=5, relief="groove", bg="whitesmoke")
            prikazFrame.place(x=500, y=475, width=630, height=175)

            sorterFrame = Frame(self.master, relief="groove", bg="whitesmoke")
            sorterFrame.place(x=500, y=90, width=630, height=50)

            self.e_sorter = Entry(sorterFrame, width=90, textvariable=sorterTxt, bd=2, font=("arial", 12, "bold"))
            self.e_sorter.grid(row=2, column=1, pady=10, sticky="")

            
            self.scrollbar = Scrollbar(listboxFrame, orient=VERTICAL)
            self.scrollbar.pack(fill=Y)

            self.listapacijenata = Listbox(listboxFrame, bd=5, relief="groove", width=250, height=300,
                                           font=("arial", 12, "bold"), yscrollcommand=self.scrollbar.set)

            self.scrollbar.config(command=self.listapacijenata.yview)
            self.scrollbar.pack(side=RIGHT, fill=Y)

            self.listapacijenata.pack()

            # ====================LABEL===============================

            pacijenti = self.__podaciUcitaj.pacijenti
            lekari = self.__podaciUcitaj.lekari
            lekovi = self.__podaciUcitaj.lekovi

            l_pacijent = Label(receptFrame, text="Pacijent: ", font=("arial", 10, "bold"))
            l_pacijent.grid(row=1, column=0, pady=5, padx=10, sticky="W")

            self.e_pacijent = Combobox(receptFrame, textvariable=self.__pacijentTxt, font=("arial", 12, "bold"))
            self.e_pacijent.grid(row=1, column=1, pady=5, padx=10, sticky="E")

            pacijenticombo = list()
            for pacijent in pacijenti:
                pacijenticombo.append(pacijent.prezime + " " + pacijent.ime)
            self.e_pacijent['values'] = pacijenticombo



            l_lekar = Label(receptFrame, text="Lekar: ", font=("arial", 10, "bold"))
            l_lekar.grid(row=2, column=0, pady=5, padx=10, sticky="W")

            self.e_lekar = Combobox(receptFrame,textvariable=self.__prezimeTxt, font=("arial", 12, "bold"))
            self.e_lekar.grid(row=2, column=1, pady=5, padx=10, sticky="E")

            lekarcombo = list()
            for lekar in lekari:
                lekarcombo.append(lekar.prezime + " " + lekar.ime)
            self.e_lekar['values'] = lekarcombo



            l_lek = Label(receptFrame, text="Lek: ", font=("arial", 10, "bold"))
            l_lek.grid(row=3, column=0, pady=5, padx=10, sticky="W")



            self.e_lekovi = Combobox(receptFrame,textvariable = self.__imeTxt, font=("arial", 12, "bold"))
            self.e_lekovi.grid(row=3, column=1, pady=5, padx=10, sticky="E")

            lekovicombo = list()
            for lek in lekovi:
                lekovicombo.append(lek.proizvodjac + " " + lek.naziv)
            self.e_lekovi['values'] = lekovicombo


            l_datum = Label(receptFrame, text="Datum: ", font=("arial", 10, "bold"))
            l_datum.grid(row=4, column=0, pady=5, padx=10, sticky="W")

            self.e_datum = Entry(receptFrame, textvariable=self.__datumTxt, font=("arial", 12, "bold"), bd=5)
            self.e_datum.grid(row=4, column=1, pady=5, padx=10, sticky="W")

            l_kolicina = Label(receptFrame, text="Kolicina(mg): ", font=("arial", 10, "bold"))
            l_kolicina.grid(row=5, column=0, pady=5, padx=10, sticky="W")

            self.e_kolicina = Entry(receptFrame, textvariable=self.__kolicinaInt, font=("arial", 12, "bold"), bd=5)
            self.e_kolicina.grid(row=5, column=1, pady=5, padx=10, sticky="W")

            b_clear = Button(receptFrame, text="Reset", font=("arial", 10, "bold"), command=self.clear)
            b_clear.grid(row=10, column=0, pady=0, padx=10)

            self.b_accept = Button(receptFrame, text="Accept", font=("arial", 10, "bold"), command=self.accept)
            self.b_accept.grid(row=10, column=1, pady=0, padx=10)

            self.b_izmeni = Button(receptFrame, text="Izmeni/Obrisi", font=("arial", 10, "bold"),
                              command=self.izmeni_recept)
            self.b_izmeni.grid(row=11, column=1, pady=15, padx=10)

            self.b_prihvati_izmenu = Button(receptFrame, command=self.prihvati_izmenu, text="Prihvati Izmenu",
                                            font=("arial", 10, "bold"), state=DISABLED)
            self.b_prihvati_izmenu.grid(row=12, column=1, pady=15)

            self.b_obrisi = Button(receptFrame, command=self.izbrisi_komanda, text="Obrisi ",
                                   font=("arial", 10, "bold"), state=DISABLED)
            self.b_obrisi.grid(row=13, column=1, pady=15)

            self.__pacijent_pLabel = Label(prikazFrame, text="Pacijent: ", font=("arial", 10, "bold"))
            self.__pacijent_pLabel.grid(row=0, column=0, sticky="E")

            self.__lekar_pLabel = Label(prikazFrame, text="Lek: ", font=("arial", 10, "bold"))
            self.__lekar_pLabel.grid(row=1, column=0, sticky="E")

            self.__lek_pLabel = Label(prikazFrame, text="Lekar: ", font=("arial", 10, "bold"))
            self.__lek_pLabel.grid(row=2, column=0, sticky="E")

            self.__datum_pLabel = Label(prikazFrame, text="Datum: ", font=("arial", 10, "bold"))
            self.__datum_pLabel.grid(row=3, column=0, sticky="E")

            self.__kolicina_pLabel = Label(prikazFrame, text="Kolicina(mg): ", font=("arial", 10, "bold"))
            self.__kolicina_pLabel.grid(row=4, column=0, sticky="E")

            self.__izvestaj_pLabel = Label(prikazFrame, text = "Izvestaj: ", font = ("arial", 10, "bold"))
            self.__izvestaj_pLabel.grid(row = 5, column = 0 , sticky = "E")


            self.listapacijenata.bind("<<ListboxSelect>>", self.promena_selekcije_u_listbox)

            self.popuni_listbox(self.__podaciUcitaj.recepti)

            self.__jmbg_labela = Label(prikazFrame, font=("arial", 12, "bold"))
            self.__jmbg_labela.grid(row=0, column=1)

            self.__ime_labela = Label(prikazFrame, font=("arial", 12, "bold"))
            self.__ime_labela.grid(row=1, column=1)

            self.__prezime_labela = Label(prikazFrame, font=("arial", 12, "bold"))
            self.__prezime_labela.grid(row=2, column=1)

            self.__datum_labela = Label(prikazFrame, font=("arial", 12, "bold"))
            self.__datum_labela.grid(row=3, column=1)

            self.__lbo_labela = Label(prikazFrame, font=("arial", 12, "bold"))
            self.__lbo_labela.grid(row=4, column=1)

            self.__izvestaj_labela = Label(prikazFrame, font = ('arial', 12, "bold"))
            self.__izvestaj_labela.grid(row = 5, column = 1)

            self.e_sorter.bind("<KeyRelease>", self.check)

        # ===============Functions=======================

        def check(self, event=None):

            typed = self.e_sorter.get()

            recepti = self.__podaciUcitaj.recepti

            if typed == "":
                data = recepti
            else:
                data = []
                for recept in recepti:
                    if typed.lower() in recept.pacijent.lower() or typed.lower() in recept.Lek.lower():
                        data.append(recept)

            self.popuni_listbox(data)

        def clear(self):
            self.__pacijentTxt.set("")
            self.__imeTxt.set("")
            self.__prezimeTxt.set("")
            self.__kolicinaInt.set(0)

            self.b_prihvati_izmenu.config(state = DISABLED)
            self.b_obrisi.config(state= DISABLED)
            self.b_accept.config(state = NORMAL)



            self.e_pacijent.config(state="normal")
            self.e_kolicina.config(state="normal")

        def accept(self):

            duzina = self.__pacijentTxt.get()
            duzina1 = self.__imeTxt.get()
            duzina2 = self.__prezimeTxt.get()
            duzina3 = self.__kolicinaInt.get()

            if duzina == "" or duzina1 == "" or duzina2 == "":
                tkinter.messagebox.showwarning("Greska", "Uneli ste prazno polje")
                return

            if duzina3 <= 0:
                tkinter.messagebox.showwarning("Greska", "Kolicina mora biti veca od 0")
                return

            recept = Recept(self.__pacijentTxt.get(), self.__imeTxt.get(), self.__prezimeTxt.get(), self.__datumTxt.get(), self.__kolicinaInt.get())
            self.listapacijenata.insert(END, "  " + recept.pacijent + " \t \t \t " + recept.Lek)

            self.__podaciUcitaj.recepti.append(recept)

            Podaci.sacuvaj(self.__podaciUcitaj)

            print(recept)

            self.__pacijentTxt.set("")
            self.__imeTxt.set("")
            self.__prezimeTxt.set("")
            self.__kolicinaInt.set("")

        def izmeni_recept(self):

            if not self.listapacijenata.curselection():
                tkinter.messagebox.showinfo("Greska", "Niste selektovali recept za izmenu")
                return
            if self.listapacijenata.curselection():
                self.b_prihvati_izmenu['state'] = NORMAL
                self.b_obrisi['state'] = NORMAL
                self.e_pacijent.config(state=DISABLED)
                self.b_accept.config(state= DISABLED)
                recept = self.__podaciUcitaj.recepti[self.listapacijenata.curselection()[0]]

                self.__pacijentTxt.set(recept.pacijent)
                self.__imeTxt.set(recept.Lek)
                self.__prezimeTxt.set(recept.Lekar)
                self.__datumTxt.set(recept.datum)
                self.__kolicinaInt.set(recept.kolicina)

        def prihvati_izmenu(self):

            ime = self.__imeTxt.get()
            prezime = self.__prezimeTxt.get()
            datum = self.__datumTxt.get()
            jmbg = self.__pacijentTxt.get()

            if len(ime) < 2 or ime.isdigit():
                tkinter.messagebox.showwarning("Greska", "Ime mora imati bar 2 karaktera i ne imati brojeve!")
                return

            if len(prezime) < 2 or prezime.isdigit():
                tkinter.messagebox.showwarning("Greska", "Prezime mora imati bar 2 karaktera i ne imati brojeve!")
                return

            recepti = self.__podaciUcitaj.recepti

            for recept in recepti:

                if recept.pacijent == jmbg:
                    pacijent_izmena = recept
                    break

            pacijent_izmena.ime = ime
            pacijent_izmena.prezime = prezime
            pacijent_izmena.datum = datum


            indeks = self.listapacijenata.curselection()[0]

            Podaci.sacuvaj(self.__podaciUcitaj)

            self.__jmbg_labela["text"] = recept.pacijent
            self.__ime_labela["text"] = recept.Lek
            self.__prezime_labela["text"] = recept.Lekar
            self.__datum_labela["text"] = recept.datum
            self.__lbo_labela["text"] = recept.kolicina

            self.listapacijenata.delete(indeks)
            self.listapacijenata.insert(indeks, "  " + pacijent_izmena.prezime + " \t \t \t " + pacijent_izmena.ime)
            self.listapacijenata.selection_set(indeks)

            self.b_prihvati_izmenu['state'] = DISABLED

            self.__pacijentTxt.set("")
            self.__imeTxt.set("")
            self.__prezimeTxt.set("")
            self.__kolicinaInt.set("")

        def ocisti_labele(self):
            self.__jmbg_labela['text'] = ""
            self.__ime_labela['text'] = ""
            self.__prezime_labela['text'] = ""
            self.__datum_labela['text'] = ""
            self.__lbo_labela['text'] = ""
            self.__izvestaj_labela['text'] = ""
            self.e_pacijent.config(state="normal")
            self.e_kolicina.config(state="normal")

        def izbrisi_komanda(self):
            
            if tkinter.messagebox.askyesno("Upozorenje", "Ovom komandom cete obrisati recept",
                                           icon='warning') == "no":
                return

            pacijent_izmena = self.listapacijenata.curselection()[0]
            self.__podaciUcitaj.obrisi_recept(pacijent_izmena)

            Podaci.sacuvaj(self.__podaciUcitaj)

            self.listapacijenata.delete(pacijent_izmena)
            self.listapacijenata.selection_set(pacijent_izmena)

        def popuni_labele(self, recept):
            self.__jmbg_labela["text"] = recept.pacijent
            self.__ime_labela["text"] = recept.Lek
            self.__prezime_labela["text"] = recept.Lekar
            self.__datum_labela["text"] = recept.datum
            self.__lbo_labela["text"] = str(recept.kolicina)
            self.__izvestaj_labela['text'] = recept.izvestaj

        def promena_selekcije_u_listbox(self, event=None):
            if not self.listapacijenata.curselection():
                self.ocisti_labele()
                return

            indeks = self.listapacijenata.curselection()[0]
            pacijent = self.__podaciUcitaj.recepti[indeks]
            self.popuni_labele(pacijent)

        def popuni_listbox(self, recepti):
            self.listapacijenata.delete(0, END)
            for recept in recepti:
                self.listapacijenata.insert(END, "  " + recept.pacijent + " | " + recept.Lek)


if __name__ == '__main__':
    main()