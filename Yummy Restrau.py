from tkinter import *

root = Tk()
root.geometry("600x500+0+0")
root.title("Yummy Restrau")

Head_Label = Label(root, text = "Yummy Restrau", font = "Arial 25 bold").place(x=175, y=0)
Menu_Label = Label(root, text = "Menu", font = "Arial 15 bold underline").place(x=260, y=85)
Items_Label = Label(root, text = "Items", font = "Arial 13 bold").place(x=40, y=140)
Rate_Label = Label(root, text = "Rate", font = "Arial 13 bold").place(x=250, y=140)
Quantity_Label = Label(root, text = "Quantity", font = "Arial 13 bold").place(x=325, y=140)
Amount_Label = Label(root, text = "Amount", font = "Arial 13 bold").place(x=450, y=140)

#check button variable
chkbtn_idlisambar_variable = IntVar()
chkbtn_masaladosa_variable = IntVar()
chkbtn_cholebhature_variable = IntVar()
chkbtn_rajkachori_variable = IntVar()
chkbtn_dahisamosa_variable = IntVar()
chkbtn_panipuri_variable = IntVar()
chkbtn_bhelpuri_variable = IntVar()

#items
chkbtn_idlisambar = Checkbutton(root, text = "IDLI SAMBAR", font = "Arial 10 bold", variable = chkbtn_idlisambar_variable, onvalue = 1, offvalue = 0).place(x=20, y=170)
chkbtn_masaladosa = Checkbutton(root, text = "MASALA DOSA", font = "Arial 10 bold", variable = chkbtn_masaladosa_variable, onvalue = 1, offvalue = 0).place(x=20, y=200)
chkbtn_cholebhature = Checkbutton(root, text = "CHOLE BHATURE", font = "Arial 10 bold", variable = chkbtn_cholebhature_variable, onvalue = 1, offvalue = 0).place(x=20, y=230)
chkbtn_rajkachori = Checkbutton(root, text = "RAJ KACHORI", font = "Arial 10 bold", variable = chkbtn_rajkachori_variable, onvalue = 1, offvalue = 0).place(x=20, y=260)
chkbtn_dahisamosa = Checkbutton(root, text = "DAHI SAMOSA", font = "Arial 10 bold", variable = chkbtn_dahisamosa_variable, onvalue = 1, offvalue = 0).place(x=20, y=290)
chkbtn_panipuri = Checkbutton(root, text = "PANI PURI", font = "Arial 10 bold", variable = chkbtn_panipuri_variable, onvalue = 1, offvalue = 0).place(x=20, y=320)
chkbtn_bhelpuri = Checkbutton(root, text = "BHEL PURI", font = "Arial 10 bold", variable = chkbtn_bhelpuri_variable, onvalue = 1, offvalue = 0).place(x=20, y=350)

#item rates
rate_idlisambar = Label(root, text = "Rs 50", font = "Arial 10 bold").place(x=250, y=170)
rate_masaladosa = Label(root, text = "Rs 80", font = "Arial 10 bold").place(x=250, y=200)
rate_cholebhature = Label(root, text = "Rs 142", font = "Arial 10 bold").place(x=250, y=230)
rate_rajkachori = Label(root, text = "Rs 95", font = "Arial 10 bold").place(x=250, y=260)
rate_dahisamosa = Label(root, text = "Rs 76", font = "Arial 10 bold").place(x=250, y=290)
rate_panipuri = Label(root, text = "Rs 70", font = "Arial 10 bold").place(x=250, y=320)
rate_bhelpuri = Label(root, text = "Rs 79", font = "Arial 10 bold").place(x=250, y=350)

#making quantities variable
quantity_idlisambar_variable = IntVar()
quantity_masaladosa_variable = IntVar()
quantity_cholebhature_variable = IntVar()
quantity_rajkachori_variable = IntVar()
quantity_dahisamosa_variable = IntVar()
quantity_panipuri_variable = IntVar()
quantity_bhelpuri_variable = IntVar()

#item quantities
quantity_idlisambar = Entry(root, textvariable = quantity_idlisambar_variable, font = "Arial 10 bold", width = 10).place(x=325, y=170)
quantity_masaladosa = Entry(root, textvariable = quantity_masaladosa_variable, font = "Arial 10 bold", width = 10).place(x=325, y=200)
quantity_cholebhature = Entry(root, textvariable = quantity_cholebhature_variable, font = "Arial 10 bold", width = 10).place(x=325, y=230)
quantity_rajkachori = Entry(root, textvariable = quantity_rajkachori_variable, font = "Arial 10 bold", width = 10).place(x=325, y=260)
quantity_dahisamosa = Entry(root, textvariable = quantity_dahisamosa_variable, font = "Arial 10 bold", width = 10).place(x=325, y=290)
quantity_panipuri = Entry(root, textvariable = quantity_panipuri_variable, font = "Arial 10 bold", width = 10).place(x=325, y=320)
quantity_bhelpuri = Entry(root, textvariable = quantity_bhelpuri_variable, font = "Arial 10 bold", width = 10).place(x=325, y=350)

#item amounts
amount_idlisambar_variable = IntVar()
amount_masaladosa_variable = IntVar()
amount_cholebhature_variable = IntVar()
amount_rajkachori_variable = IntVar()
amount_dahisamosa_variable = IntVar()
amount_panipuri_variable = IntVar()
amount_bhelpuri_variable = IntVar()

#final amount variable
final_amount_variable = IntVar()

#reset
def Reset():
    chkbtn_idlisambar_variable.set(0)
    chkbtn_masaladosa_variable.set(0)
    chkbtn_cholebhature_variable.set(0)
    chkbtn_rajkachori_variable.set(0)
    chkbtn_dahisamosa_variable.set(0)
    chkbtn_panipuri_variable.set(0)
    chkbtn_bhelpuri_variable.set(0)

    quantity_idlisambar_variable.set(0)
    quantity_masaladosa_variable.set(0)
    quantity_cholebhature_variable.set(0)
    quantity_rajkachori_variable.set(0)
    quantity_dahisamosa_variable.set(0)
    quantity_panipuri_variable.set(0)
    quantity_bhelpuri_variable.set(0)

    amount_idlisambar_variable.set(0)
    amount_masaladosa_variable.set(0)
    amount_cholebhature_variable.set(0)
    amount_rajkachori_variable.set(0)
    amount_dahisamosa_variable.set(0)
    amount_panipuri_variable.set(0)
    amount_bhelpuri_variable.set(0)


#calculating amount of each items
def Calculate():
    if (chkbtn_idlisambar_variable.get() == 1):
        amount_idlisambar_variable.set(quantity_idlisambar_variable.get()*50)
    if (chkbtn_masaladosa_variable.get() == 1):
        amount_masaladosa_variable.set(quantity_masaladosa_variable.get()*80)
    if (chkbtn_cholebhature_variable.get() == 1):
        amount_cholebhature_variable.set(quantity_cholebhature_variable.get()*142)
    if (chkbtn_rajkachori_variable.get() == 1):
        amount_rajkachori_variable.set(quantity_rajkachori_variable.get()*95)
    if (chkbtn_dahisamosa_variable.get() == 1):
        amount_dahisamosa_variable.set(quantity_dahisamosa_variable.get()*76)
    if (chkbtn_panipuri_variable.get() == 1):
        amount_panipuri_variable.set(quantity_panipuri_variable.get()*70)
    if (chkbtn_bhelpuri_variable.get() == 1):
        amount_bhelpuri_variable.set(quantity_bhelpuri_variable.get()*79)

    final_amount_variable.set(amount_idlisambar_variable.get() + amount_bhelpuri_variable.get() + amount_dahisamosa_variable.get() + amount_cholebhature_variable.get() + amount_rajkachori_variable.get() + amount_masaladosa_variable.get() + amount_panipuri_variable.get())




#item amount
amount_idlisambar = Entry(root, textvariable = amount_idlisambar_variable, font = "Arial 10 bold", width = 10, state = "disabled").place(x=450, y=170)
amount_masaladosa = Entry(root, textvariable = amount_masaladosa_variable, font = "Arial 10 bold", width = 10, state = "disabled").place(x=450, y=200)
amount_cholebhature = Entry(root, textvariable = amount_cholebhature_variable, font = "Arial 10 bold", width = 10, state = "disabled").place(x=450, y=230)
amount_rajkachori = Entry(root, textvariable = amount_rajkachori_variable, font = "Arial 10 bold", width = 10, state = "disabled").place(x=450, y=260)
amount_dahisamosa = Entry(root, textvariable = amount_dahisamosa_variable, font = "Arial 10 bold", width = 10, state = "disabled").place(x=450, y=290)
amount_panipuri = Entry(root, textvariable = amount_panipuri_variable, font = "Arial 10 bold", width = 10, state = "disabled").place(x=450, y=320)
amount_bhelpuri = Entry(root, textvariable = amount_bhelpuri_variable, font = "Arial 10 bold", width = 10, state = "disabled").place(x=450, y=350)

#final amount
Final_Amount_Label = Label(root, text = "FINAL AMOUNT = ", font = "Arial 16 bold").place(x=10, y=420)
Final_Amount_Entry = Entry(root, textvariable = final_amount_variable, width = 10, state = "disabled", font = "Arial 16 bold").place(x=200, y=420)

#buttons
Calculate_Amount_Button = Button(root, text = "Calculate Bill Amount", font = "Arial 10 bold", command = Calculate).place(x=400, y=400)
Reset_Button = Button(root, text = "RESET", font = "Arial 10 bold", command = Reset).place(x=440, y=440)

root.mainloop()