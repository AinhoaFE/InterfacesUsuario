from tkinter import *
from tkinter import messagebox
import cv2
raiz=Tk()
raiz.title("APP Instagram")
raiz.geometry("400x690+400+0")
raiz.grid()

#canvas_width=400
#canvas_height=650

miFrame=Frame()
miFrame.pack(side="top", anchor="n")
miFrame.pack(fill="both", expand="true")
miFrame.config( bg="white",width="400", height="100")
#miFrame.place(x=650, y=0)

historias=Frame()
historias.pack(side="top", anchor="n")
historias.pack(fill="both", expand="true")
historias.config( bg="#F0F4F4",width="400", height="100")

historias.config(bg="white")
#historias.place(x=0,y=550 )

resto=Frame()
resto.pack(side="top", anchor="n")
resto.pack(fill="both", expand="true")
resto.config( bg="white",width="400", height="150")
#resto.place(x=650,y=0)

#canvas=Canvas(resto)
#canvas.grid(row=0, column=0, sticky="ns")
#scrollBar=Scrollbar(resto)
#scrollBar.pack(side = RIGHT, fill = Y)
#scrollBar.grid(row=3, column=3,sticky='ns')
#canvas.configure(yscrollcommand = scrollBar.set)
#canvas.pack(side=LEFT,expand=True,fill=BOTH)


#canvas=Canvas(resto, yscrollincrement = 10, bg='#FFFFFF',width=300,height=650,scrollregion=(0,0,500,1000))
#vbar=Scrollbar(resto,orient=VERTICAL)
#vbar.pack(side=RIGHT,fill=Y)
#vbar.config(command=canvas.yview)
#canvas.config(width=400,height=250)
#canvas.config( yscrollcommand=vbar.set)
#canvas.pack(side=LEFT,expand=True,fill=BOTH)

pie=Frame()
pie.pack(side="top", anchor="n")
pie.pack(fill="both", expand="true")
pie.config( bg="white",width="400", height="100")

Foto=PhotoImage(file="img/Foto.PNG")
foto=Label(miFrame, image=Foto, bd=0)
foto.grid(row=0, column=0, sticky="n", padx=20)

Instagram=PhotoImage(file="img/Logoinsta.PNG")
insta=Label(miFrame, image=Instagram, bd=0)
insta.grid(row=0, column=1, sticky="n", padx=20, columnspan=3)

Mensajes=PhotoImage(file="img/Mensajes.PNG")
mens=Label(miFrame, image=Mensajes , bd=0)
mens.grid(row=0, column=4, sticky="n", padx=20)

Imagen=PhotoImage(file="img/homero.png")
Imag=Label(historias, image=Imagen, bd=7)
Imag.grid(row=1, column=0, sticky="n", padx=0)

Hist=Label(historias, text=" Tu historia   ",bd=7 ,anchor="center")
Hist.grid(row=2, column=0, sticky="n")

Perfil1=PhotoImage(file="img/mono_logo_a_copia.png")
Perf1=Label(historias, image=Perfil1 ,bd=7)
Perf1.grid(row=1, column=1, sticky="n", ipadx=0)

NPerfil=Label(historias, text=" Perfil Mono ",anchor="center",bd=7)
NPerfil.grid(row=2, column=1, sticky="n")

Perfil2=PhotoImage(file="img/mono1_logo_a_copia.png")
Perf2=Label(historias, image=Perfil2 ,bd=7)
Perf2.grid(row=1, column=2, sticky="n", ipadx=0)

NPerfil2=Label(historias, text="Perfil Mono1", anchor="center", bd=7)
NPerfil2.grid(row=2, column=2, sticky="n")

Perfil3=PhotoImage(file="img/mono2_logo_a_copia.png")
Perf3=Label(historias, image=Perfil3 ,bd=7)
Perf3.grid(row=1, column=3, sticky="n", ipadx=0)

NPerfi3=Label(historias, text="Perfil Mono2", anchor="center", bd=7)
NPerfi3.grid(row=2, column=3, sticky="n")


Perfil4=PhotoImage(file="img/mono3_logo_a_copia.png")
Perf4=Label(historias, image=Perfil4 ,bd=7)
Perf4.grid(row=1, column=4, sticky="n" , ipadx=0)

NPerfil4=Label(historias, text="Perfil Mono3", anchor="center", bd=7)
NPerfil4.grid(row=2, column=4, sticky="n")

#Parte del body
Perfil=PhotoImage(file="img/mono_logo_a_copia.png")
Perfil=Perfil.subsample(2,2)
perf=Label(resto, image=Perfil,  bg="white")
perf.grid(row=0, column=0, sticky="w", padx=0)

Hist=Label(resto, text="Perfil Mono1",anchor="center",  bg="white")
Hist.grid(row=0, column=0 , padx=0)

Puntos=Label(resto, text="...",anchor="center", bg="white")
Puntos.grid(row=0, column=2, sticky="e", padx=10,)

Desc=Label(resto, text="Descripción",anchor="center", bg="white")
Desc.grid(row=1, column=0, sticky="w", padx=10,)

NY=PhotoImage(file="img/ny.png",width=1200, height=450)
NY=NY.subsample(3,3)
ny=Label(resto, image=NY)
ny.grid(row=2, column=0, sticky="n", columnspan=3)


Mono1=PhotoImage(file="img/mono1_logo_a_copia.png")
Mono1=Mono1.subsample(2,2)
mono1=Label(resto, image=Mono1,  bg="white")
mono1.grid(row=3, column=0, sticky="w", padx=0)

Hist=Label(resto, text="Perfil Mono2",anchor="center",  bg="white")
Hist.grid(row=3, column=0 , padx=0)

Puntos=Label(resto, text="...",anchor="center", bg="white")
Puntos.grid(row=3, column=2, sticky="e", padx=10,)


Desc=Label(resto, text="Descripción",anchor="center", bg="white")
Desc.grid(row=4, column=0, sticky="w", padx=10,)


PuntaCana=PhotoImage(file="img/pc.png", width=400, height=180)
pc=Label(resto, image=PuntaCana)
pc.grid(row=8, column=0, sticky="w", columnspan=3)
'''
Mono2=PhotoImage(file="img/mono2_logo_a_copia.png")
Mono2=Mono1.subsample(2,2)
mono2=Label(resto, image=Mono1,  bg="white")
mono2.grid(row=6, column=0, sticky="w", padx=0)

Hist=Label(resto, text="Perfil Mono3",anchor="center",  bg="white")
Hist.grid(row=6, column=0 , padx=0)

Puntos=Label(resto, text="...",anchor="center", bg="white")
Puntos.grid(row=6, column=2, sticky="e", padx=10)


Desc=Label(resto, text="Descripción",anchor="center", bg="white")
Desc.grid(row=7, column=0, sticky="w", padx=10,)

PuntaCana=PhotoImage(file="img/pc.png", width=400, height=200)
pc=Label(resto, image=PuntaCana)
pc.grid(row=8, column=0, sticky="w", columnspan=3)
Retiro=PhotoImage(file="img/retiro1.png", width=400, height=150)
#Retiro=Retiro.subsample(2,2)
#Retiro = Retiro.resize((400,100))
retiro=Label(resto, image=Retiro)
retiro.grid(row=5, column=0, sticky="w", columnspan=3)
'''

Casa=PhotoImage(file="img/Inicio.PNG")
casa=Label(pie, image=Casa,  bg="white")
casa.grid(row=0, column=0, sticky="w", padx=15)

Lupa=PhotoImage(file="img/Buscar.PNG")
lupa=Label(pie, image=Lupa,  bg="white")
lupa.grid(row=0, column=1, sticky="w", padx=15)

Anadir=PhotoImage(file="img/Anadir.PNG")
anadir=Label(pie, image=Anadir,  bg="white")
anadir.grid(row=0, column=2, sticky="w", padx=15)

Like=PhotoImage(file="img/Corazon.PNG")
like=Label(pie, image=Like,  bg="white")
like.grid(row=0, column=3, sticky="w", padx=15)

Perfilpie=PhotoImage(file="img/perfil.gif")
Perfilpie=Perfilpie.subsample(2,2)
perfpie=Label(pie, image=Perfilpie,  bg="white")
perfpie.grid(row=0, column=4, sticky="w", padx=15)


def ask_quit():
    if messagebox.askokcancel(title="Cerrar la aplicación",message="¿Seguro que quieres cerrar la aplicación?\n\n"):
        raiz.destroy()


raiz.protocol("WM_DELETE_WINDOW", ask_quit)
raiz.mainloop()
