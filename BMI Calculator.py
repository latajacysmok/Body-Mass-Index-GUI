from tkinter import *

def BMI_cal():
    BWeight = float(var1.get())
    BHeight = float(var2.get())
    BMI = str("%.2f" %(BWeight / (BHeight*BHeight)))
    lblBMIResult.config(text=BMI)

bmi = Tk()
bmi.title(" Body Mass Index ")
bmi.resizable(0, 0)
bmi ['bg'] = 'powder blue'
bmi.geometry('1350x650')

var1 = DoubleVar()
var2 = DoubleVar()

Tops = Frame(bmi, width=1350, height=50, bd=8, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(bmi, width=600, height=600, bd=8, relief="raise")
f1.pack(side=LEFT)

f1a = Frame(f1, width=600, height=200, bd=20, relief="raise")
f1a.pack(side=TOP)
f1b = Frame(f1, width=600, height=600, bd=20, relief="raise")
f1b.pack(side=TOP)

f2 = Frame(bmi, width=300, height=700, bd=8, relief="raise")
f2.pack(side=RIGHT)

lblTitle = Label(Tops, text="   Body Mass Index   ", padx=16, pady=16, bd=16,
                 fg='#000000', font=('arial', 54, 'bold'), bg='sky blue',
                 relief= 'raise', width=32, height=1)
lblTitle.pack()

lblHeight = Label(f1a, text="Select Weight in Kilograms", font=('arial', 20, 'bold'), bd=20).grid(row=0, column=0)

BodyWeight = Scale(f1a, variable = var1, from_=0, to=200, length=880, tickinterval=10, orient=HORIZONTAL)
BodyWeight.grid(row=1, column=0)

lblHeight = Label(f1b, text="Enter Height in Meters Square", font=('arial', 20, 'bold'), bd=20).grid(row=0, column=0)
txtheight = Entry(f1b, textvariable=var2, font=('arial', 16, 'bold'), bd=16, width=22, justify='center')
txtheight.grid(row=1, column=0)

lblBMIResult = Label(f1b, padx=16, pady=16, bd=16,
                 fg='#000000', font=('arial', 30, 'bold'), bg='sky blue',
                 relief= 'sunk', width=34, height=1)
lblBMIResult.grid(row=2, column=0)

lblBMITable = Label(f2, text="BMI Table", font=('arial', 20, 'bold')).grid(row=0, column=0)
txtlblBMITable = Text(f2, font=('arial', 12, 'bold'), bd=16, width=38, height=12)
txtlblBMITable.grid(row=1, column=0)

txtlblBMITable.insert(END, 'Meaning \t\t'+'BMI \n\n')
txtlblBMITable.insert(END, 'Normal weight \t\t'+'19-24,9 \n\n')
txtlblBMITable.insert(END, 'Overweight \t\t'+'25-29,9 \n\n')
txtlblBMITable.insert(END, 'Obesity level I   \t\t'+'30-34,9 \n\n')
txtlblBMITable.insert(END, 'Obesity level II  \t\t'+'35-39,9 \n\n')
txtlblBMITable.insert(END, 'Obesity level III \t\t'+'>40 \n\n')

btnBMI = Button(f2, text="Click to \nCheck Your \nBMI", padx=8, pady=8, bd=12,
                width=21, height=3, font=('arial', 20, 'bold'), command=BMI_cal)
btnBMI.grid(row=2, column=0)


bmi.mainloop()