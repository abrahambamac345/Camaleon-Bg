#Uso de la libreria Tkinter 
import tkinter
#Uso de la libreria Random
import random
#ventana
ventanatk = tkinter.Tk()#abrimos nuestra ventana
ventanatk.title("Background Camaleón")
ventanatk.resizable(False,False)
ventanatk.geometry("800x500")#definimos el tamaño de la ventana
#monitor
BGCOLOR = tkinter.Label(ventanatk, text = "Background Color:", font='Courier 30',foreground="white",background="grey")
BGCOLOR.place(x=105,y=170) 
#Fondo random
def Camaleón():
    colores=["#E69218","#E6B418","#82E618","#18E6A4","#C0E618","#ED3F19","#137896","#1F1396","#371396","#721396","#961378","#5A78B2","#18E6E0"]
    randcolores=random.choice(colores)
    ventanatk.config(background=randcolores)
    BGCOLO = tkinter.Label(ventanatk, text = randcolores, font='Courier 30',foreground="white",background="grey")
    BGCOLO.place(x=512,y=170)
#boton para cambiar el color
SUMA=tkinter.Button(ventanatk, text = "CLIK ME", font= "Arial_Black 20", width=12, height=1, command=Camaleón,foreground="black")
SUMA.place(x=300, y=250)
ventanatk.mainloop()#cerramos