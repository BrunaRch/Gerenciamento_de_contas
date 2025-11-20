
from tkinter import *

# Cria root-janela
root=Tk()
root.geometry("1000x500")
root.title("Gerenciamento")
root.resizable(False,False)

Label(text="Gerenciamento de contas", bg="rosybrown", fg="black", font=("Georgia",33),width="300",height="2").pack()

# Cartão de menu
# Coluna dos preços-edição do frame de menu
f=Frame(root,bg="rosybrown",highlightbackground="LIGHTGRAY",highlightthickness=1,width=350,height=350)
f.place(x=10,y=118)

Label(f,text="Menu",bg="rosybrown",fg="black",font=("Georgia",31,"bold")).place(x=105,y=0)

Label(f,font=("Georgia",15,'bold'),text="Panquecas..........R$ 25/prato",fg="black",bg="rosybrown").place(x=10,y=80)
Label(f,font=("Georgia",15,'bold'),text="Misto.................R$ 15/uni",fg="black",bg="rosybrown").place(x=10,y=110)
Label(f,font=("Georgia",15,'bold'),text="Cookies..............R$ 9/unid",fg="black",bg="rosybrown").place(x=10,y=140)
Label(f,font=("Georgia",15,'bold'),text="Café...................R$ 5/350ml",fg="black",bg="rosybrown").place(x=10,y=170)
Label(f,font=("Georgia",15,'bold'),text="Chá....................R$ 4/200ml",fg="black",bg="rosybrown").place(x=10,y=200)

# Cria conteiner de entradas do usuário
f1=Frame(root,bd=5,height=370,width=300,bg="seashell", relief=GROOVE)
f1.place(x=360, y=118)

Panquecas=StringVar()
Misto=StringVar()
Cookies=StringVar()
Cafe=StringVar()
Cha=StringVar()
Total_da_conta=StringVar()

# Label 

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


root.mainloop()