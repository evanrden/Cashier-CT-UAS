from tkinter import *

MainPage = Tk()

MainPage.title("Masakan Padang Gogo")
MainPage.minsize(width=500, height=700)
MainPage.configure(bg="white")

def button_clicked():
    RendangTotal = int(RendangSpin.get()) * 5
    AyamPopTotal = int(AyamPopSpin.get()) * 15
    SatePadangTotal = int(SatePadangSpin.get()) * 11
    KeripikKulitSapiTotal = int(KeripikKulitSapiSpin.get()) * 5
    AyamGulaiTotal = int(AyamGulaiSpin.get()) * 16
    ParuTotal = int(ParuSpin.get()) * 5
    TempeGorengTotal = int(TempeGorengSpin.get()) * 3
    PerkedelTotal = int(PerkedelSpin.get()) * 4
    BaladoCumiAsinTotal = int(BaladoCumiAsinSpin.get()) * 3
    UdangPedasManisTotal = int(UdangPedasManisSpin.get()) * 1
    DendengLadoTotal = int(DendengLadoSpin.get()) * 3
    TotalBill = RendangTotal + AyamPopTotal + SatePadangTotal + KeripikKulitSapiTotal + AyamGulaiTotal + ParuTotal + TempeGorengTotal + PerkedelTotal + BaladoCumiAsinTotal + UdangPedasManisTotal + DendengLadoTotal
    Bill = Label(text=f'Your Total Bill ${TotalBill}', font=("Didot", 16, "bold"), bg="white")
    Bill.place(x=350, y=600)
RestoName = Label(text='Masakan Padang Bang Gogo', font=("Didot", 18, "bold"), bg="white")
RestoName.grid(column=1, row=0)

quote = Label(text="Masakan Padang berkualitas dengan harga ekonomis", font=("Didot", 16, "bold"), bg="white")
quote.grid(column=1, row=2)


FoodLabel = Label(text='Pilih makanan', font=("Didot", 16, "bold"), bg="white")
FoodLabel.grid(column=0, row=3)

# row atas
Rendang = PhotoImage(file="")
RendangLabel = Label(image=Rendang, borderwidth=0)
RendangLabel.place(x=50, y=130)
RendangInfo = Label(text="Rendang pedas", font=("Didot", 10, "normal"), bg="white")
RendangInfo.place(x=40, y=230)
RendangPriceInfo = Label(text="5$", font=("Didot", 10, "normal"), bg="white")
RendangPriceInfo.place(x=80, y=250)
RendangSpin = Spinbox(from_=0, to=10, width=5)
RendangSpin.place(x=80, y=270)

AyamPop = PhotoImage(file="")
AyamPopLabel = Label(image=AyamPop, borderwidth=0)
AyamPopLabel.place(x=200, y=130)
AyamPopInfo = Label(text="Ayam Pop pedas", font=("Didot", 10, "normal"), bg="white")
AyamPopInfo.place(x=210, y=230)
AyamPopPriceInfo = Label(text="15$", font=("Didot", 10, "normal"), bg="white")
AyamPopPriceInfo.place(x=230, y=250)
AyamPopSpin = Spinbox(from_=0, to=10, width=5)
AyamPopSpin.place(x=230, y=270)

SatePadang = PhotoImage(file="")
SatePadangLabel = Label(image=SatePadang, borderwidth=0)
SatePadangLabel.place(x=350, y=130)
SatePadangInfo = Label(text="Sate Padang", font=("Didot", 10, "normal"), bg="white")
SatePadangInfo.place(x=340, y=230)
SatePadangPriceInfo = Label(text="11$", font=("Didot", 10, "normal"), bg="white")
SatePadangPriceInfo.place(x=380, y=250)
SatePadangSpin = Spinbox(from_=0, to=10, width=5)
SatePadangSpin.place(x=380, y=270)

KeripikKulitSapi = PhotoImage(file="")
KeripikKulitSapiLabel = Label(image=KeripikKulitSapi, borderwidth=0)
KeripikKulitSapiLabel.place(x=500, y=130)
KeripikKulitSapiInfo = Label(text="Keripik Sapi Gurih", font=("Didot", 10, "normal"), bg="white")
KeripikKulitSapiInfo.place(x=490, y=230)
KeripikKulitPriceInfo = Label(text="5$", font=("Didot", 10, "normal"), bg="white")
KeripikKulitPriceInfo.place(x=530, y=250)
KeripikKulitSapiSpin = Spinbox(from_=0, to=10, width=5)
KeripikKulitSapiSpin.place(x=530, y=270)

AyamGulai = PhotoImage(file="")
AyamGulaiLabel = Label(image=AyamGulai, borderwidth=0)
AyamGulaiLabel.place(x=650, y=130)
AyamGulaiInfo = Label(text="Ayam Gulai ", font=("Didot", 10, "normal"), bg="white")
AyamGulaiInfo.place(x=640, y=230)
AyamGulaiPriceInfo = Label(text="16$", font=("Didot", 10, "normal"), bg="white")
AyamGulaiPriceInfo.place(x=680, y=250)
AyamGulaiSpin = Spinbox(from_=0, to=10, width=5)
AyamGulaiSpin.place(x=680, y=270)

Paru = PhotoImage(file="")
ParuLabel = Label(image=Paru, borderwidth=0)
ParuLabel.place(x=800, y=130)
ParuInfo = Label(text="Paru ", font=("Didot", 10, "normal"), bg="white")
ParuInfo.place(x=790, y=230)
ParuPriceInfo = Label(text="5$", font=("Didot", 10, "normal"), bg="white")
ParuPriceInfo.place(x=830, y=250)
ParuSpin = Spinbox(from_=0, to=10, width=5)
ParuSpin.place(x=830, y=270)



Perkedel = PhotoImage(file="")
PerkedelLabel = Label(image=Perkedel, borderwidth=0)
PerkedelLabel.place(x=950, y=130)
PerkedelInfo = Label(text="Perkedel renyah ", font=("Didot", 10, "normal"), bg="white")
PerkedelInfo.place(x=940, y=230)
PerkedelPriceInfo = Label(text="4$", font=("Didot", 10, "normal"), bg="white")
PerkedelPriceInfo.place(x=980, y=250)
PerkedelSpin = Spinbox(from_=0, to=10, width=5)
PerkedelSpin.place(x=980, y=270)

TempeGoreng = PhotoImage(file="")
TempeGorengLabel = Label(image=TempeGoreng, borderwidth=0)
TempeGorengLabel.place(x=1100, y=130)
TempeGorengInfo = Label(text="Tempe Goreng ", font=("Didot", 10, "normal"), bg="white")
TempeGorengInfo.place(x=1090, y=230)
TempeGorengPriceInfo = Label(text="3$", font=("Didot", 10, "normal"), bg="white")
TempeGorengPriceInfo.place(x=1130, y=250)
TempeGorengSpin = Spinbox(from_=0, to=10, width=5)
TempeGorengSpin.place(x=1130, y=270)

#row bawah
BaladoCumiAsin = PhotoImage(file="")
BaladoCumiAsinLabel = Label(image=BaladoCumiAsin, borderwidth=0)
BaladoCumiAsinLabel.place(x=50, y=380)
BaladoCumiAsinInfo = Label(text="Cumi Balado Asin", font=("Didot", 10, "normal"), bg="white")
BaladoCumiAsinInfo.place(x=40, y=480)
BaladoCumiPriceInfo = Label(text="3$", font=("Didot", 10, "normal"), bg="white")
BaladoCumiPriceInfo.place(x=80, y=500)
BaladoCumiAsinSpin = Spinbox(from_=0, to=10, width=5)
BaladoCumiAsinSpin.place(x=80, y=520)

UdangPedasManis = PhotoImage(file="")
UdangPedasManisLabel = Label(image=UdangPedasManis, borderwidth=0)
UdangPedasManisLabel.place(x=200, y=380)
UdangPedasManisInfo = Label(text="Udang pedas dan manis", font=("Didot", 10, "normal"), bg="white")
UdangPedasManisInfo.place(x=190, y=480)
UdangPedasPriceInfo = Label(text="1$", font=("Didot", 10, "normal"), bg="white")
UdangPedasPriceInfo.place(x=230, y=500)
UdangPedasManisSpin = Spinbox(from_=0, to=10, width=5)
UdangPedasManisSpin.place(x=230, y=520)

DendengLado = PhotoImage(file="")
DendengLadoLabel = Label(image=DendengLado, borderwidth=0)
DendengLadoLabel.place(x=350, y=380)
DendengLadoInfo = Label(text="Dendeng Lado", font=("Didot", 10, "normal"), bg="white")
DendengLadoInfo.place(x=340, y=480)
DendengPriceInfo = Label(text="3$", font=("Didot", 10, "normal"), bg="white")
DendengPriceInfo.place(x=380, y=500)
DendengLadoSpin = Spinbox(from_=0, to=10, width=5)
DendengLadoSpin.place(x=380, y=520)

Finish = Button(text='Order', command=button_clicked)
Finish.place(x=350, y=560)
MainPage.mainloop()