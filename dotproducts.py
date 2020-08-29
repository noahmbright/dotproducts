from tkinter import *
from flask import Flask



def hermcon(psi):
    psibar = []
    for i in range(len(psi)):
        psibar.append(complex(psi[i].real,-psi[i].imag))
    return psibar

def innerprod(a,b):
    sum = 0
    c = hermcon(a)
    for i in range(0, len(a)):
        prod = c[i]*b[i]
        sum += prod
    return sum

def squaremod(z):
    return((z.real)**2 + (z.imag)**2)


root = Tk()

v1input = Text(root, height = 1, borderwidth = 5, spacing1 = 1)
v2input = Text(root, height = 2, bd = 5, spacing1 = 1)
v1input.pack()
v2input.pack()

def takeprod():
    a = v1input.get(0.0,END).split(',')
    b = v2input.get(0.0,END).split(',')
    stringa = ""
    stringb = ""
    for i in range(len(a)):
        if i<(len(a)-1):
            stringa += str(a[i]) + "|" + str(i+1) + "> + "
            stringb += str(b[i]) + "|" + str(i + 1) + "> + "
        if i ==len(a)-1:
            stringa += str(a[i]) + "|" + str(i+1) + ">"
            stringb += str(b[i]) + "|" + str(i + 1) + ">"


        a[i] = complex(a[i])
        b[i] = complex(b[i])
    prod = innerprod(a,b)
    stringc = stringa.replace('\n', "")
    stringd = stringb.replace('\n', "")

    output1 = Label(root, text = "V1 =" + stringc)
    output2 = Label(root, text = "V2 = " + stringd)
    output3 = Label(root, text = "|<V1|V2>|^2 = " + str(squaremod(prod)))
    output1.pack()
    output2.pack()
    output3.pack()

    print("\n" in stringc)

b = Button(root, text = "Find inner product", command = takeprod)
b.pack()
quitbutton = Button(root, text= "Done", command = root.quit)
quitbutton.pack()


root.mainloop()

