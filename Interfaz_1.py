#Flores Romero Andres Gael
#09/03/2023

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("600x450")

#--------------------MENU--------------------
#background="cyan3"
#background="gray55"

noteBook = ttk.Notebook(root)
tabAD = ttk.Frame(noteBook)
tabDelete = ttk.Frame(noteBook)
tabSearch = ttk.Frame(noteBook)
tabService = ttk.Frame(noteBook)
tabHelp = ttk.Frame(noteBook)

noteBook.pack_configure(expand=True, fill="both")

#Pestañas
noteBook.add(tabAD, text="                  ADD                 ")
noteBook.add(tabDelete, text="                  Delete              ")
noteBook.add(tabSearch, text="              Search                  ")
noteBook.add(tabService, text="                 Service                 ")
noteBook.add(tabHelp, text="                    Help                    ")

style = ttk.Style()
style.theme_create("MyStyle", parent="alt", settings={
    "TNotebook.Tab": {
        "configure": {"background": "cyan3", "foreground": "black"},
        "map": {"background": [("selected", "deep sky blue")], "foreground": [("selected", "white")]}
    }
})
style.theme_use("MyStyle")

#--------------------FRAMES--------------------
BaseFrame = ttk.Frame(tabAD, padding="5 5 5 5")
BaseFrame.grid(column=0, row= 0)

Frame2 = ttk.Frame(BaseFrame, padding="40 30 40 30", relief="groove")
Frame2.grid(column=0, row=1)

Frame3 = ttk.Frame(Frame2)
Frame3.grid(column=1, row=1, sticky=(W), padx=5, pady=5)

Frame4 = ttk.Frame(BaseFrame, padding="40 30 202 30", relief="groove")
Frame4.grid(column=0, row=2, sticky=(W))

Frame5 = ttk.Frame(BaseFrame, padding="40 30 165 30", relief="groove")
Frame5.grid(column=0, row=3, sticky=(W))

Frame6 = ttk.Frame(BaseFrame, padding="272 30 272 30")
Frame6.grid(column=0, row=4, sticky=(W))

#--------------------DATOS---------------------

#Segundo Frame
FName = StringVar()
LName = StringVar()
Country = StringVar()

#Tercer Frame 
Dia = IntVar()
Mes = StringVar()
Año = IntVar()

#Cuarto Frame
Credit = IntVar()

#Quinto Frame
Days = IntVar()

#--------------------LABELS--------------------

#Segundo Frame

ttk.Label(Frame2, text="First Name: ").grid(column=0, row=0,sticky=(W))
ttk.Label(Frame2, text="Last Name: ").grid(column=2, row=0,sticky=(W),padx=5)

#Tercer Frame
ttk.Label(Frame2, text="Birth Date ").grid(column=0, row=1, sticky=(W))
ttk.Label(Frame2, text="Country: ").grid(column=2, row=1, sticky=(W), padx=5)

#Cuarto Frame
ttk.Label(Frame4, text="Credir Card (if any): ").grid(column=0,row=0,sticky=(W))
ttk.Label(Frame4, text="Type Credit Card (if any): ").grid(column=0, row=1,sticky=(W), pady=2)

#Quinto Frame
ttk.Label(Frame5, text="RoomType: ").grid(column=0, row=0, sticky=(W))
ttk.Label(Frame5, text="Total Staying Time (days): ").grid(column=3, row=0,sticky=(W), padx=20)

#--------------------ENTRYS--------------------

#Segundo Frame
FirstNameEntry = ttk.Entry(Frame2, textvariable=FName, width=28).grid(column=1, row=0, sticky=(W),padx=5)
LastNameEntry = ttk.Entry(Frame2, textvariable=LName, width=28).grid(column=3, row=0, sticky=(W),padx=5)
CountryEntry = ttk.Entry(Frame2,textvariable=Country, width=28).grid(column=3, row=1, sticky=(W),padx=5)

#Cuarto Frame
CreditEntry = ttk.Entry(Frame4, textvariable=Credit, width=28).grid(column=1, row=0, sticky=(W),padx=5)

#Quinto Frame
CreditEntry = ttk.Entry(Frame5,textvariable= Days, width=10).grid(column=4, row=0)
#--------------------COMBO BOX--------------------
DiaBox = ttk.Combobox(Frame3, textvariable=Dia, width=3)
DiaBox.grid(column=0, row=0, sticky=(W))
DiaBox['values'] = tuple (range(1, 32))

MesBox = ttk.Combobox(Frame3, textvariable=Mes, width=8)
MesBox.grid(column=1, row=0, sticky=(W), padx=2)
MesBox['values'] = ("January","February","March","April","May","June","July","August","September",
                    "Octuber","November","December")

AñoBox = ttk.Combobox(Frame3, textvariable=Año, width=8)
AñoBox.grid(column=2, row= 0,sticky=(W), padx=2)
AñoBox['values'] = tuple (range(1923,2024))

#--------------------RADIO BOTTON--------------------

#Frame 4
ttk.Radiobutton(Frame4, text="Visa").grid(column=1, row=1, sticky=(W), pady=2, padx=15)
ttk.Radiobutton(Frame4, text="MasterCard").grid(column=1, row=1, sticky=(W), pady=2 ,padx=65)

#Frame 5
ttk.Radiobutton(Frame5, text="Nomral").grid(column=1, row=0, sticky=(W), padx=5)
ttk.Radiobutton(Frame5, text="Familiar").grid(column=1, row=1, sticky=(W), padx=5)
ttk.Radiobutton(Frame5, text="Special").grid(column=1, row=2, sticky=(W), padx=5)

#--------------------BOTTON--------------------
Boton = ttk.Button(Frame6, text= "Submit").grid(column=2, row=4, sticky=(S))

root.mainloop()