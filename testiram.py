from tkinter import *
import tkinter.messagebox

class windows1:





    def __init__(self, master):
        self.master = master
        self.master.title("Ana Mandic Test")
        self.master.geometry("400x400+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()


        self.jmbgTxt = StringVar()
        self.imeTxt = StringVar()
        self.prezimeTxt = StringVar()

        unosFrame = Frame(self.master, bd=4, relief="groove", bg="whitesmoke")
        unosFrame.place(x=0, y=0, width=400, height=400)

        self.l_jmbg = Label(unosFrame, text="jmbg: ", font=("arial", 10, "bold"))
        self.l_jmbg.grid(row=1, column=0, pady=5, padx=10, sticky="W")

        e_jmbg = Entry(unosFrame, textvariable=self.jmbgTxt, bd=5, font=("arial", 10, "bold"))
        e_jmbg.grid(row=1, column=1, pady=5, padx=10, sticky="E")

        self.l_ime = Label(unosFrame, text="Ime: ", font=("arial", 10, "bold"))
        self.l_ime.grid(row=2, column=0, pady=5, padx=10, sticky="W")

        e_ime = Entry(unosFrame, textvariable=self.imeTxt, bd=5, font=("arial", 10, "bold"))
        e_ime.grid(row=2, column=1, pady=5, padx=10, sticky="E")

        self.l_prezime = Label(unosFrame, text="Prezime: ", font=("arial", 10, "bold"))
        self.l_prezime.grid(row=3, column=0, pady=5, padx=10, sticky="W")

        e_prezime = Entry(unosFrame, textvariable=self.prezimeTxt, bd=5, font=("arial", 10, "bold"))
        e_prezime.grid(row=3, column=1, pady=5, padx=10, sticky="E")

        proveri_b = Button(unosFrame, width = 10, height = 2, text = "Proveri", command = self.Accept)
        proveri_b.grid(row  = 4, column = 1)

        uvecaj_b = Button(unosFrame, width = 10, height = 2, text = "Proveri", command = self.Uvecaj)
        uvecaj_b.grid(row  = 5, column = 1)

        umanji_b = Button(unosFrame, width = 10, height = 2, text = "Proveri", command = self.Smanji)
        umanji_b.grid(row=6, column=1)

        umanji_ba = Combo(unosFrame, width=10, height=2, text="Proveri", command=self.Smanji)
        umanji_ba.grid(row=6, column=1)

    def Accept(self):

        jmbg_pr = self.jmbgTxt.get()
        ime_pr = self.imeTxt.get()
        prezime_pr = self.prezimeTxt.get()

        if len(jmbg_pr) != 13 or not jmbg_pr.isdigit():
            tkinter.messagebox.showwarning("Greska", "JMBG mora  biti broj i imati 13 karaktera!")

        if len(ime_pr) < 2 or ime_pr.isdigit():
            tkinter.messagebox.showwarning("Greska", "Ime mora imati bar 2 karaktera i ne imati brojeve!")

        if len(prezime_pr) < 2 or prezime_pr.isdigit():
            tkinter.messagebox.showwarning("Greska", "Prezime mora imati bar 2 karaktera i ne imati brojeve!")

    def Uvecaj(self):
        self.l_jmbg['text'] = "JMBG: "
        self.l_ime['text'] = "IME :"
        self.l_prezime["text"] = "PREZIME: "

    def Smanji(self):
        self.l_jmbg['text'] = "jmbg: "
        self.l_ime['text'] = "ime :"
        self.l_prezime["text"] = "prezime: "

def main():

    root = Tk()
    app = windows1(root)
    root.mainloop()

if __name__ == '__main__':
    main()