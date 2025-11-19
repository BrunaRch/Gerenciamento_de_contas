from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("Gerenciamento")
root.resizable(False,False)

Label(text="Gerenciamento de contas", bg="lightsalmon", fg="chocolate", font=("calibri",33),width="300",height="2").pack()

# Cartão de menu
# Coluna dos preços-edição-tamanho
f=Frame(root,bg="lightsalmon",highlightbackground="grey",highlightthickness=1,width=300,height=350)
f.place(x=10,y=118)

Label(f,text="Menu",bg="lightsalmon",fg="chocolate",font=("MonoLisa",32,"bold")).place(x=80,y=0)
root.mainloop()