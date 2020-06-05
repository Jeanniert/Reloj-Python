from  tkinter import *
import time

#FUNCION DE LA ACTUALIZAR DE LA HORA
def times():
	current_time=time.strftime("%H:%M:%S") 
	clock.config(text=current_time,bg="teal",fg="black",font="Arial 50 bold")
	clock.after(200,times)
	
#VENTANA
root=Tk()
root.title("Reloj digital con Python")
clock=Label(root,font=("calibri",50,"bold"))

clock.grid(row=2,column=1,pady=25,padx=100)

times()
root.mainloop()

#
#
#
#
#
#
#
#
#
#