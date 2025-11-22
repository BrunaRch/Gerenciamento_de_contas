
from tkinter import *

# Cria root-janela
root=Tk()
root.geometry("1100x500")
root.title("Gerenciamento")
root.resizable(False,False)

# Função pra limpar campos de entrada
def Limpar():
    entry_Panquecas.delete(0,END)
    entry_Misto.delete(0,END)
    entry_Cookies.delete(0,END)
    entry_Cafe.delete(0,END)
    entry_Cha.delete(0,END)

# Função para calcular total da conta
def Total():
    try:a1=int(Panquecas.get())
    except:a1=0

    try:a2=int(Misto.get())
    except:a2=0

    try:a3=int(Cookies.get())
    except:a3=0

    try:a4=int(Cafe.get())
    except:a4=0

    try:a5=int(Cha.get())
    except:a5=0

    # Definir custos entradas x preços
    C1=25*a1
    C2=15*a2
    C3=9*a3
    C4=5*a4
    C5=4*a5

    lbl_total=Label(f2,font=('arial',20,'bold'),text="Total",width=16,fg="black",bg="lightgray")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=('arial',20,'bold'),bd=6,width=14,bg="lightgray")
    entry_total.place(x=0,y=90)
    total_conta=str(C1+C2+C3+C4+C5)
    entry_total.insert(0,total_conta)


Label(text="Gerenciamento de contas", bg="rosybrown", fg="black", font=("Georgia",33),width="300",height="2").pack()

# Coluna dos preços-edição do frame de menu
f=Frame(root,bg="rosybrown",highlightbackground="LIGHTGRAY",highlightthickness=1,width=350,height=350)
f.place(x=10,y=118)

Label(f,text="Menu",bg="rosybrown",fg="black",font=("Georgia",31,"bold")).place(x=105,y=0)

Label(f,font=("Georgia",15,'bold'),text="Panquecas..........R$ 25/prato",fg="black",bg="rosybrown").place(x=10,y=80)
Label(f,font=("Georgia",15,'bold'),text="Misto.................R$ 15/uni",fg="black",bg="rosybrown").place(x=10,y=110)
Label(f,font=("Georgia",15,'bold'),text="Cookies..............R$ 9/unid",fg="black",bg="rosybrown").place(x=10,y=140)
Label(f,font=("Georgia",15,'bold'),text="Café...................R$ 5/350ml",fg="black",bg="rosybrown").place(x=10,y=170)
Label(f,font=("Georgia",15,'bold'),text="Chá....................R$ 4/200ml",fg="black",bg="rosybrown").place(x=10,y=200)



# f1 = Frame de entradas do usuário
f1=Frame(root,bd=5,height=350,width=300,bg="seashell", relief=GROOVE)
f1.place(x=360, y=118)



Panquecas=StringVar()
Misto=StringVar()
Cookies=StringVar()
Cafe=StringVar()
Cha=StringVar()
Total_da_conta=StringVar()

# f2 = Frame para conta
f2=Frame(root,bd=5,bg="lightyellow",height=350,width=300,relief=GROOVE)
f2.place(x=710,y=118)

conta=Label(f2,text="Custos",font=("Georgia",23,'bold'),bg="lightyellow",fg="black").place(x=90,y=0)

# Label quantidades
Label(f1,text="Quantidades",fg="black",bg="seashell",font=("georgia",23,'bold')).grid(row=0, column=0)

lbl_Panquecas=Label(f1,font=("Arial",13,'bold'),text="Panquecas",width=9,fg="black", bg="seashell")
lbl_Misto=Label(f1,font=("Arial",13,'bold'),text="Misto",width=9,fg="black", bg="seashell")
lbl_Cookies=Label(f1,font=("Arial",13,'bold'),text="Cookies",width=9,fg="black", bg="seashell")
lbl_Cafe=Label(f1,font=("Arial",13,'bold'),text="Cafe",width=9,fg="black", bg="seashell")
lbl_Cha=Label(f1,font=("Arial",13,'bold'),text="Cha",width=9,fg="black", bg="seashell")
lbl_Panquecas.grid(row=1,column=0)
lbl_Misto.grid(row=2, column=0)
lbl_Cookies.grid(row=3, column=0)
lbl_Cafe.grid(row=4, column=0)
lbl_Cha.grid(row=5, column=0)

# Entrada do usuário
entry_Panquecas = Entry(f1,font=("Arial",13,'bold'),textvariable=Panquecas,bd=6,width=8,bg="lightgray")
entry_Misto = Entry(f1,font=("Arial",13,'bold'),textvariable=Misto,bd=6,width=8,bg="lightgray")
entry_Cookies = Entry(f1,font=("Arial",13,'bold'),textvariable=Cookies,bd=6,width=8,bg="lightgray")
entry_Cafe = Entry(f1,font=("Arial",13,'bold'),textvariable=Cafe,bd=6,width=8,bg="lightgray")
entry_Cha = Entry(f1,font=("Arial",13,'bold'),textvariable=Cha,bd=6,width=8,bg="lightgray")

entry_Panquecas.grid(row=1,column=1)
entry_Misto.grid(row=2,column=1)
entry_Cookies.grid(row=3,column=1)
entry_Cafe.grid(row=4,column=1)
entry_Cha.grid(row=5,column=1)

#limpar campos de quantidades inseridas
btn_limpar=Button(f1,bd=5,fg="black",bg="rosybrown",font=("Georgia",10,'bold'),width=10,text="Limpar",command=Limpar)
btn_limpar.grid(row=7,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="rosybrown",font=("Georgia",10,'bold'),width=10,text="Pagar conta", command=Total)
btn_total.grid(row=7,column=1)


root.mainloop()