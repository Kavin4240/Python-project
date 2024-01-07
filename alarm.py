from tkinter import *
from tkinter import messagebox
import time
import threading
from pygame import mixer

root= Tk()
root.title("Alarm")
root.geometry("550x350")
root.configure(background="#87CEEB")
mixer.init()

def th():
	t1 = threading.Thread(target=a, args=())
	t1.start()
def a():
	a = hr.get()
	if a == "":
		msg = messagebox.showerror('Invalid data','Please enter valid time')
	else:
		Alarmtime= a
		CurrentTime = time.strftime("%H:%M")
		while Alarmtime != CurrentTime:
			CurrentTime = time.strftime("%H:%M")
   
		if Alarmtime == CurrentTime: 
			mixer.music.load('tone.mp3')
			mixer.music.play()
			msg = messagebox.showinfo('It is time',f'{amsg.get()}')
			if msg == 'ok':
				mixer.music.stop()
                
       
header =Frame(root)
header.place(x=5,y=5)
head =Label(root,text="ALARM CLOCK",font=('comic sans',20),foreground='blue',bg='pink')
head.pack(fill=X)
panel = Frame(root)
panel.place(x=400,y=200)
alpp = PhotoImage(file='al.png')
alp = Label(panel,image=alpp)
alp.grid(rowspan=4,column=0)


atime = Label(panel,text="Alarm Time \n(Hr:Min)",font=('comic sans',18),activeforeground='green')
atime.grid(row=0,column=1,padx=10,pady=5)
hr = Entry(panel,font=('comic sans',20),width=5,fg='black')
hr.grid(row=0,column=2,padx=10,pady=5)
amessage = Label(panel,text="Message",font=('comic sans',20),foreground="red")
amessage.grid(row=1,column=1,columnspan=2,padx=10,pady=5)
amsg = Entry(panel,font=('comic sans',15),width=25)
amsg.grid(row=2,column=1,columnspan=2,padx=10,pady=5)
start = Button(panel,text="Start alarm",font=('Times New Roman',20),foreground='green',command=th,bg="#33FFE0")
start.grid(row=3,column=1,columnspan=2,padx=10,pady=5)
root.mainloop()