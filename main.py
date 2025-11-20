
from tkinter import *

# Cria root-janela
root=Tk()
root.geometry("1000x500")
root.title("Gerenciamento")
root.resizable(False,False)

Label(text="Gerenciamento de contas", bg="lightsalmon", fg="chocolate", font=("calibri",33),width="300",height="2").pack()

# Cartão de menu
# Coluna dos preços-edição do frame de menu
f=Frame(root,bg="lightsalmon",highlightbackground="goldenrod",highlightthickness=1,width=300,height=350)
f.place(x=10,y=118)

Label(f,text="Menu",bg="lightsalmon",fg="chocolate",font=("MonoLisa",32,"bold")).place(x=80,y=0)

Label(f,font=("Impact",13,'bold'),text="Panquecas..........R$.60/prato",fg="black",bg="lightsalmon").place(x=10,y=80)
Label(f,font=("Impact",13,'bold'),text="Misto..........R$.60/prato",fg="black",bg="lightsalmon").place(x=10,y=110)
Label(f,font=("Impact",13,'bold'),text="Cookies..........R$.60/prato",fg="black",bg="lightsalmon").place(x=10,y=140)
Label(f,font=("Impact",13,'bold'),text="Café..........R$.60/prato",fg="black",bg="lightsalmon").place(x=10,y=170)
Label(f,font=("Impact",13,'bold'),text="Chá..........R$.60/prato",fg="black",bg="lightsalmon").place(x=10,y=200)

# Cria conteiner de entradas do usuário
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Panquecas=StringVar()
Misto=StringVar()
Cookies=StringVar()
Cafe=StringVar()
Cha=StringVar()
Total_da_conta=StringVar()

# Label 
lbl_Panquecas=Label(f1,font=("Arial",15,'bold'),text="Panquecas",width=9,fg="blue")
lbl_Misto=Label(f1,font=("Arial",15,'bold'),text="Misto",width=9,fg="blue")
lbl_Cookies=Label(f1,font=("Arial",15,'bold'),text="Cookies",width=9,fg="blue")
lbl_Cafe=Label(f1,font=("Arial",15,'bold'),text="Cafe",width=9,fg="blue")
lbl_Cha=Label(f1,font=("Arial",15,'bold'),text="Cha",width=9,fg="blue")
lbl_Panquecas.grid(row=1,column=0)
lbl_Misto.grid(row=2, column=0)
lbl_Cookies.grid(row=3, column=0)
lbl_Cafe.grid(row=4, column=0)
lbl_Cha.grid(row=5, column=0)

# Entrada do usuário
entry_Panquecas = Entry(f1,font=("Arial",15,'bold'),textvariable=Panquecas,bd=6,width=8,bg="lightpink")
entry_Panquecas.grid(row=1,column=1)


root.mainloop()