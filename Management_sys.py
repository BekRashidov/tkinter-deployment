from tkinter import *
import random
import time
import datetime
from tkinter import messagebox

root = Tk()
root.geometry("1350x750+0+0")
root.title("  Simit Factory Management System  ")
root.configure(background='#BBDFFA')

Tops = Frame(root, width=1350, height=100, bd=14, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root, width=440, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a = Frame(f1, width=900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)

f2a = Frame(f1, width=900, height=320, bd=6, relief="raise")
f2a.pack(side=BOTTOM)

ft2 = Frame(f2, width=440, height=450, bd=12, bg='#1727AE', relief="raise")
ft2.pack(side=TOP)
fb2 = Frame(f2, width=440, height=250, bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=330, bd=16, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=330, bd=16, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=14, relief="raise")
f2aa.pack(side=LEFT)

f2ab = Frame(f2a, width=450, height=330, bd=14, relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background='#BBDFFA')
f1.configure(background='#BBDFFA')
f2.configure(background='#BBDFFA')

lblInfo = Label(Tops, font=('arial', 50, 'bold'), bg='#97BAEC', text="Simit Cafeteria Management System", bd=10)
lblInfo.grid(row=0, column=0)


# =============================================METHODS=====================================================
def CostofItems():
    Item1 = float(E_Latte.get())
    Item2 = float(E_Espresso.get())
    Item3 = float(E_Ice_Latte.get())
    Item4 = float(E_Vale_Coffee.get())
    Item5 = float(E_Cappuccino.get())
    Item6 = float(E_African_Coffee.get())
    Item7 = float(E_American_Coffee.get())
    Item8 = float(E_Iced_Cappuccino.get())

    Item9 = float(E_Coffee_cake.get())
    Item10 = float(E_Red_Velvet_Cake.get())
    Item11 = float(E_Black_Forest_Cake.get())
    Item12 = float(E_Boston_Cream_Cake.get())
    Item13 = float(E_Lagos_Chocolate_Cake.get())
    Item14 = float(E_Kilburn_Chocolate_Cake.get())
    Item15 = float(E_Carlton_Hill_Cake.get())
    Item16 = float(E_Queen_Park_Cake.get())

    PriceofDrinks = (Item1 * 1.2) + (Item2 * 1.99) + (Item3 * 2.05) + (Item4 * 1.89) + (Item5 * 1.99) + (Item6 * 2.99) \
                    + (Item7 * 2.39) + (Item8 * 1.29)

    PriceofCakes = (Item9 * 1.35) + (Item10 * 2.2) + (Item11 * 1.99) \
                   + (Item12 * 1.49) + (Item13 * 1.8) + (Item14 * 1.67) + (Item15 * 1.6) + (Item16 * 1.99)

    DrinksPrice = "$", str('%.2f' % PriceofDrinks)
    CakesPrice = "$", str('%.2f' % PriceofCakes)
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC = "$", str('%.2f' % 1.59)
    ServiceCharge.set(SC)

    SubTotalofItems = "$", str('%.2f' % (PriceofDrinks + PriceofCakes + 1.59))
    SubTotal.set(SubTotalofItems)

    Tax = "$", str('%.2f' % ((PriceofDrinks + PriceofCakes + 1.59) * 0.15))
    PaidTax.set(Tax)

    TT = ((PriceofDrinks + PriceofCakes + 1.59) * 0.15)
    TC = "$", str('%.2f' % (PriceofDrinks + PriceofCakes + 1.59 + TT))
    TotalCost.set(TC)


def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + Receipt_Ref.get() + '\t\t' + DateofOrder.get() + "\n")
    txtReceipt.insert(END, 'Items\t\t\t\t\t' + "Cost of Items \n\n")
    txtReceipt.insert(END, 'Latte: \t\t\t\t\t' + E_Latte.get() + "\n")
    txtReceipt.insert(END, 'Espresso: \t\t\t\t\t' + E_Espresso.get() + "\n")
    txtReceipt.insert(END, 'Ice Latte: \t\t\t\t\t' + E_Ice_Latte.get() + "\n")
    txtReceipt.insert(END, 'Vale Coffee: \t\t\t\t\t' + E_Vale_Coffee.get() + "\n")
    txtReceipt.insert(END, 'Cappuccino: \t\t\t\t\t' + E_Cappuccino.get() + "\n")
    txtReceipt.insert(END, 'African Coffee: \t\t\t\t\t' + E_African_Coffee.get() + "\n")
    txtReceipt.insert(END, 'American Coffee: \t\t\t\t\t' + E_American_Coffee.get() + "\n")
    txtReceipt.insert(END, 'Iced Cappuccino: \t\t\t\t\t' + E_Iced_Cappuccino.get() + "\n")
    txtReceipt.insert(END, 'Coffee Cake: \t\t\t\t\t' + E_Coffee_cake.get() + "\n")
    txtReceipt.insert(END, 'Red Velvet Cake: \t\t\t\t\t' + E_Red_Velvet_Cake.get() + "\n")
    txtReceipt.insert(END, 'Black Forest Cake: \t\t\t\t\t' + E_Black_Forest_Cake.get() + "\n")
    txtReceipt.insert(END, 'Boston Cream Cake: \t\t\t\t\t' + E_Boston_Cream_Cake.get() + "\n")
    txtReceipt.insert(END, 'Lagos Chocolate Cake: \t\t\t\t\t' + E_Lagos_Chocolate_Cake.get() + "\n")
    txtReceipt.insert(END, 'Kilburn Chocolate Cake: \t\t\t\t\t' + E_Kilburn_Chocolate_Cake.get() + "\n")
    txtReceipt.insert(END, 'Carlton Hill Chocolate Cake: \t\t\t\t\t' + E_Carlton_Hill_Cake.get() + "\n")
    txtReceipt.insert(END, 'Queens Park Chocolate Cake: \t\t\t\t\t' + E_Queen_Park_Cake.get() + "\n")
    txtReceipt.insert(END, 'Cost of Drinks: \t\t' + CostofDrinks.get() + '\tTax Paid:\t\t' + PaidTax.get() + "\n")
    txtReceipt.insert(END, 'Cost of Cakes: \t\t' + CostofCakes.get() + '\tSub Total: \t\t' + SubTotal.get() + "\n")
    txtReceipt.insert(END, 'Service Charge: \t\t' + ServiceCharge.get() + '\tTotal Cost: \t\t' + TotalCost.get() + "\n")


def qExit():
    qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return


def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)

    E_Latte.set("0")
    E_Espresso.set("0")
    E_Ice_Latte.set("0")
    E_Vale_Coffee.set("0")
    E_Cappuccino.set("0")
    E_African_Coffee.set("0")
    E_American_Coffee.set("0")
    E_Iced_Cappuccino.set("0")
    E_Coffee_cake.set("0")
    E_Red_Velvet_Cake.set("0")
    E_Queen_Park_Cake.set("0")
    E_Black_Forest_Cake.set("0")
    E_Boston_Cream_Cake.set("0")
    E_Lagos_Chocolate_Cake.set("0")
    E_Kilburn_Chocolate_Cake.set("0")
    E_Carlton_Hill_Cake.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtLatte.configure(state=DISABLED)
    txtEspresso.configure(state=DISABLED)
    txtIce_Latte.configure(state=DISABLED)
    txtVale_Coffee.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtAfrican_Coffee.configure(state=DISABLED)
    txtAmerican_Coffee.configure(state=DISABLED)
    txtIced_Cappuccino.configure(state=DISABLED)
    txtCoffee_cake.configure(state=DISABLED)
    txtRed_Velvet_Cake.configure(state=DISABLED)
    txtQueen_Park_Cake.configure(state=DISABLED)
    txtBlack_Forest_Cake.configure(state=DISABLED)
    txtBoston_Cream_Cake.configure(state=DISABLED)
    txtLagos_Chocolate_Cake.configure(state=DISABLED)
    txtKilburn_Chocolate_Cake.configure(state=DISABLED)
    txtCarlton_Hill_Cake.configure(state=DISABLED)


# =======================================Receipt========================================================
# =======================================CHECKBUTTON========================================================
def chkbutton_value():
    if (var1.get() == 1):
        txtLatte.configure(state=NORMAL)
    elif var1.get() == 0:
        txtLatte.configure(state=DISABLED)
        E_Latte.set("0")
    if (var2.get() == 1):
        txtEspresso.configure(state=NORMAL)
    elif var2.get() == 0:
        txtEspresso.configure(state=DISABLED)
        E_Espresso.set("0")
    if (var3.get() == 1):
        txtIce_Latte.configure(state=NORMAL)
    elif var3.get() == 0:
        txtIce_Latte.configure(state=DISABLED)
        E_Ice_Latte.set("0")
    if (var4.get() == 1):
        txtVale_Coffee.configure(state=NORMAL)
    elif var4.get() == 0:
        txtVale_Coffee.configure(state=DISABLED)
        E_Vale_Coffee.set("0")
    if (var5.get() == 1):
        txtCappuccino.configure(state=NORMAL)
    elif var5.get() == 0:
        txtCappuccino.configure(state=DISABLED)
        E_Cappuccino.set("0")
    if (var6.get() == 1):
        txtAfrican_Coffee.configure(state=NORMAL)
    elif var6.get() == 0:
        txtAfrican_Coffee.configure(state=DISABLED)
        E_African_Coffee.set("0")
    if (var7.get() == 1):
        txtAmerican_Coffee.configure(state=NORMAL)
    elif var7.get() == 0:
        txtAmerican_Coffee.configure(state=DISABLED)
        E_American_Coffee.set("0")
    if (var8.get() == 1):
        txtIced_Cappuccino.configure(state=NORMAL)
    elif var8.get() == 0:
        txtIced_Cappuccino.configure(state=DISABLED)
        E_Iced_Cappuccino.set("0")
    if (var9.get() == 1):
        txtCoffee_cake.configure(state=NORMAL)
    elif var9.get() == 0:
        txtCoffee_cake.configure(state=DISABLED)
        E_Coffee_cake.set("0")
    if (var10.get() == 1):
        txtRed_Velvet_Cake.configure(state=NORMAL)
    elif var10.get() == 0:
        txtRed_Velvet_Cake.configure(state=DISABLED)
        E_Red_Velvet_Cake.set("0")
    if (var11.get() == 1):
        txtQueen_Park_Cake.configure(state=NORMAL)
    elif var11.get() == 0:
        txtQueen_Park_Cake.configure(state=DISABLED)
        E_Queen_Park_Cake.set("0")
    if (var12.get() == 1):
        txtBlack_Forest_Cake.configure(state=NORMAL)
    elif var12.get() == 0:
        txtBlack_Forest_Cake.configure(state=DISABLED)
        E_Black_Forest_Cake.set("0")
    if (var13.get() == 1):
        txtBoston_Cream_Cake.configure(state=NORMAL)
    elif var13.get() == 0:
        txtBoston_Cream_Cake.configure(state=DISABLED)
        E_Boston_Cream_Cake.set("0")
    if (var14.get() == 1):
        txtLagos_Chocolate_Cake.configure(state=NORMAL)
    elif var14.get() == 0:
        txtLagos_Chocolate_Cake.configure(state=DISABLED)
        E_Lagos_Chocolate_Cake.set("0")
    if (var15.get() == 1):
        txtKilburn_Chocolate_Cake.configure(state=NORMAL)
    elif var15.get() == 0:
        txtKilburn_Chocolate_Cake.configure(state=DISABLED)
        E_Kilburn_Chocolate_Cake.set("0")
    if (var16.get() == 1):
        txtCarlton_Hill_Cake.configure(state=NORMAL)
    elif var16.get() == 0:
        txtCarlton_Hill_Cake.configure(state=DISABLED)
        E_Carlton_Hill_Cake.set("0")


# =============================================VARIABLES=====================================================
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

E_Latte = StringVar()
E_Espresso = StringVar()
E_Ice_Latte = StringVar()
E_Vale_Coffee = StringVar()
E_Cappuccino = StringVar()
E_African_Coffee = StringVar()
E_American_Coffee = StringVar()
E_Iced_Cappuccino = StringVar()

E_Coffee_cake = StringVar()
E_Red_Velvet_Cake = StringVar()
E_Queen_Park_Cake = StringVar()
E_Black_Forest_Cake = StringVar()
E_Boston_Cream_Cake = StringVar()
E_Lagos_Chocolate_Cake = StringVar()
E_Kilburn_Chocolate_Cake = StringVar()
E_Carlton_Hill_Cake = StringVar()

E_Latte.set("0")
E_Espresso.set("0")
E_Ice_Latte.set("0")
E_Vale_Coffee.set("0")
E_Cappuccino.set("0")
E_African_Coffee.set("0")
E_American_Coffee.set("0")
E_Iced_Cappuccino.set("0")
E_Coffee_cake.set("0")
E_Red_Velvet_Cake.set("0")
E_Queen_Park_Cake.set("0")
E_Black_Forest_Cake.set("0")
E_Boston_Cream_Cake.set("0")
E_Lagos_Chocolate_Cake.set("0")
E_Kilburn_Chocolate_Cake.set("0")
E_Carlton_Hill_Cake.set("0")

DateofOrder.set(time.strftime("%d/%m/%Y"))

# =========================Drinks================================================
Latte = Checkbutton(f1aa, text="Latte \t", variable=var1, onvalue=1, offvalue=0,
                    font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=0, sticky=W)
Espresso = Checkbutton(f1aa, text="Espresso \t", variable=var2, onvalue=1, offvalue=0,
                       font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=1, sticky=W)
Ice_Latte = Checkbutton(f1aa, text="Ice Latte \t", variable=var3, onvalue=1, offvalue=0,
                        font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=2, sticky=W)
Vale_Coffee = Checkbutton(f1aa, text="Vale Coffee \t", variable=var4, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=3, sticky=W)
Cappuccino = Checkbutton(f1aa, text="Cappuccino \t", variable=var5, onvalue=1, offvalue=0,
                         font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=4, sticky=W)
African_Coffee = Checkbutton(f1aa, text="African Coffee \t", variable=var6, onvalue=1, offvalue=0,
                             font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=5, sticky=W)
American_Coffee = Checkbutton(f1aa, text="American Coffee \t", variable=var7, onvalue=1, offvalue=0,
                              font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=6, sticky=W)
Iced_Cappuccino = Checkbutton(f1aa, text="Ice Cappuccino \t", variable=var8, onvalue=1, offvalue=0,
                              font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=7, sticky=W)
# =========================Cakes================================================

# =========================Enter widget for Drinks================================================
txtLatte = Entry(f1aa, font=('arial', 16, 'bold'), bg='#6987D5', bd=8, width=6, justify='left', textvariable=E_Latte, state=DISABLED)
txtLatte.grid(row=0, column=1)
txtEspresso = Entry(f1aa, font=('arial', 16, 'bold'),bg='#6987D5', bd=8, width=6, justify='left', textvariable=E_Espresso,
                    state=DISABLED)
txtEspresso.grid(row=1, column=1)
txtIce_Latte = Entry(f1aa, font=('arial', 16, 'bold'), bg='#6987D5', bd=8, width=6, justify='left', textvariable=E_Ice_Latte,
                     state=DISABLED)
txtIce_Latte.grid(row=2, column=1)
txtVale_Coffee = Entry(f1aa, font=('arial', 16, 'bold'),bg='#6987D5', bd=8, width=6, justify='left', textvariable=E_Vale_Coffee,
                       state=DISABLED)
txtVale_Coffee.grid(row=3, column=1)
txtCappuccino = Entry(f1aa, font=('arial', 16, 'bold'),bg='#6987D5', bd=8, width=6, justify='left', textvariable=E_Cappuccino,
                      state=DISABLED)
txtCappuccino.grid(row=4, column=1)
txtAfrican_Coffee = Entry(f1aa, font=('arial', 16, 'bold'),bg='#6987D5', bd=8, width=6, justify='left',
                          textvariable=E_African_Coffee, state=DISABLED)
txtAfrican_Coffee.grid(row=5, column=1)
txtAmerican_Coffee = Entry(f1aa, font=('arial', 16, 'bold'),bg='#6987D5', bd=8, width=6, justify='left',
                           textvariable=E_American_Coffee, state=DISABLED)
txtAmerican_Coffee.grid(row=6, column=1)
txtIced_Cappuccino = Entry(f1aa, font=('arial', 16, 'bold'),bg='#6987D5', bd=8, width=6, justify='left',
                           textvariable=E_Iced_Cappuccino, state=DISABLED)
txtIced_Cappuccino.grid(row=7, column=1)
# -------------------------------------------------------------------------------------------------
Coffee_cake = Checkbutton(f1ab, text="Coffee Cake \t", variable=var9, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=0, sticky=W)
Red_Velvet_Cake = Checkbutton(f1ab, text="Red Velvet Cake \t", variable=var10, onvalue=1, offvalue=0,
                              font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=1, sticky=W)
Queen_Park_Cake = Checkbutton(f1ab, text="Queen`s Park Cake  \t", variable=var11, onvalue=1, offvalue=0,
                              font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=2, sticky=W)
Black_Forest_Cake = Checkbutton(f1ab, text="Black Forest Cake \t", variable=var12, onvalue=1, offvalue=0,
                                font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=3, sticky=W)
Boston_Cream_Cake = Checkbutton(f1ab, text="Boston Cream Cake \t", variable=var13, onvalue=1, offvalue=0,
                                font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=4, sticky=W)
Lagos_Chocolate_Cake = Checkbutton(f1ab, text="Lagos Chocolate Cake \t", variable=var14, onvalue=1, offvalue=0,
                                   font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=5, sticky=W)
Kilburn_Chocolate_Cake = Checkbutton(f1ab, text="Kilburn Chocolate Cake \t", variable=var15, onvalue=1, offvalue=0,
                                     font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=6, sticky=W)
Carlton_Hill_Cake = Checkbutton(f1ab, text="Carlton Hill Cake \t", variable=var16, onvalue=1, offvalue=0,
                                font=('arial', 18, 'bold'), command=chkbutton_value).grid(row=7, sticky=W)
# =========================Enter widget Cakes================================================
txtCoffee_cake = Entry(f1ab, font=('arial', 16, 'bold'),bg='#6987D5', bd=8, width=6, justify='left', textvariable=E_Coffee_cake,
                       state=DISABLED)
txtCoffee_cake.grid(row=0, column=1)
txtRed_Velvet_Cake = Entry(f1ab, font=('arial', 16, 'bold'),bg='#6987D5', bd=8, width=6, justify='left',
                           textvariable=E_Red_Velvet_Cake, state=DISABLED)
txtRed_Velvet_Cake.grid(row=1, column=1)
txtQueen_Park_Cake = Entry(f1ab, font=('arial', 16, 'bold'),bg='#6987D5', bd=8, width=6, justify='left',
                           textvariable=E_Queen_Park_Cake, state=DISABLED)
txtQueen_Park_Cake.grid(row=2, column=1)
txtBlack_Forest_Cake = Entry(f1ab, font=('arial', 16, 'bold'),bg='#6987D5', bd=8, width=6, justify='left',
                             textvariable=E_Black_Forest_Cake, state=DISABLED)
txtBlack_Forest_Cake.grid(row=3, column=1)
txtBoston_Cream_Cake = Entry(f1ab, font=('arial', 16, 'bold'),bg='#6987D5', bd=8, width=6, justify='left',
                             textvariable=E_Boston_Cream_Cake, state=DISABLED)
txtBoston_Cream_Cake.grid(row=4, column=1)
txtLagos_Chocolate_Cake = Entry(f1ab, font=('arial', 16, 'bold'),bg='#6987D5', bd=8, width=6, justify='left',
                                textvariable=E_Lagos_Chocolate_Cake, state=DISABLED)
txtLagos_Chocolate_Cake.grid(row=5, column=1)
txtKilburn_Chocolate_Cake = Entry(f1ab, font=('arial', 16, 'bold'),bg='#6987D5', bd=8, width=6, justify='left',
                                  textvariable=E_Kilburn_Chocolate_Cake, state=DISABLED)
txtKilburn_Chocolate_Cake.grid(row=6, column=1)
txtCarlton_Hill_Cake = Entry(f1ab, font=('arial', 16, 'bold'),bg='#6987D5', bd=8, width=6, justify='left',
                             textvariable=E_Carlton_Hill_Cake, state=DISABLED)
txtCarlton_Hill_Cake.grid(row=7, column=1)

# ========================================================COST ITEM INFORMATION========================================
lblCostofDrinks = Label(f2aa, font=('arial', 16, 'bold'), text="Cost Of Drinks", bd=8, anchor='w')
lblCostofDrinks.grid(row=2, column=0, sticky=W)
txtCostofDrinks = Entry(f2aa, font=('arial', 16, 'bold'), insertwidth=2, justify='left', textvariable=CostofDrinks,
                        bd=8, bg='#BBDFFA')
txtCostofDrinks.grid(row=2, column=1)

lblCostofCakes = Label(f2aa, font=('arial', 16, 'bold'), text="Cost Of Cakes", bd=8, anchor='w')
lblCostofCakes.grid(row=3, column=0, sticky=W)
txtCostofCakes = Entry(f2aa, font=('arial', 16, 'bold'), insertwidth=2, justify='left', textvariable=CostofCakes, bd=8, bg='#BBDFFA')
txtCostofCakes.grid(row=3, column=1)

lblServiceCharge = Label(f2aa, font=('arial', 16, 'bold'), text="Service Charge", bd=8, anchor='w')
lblServiceCharge.grid(row=4, column=0, sticky=W)
txtServiceCharge = Entry(f2aa, font=('arial', 16, 'bold'), insertwidth=2, justify='left', bd=8, bg='#BBDFFA')
txtServiceCharge.grid(row=4, column=1)

# ========================================================PAYMENT INFORMATION==========================================
lblPaidTax = Label(f2ab, font=('arial', 16, 'bold'), text=" PAID TAX", bd=8)
lblPaidTax.grid(row=2, column=0, sticky=W)
txtPaidTax = Entry(f2ab, font=('arial', 16, 'bold'), insertwidth=2, justify='left', textvariable=PaidTax, bd=8, bg='#BBDFFA')
txtPaidTax.grid(row=2, column=1)

lblSubTotal = Label(f2ab, font=('arial', 16, 'bold'), text="Sub Total", bd=8)
lblSubTotal.grid(row=3, column=0, sticky=W)
txtSubTotal = Entry(f2ab, font=('arial', 16, 'bold'), insertwidth=2, textvariable=SubTotal, justify='left', bd=8, bg='#BBDFFA')
txtSubTotal.grid(row=3, column=1)

lblTotalCost = Label(f2ab, font=('arial', 16, 'bold'), text="Total", bd=8)
lblTotalCost.grid(row=4, column=0, sticky=W)
txtTotalCost = Entry(f2ab, font=('arial', 16, 'bold'), insertwidth=2, textvariable=TotalCost, justify='left', bd=8, bg='#BBDFFA')
txtTotalCost.grid(row=4, column=1)
# ========================================================ft2=======================================================
lblReceipt = Label(ft2, font=('arial', 12, 'bold'), text="Receipt: ", bd=2, anchor='w')
lblReceipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(ft2, width=59, height=22, bg="white", font=('arial', 11, 'bold'), bd=8, )
txtReceipt.grid(row=1, column=0)
# ========================================================fb2=======================================================
btnTotal = Button(fb2, padx=16, pady=1, bd=4, fg='black', font=('arial', 13, 'bold'), command=CostofItems, width=5,
                  text="Total ", bg='#445BC1').grid(row=0, column=0)
btnReceipt = Button(fb2, padx=16, pady=1, bd=4, fg='black', font=('arial', 13, 'bold'), width=5,
                    text="Receipt", bg='#445BC1', command=Receipt).grid(row=0, column=1)
btnReset = Button(fb2, padx=16, pady=1, bd=4, fg='black', font=('arial', 13, 'bold'), width=5,
                  text="Reset",bg='#445BC1', command=Reset).grid(row=0, column=2)
btnExit = Button(fb2, padx=16, pady=1, bd=4, fg='black', font=('arial', 13, 'bold'), width=3,
                 text="Exit",bg='#445BC1', command=qExit).grid(row=0, column=3)

root.mainloop()
