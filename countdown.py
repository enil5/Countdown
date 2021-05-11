import datetime
import time
import tkinter as tk
from tkinter import ttk
from tkinter import *

class countdown:

    def __init__(self):
        self.index=0
        self.checktop=1
        self.check=0
        self.counter=0
        self.labels=[]
        self.labels2=[]
        self.checkboxes=[]
        self.combox=[]
        self.frames=[]
        self.wtime=0
        self.time="0:00:00"
        self.timel=self.time.split(":")
        print(self.timel)
        self.steps=["Suit UP","Crew walk out","Transport to Pad","Ingress","Hatch Close","Access Arm Retracts","Fuel Loading","Terminal Count","Launch"]
        self.timerel=[8]


    def startcount(self):
    
        zaehler=0
        countl=["0:00:00","def"]
        
        #print(self.monat.current())
        zeit=datetime.datetime.now()
        zeit=zeit.replace(microsecond=0)
        #zeitab=datetime.datetime(int(self.jahr.get()),self.monat.current()+1,int(self.tag.get()),int(self.timel[0]),int((self.timel[1])),int(self.timel[2]))-zeit
        #zeitab=zeitab.replace(microsecond=0)
        #print(self.index)

        if self.wtime==0:
            zeitab=datetime.datetime(int(self.jahr.get()),self.monat.current()+1,int(self.tag.get()),int(self.timel[0]),int((self.timel[1])),int(self.timel[2]))-zeit
        elif self.wtime==1:
            #print("wtime=1")
            zeitab=zeit-datetime.datetime(int(self.jahr.get()),self.monat.current()+1,int(self.tag.get()),int(self.timel[0]),int((self.timel[1])),int(self.timel[2]))

            
        print(zeitab)

        

        
        if(str(zeitab)==countl[self.index]):
            print("Count ab")
            print(self.labels[8])
        
            self.combox[8].current(2)
            #farbe="green"
            #self.combox
            #self.top.update_idletasks()
            self.index+=1

        if str(zeitab)=="0:00:00":
            self.wtime=1

        #print(len(self.combox))
        try:
            for i in range (0,len(self.combox),1):
                #print(self.combox[i])

                if self.combox[i].get() == "Noch nicht":
                    self.labels2[zaehler].config(bg="red")
                    self.labels[zaehler].config(bg="red")
                
                elif self.combox[i].get() == "In Arbeit":
                    self.labels2[zaehler].config(bg="yellow")
                    self.labels[zaehler].config(bg="yellow")

                elif self.combox[i].get() == "Fertig":
                    self.labels2[zaehler].config(bg="green")
                    self.labels[zaehler].config(bg="green")
                zaehler+=1
                #print(zaehler)
        except:
            pass




        self.anzeige.config(text=zeitab)
        try:
            self.anzeige2.config(text=zeitab)
        except:
            pass
        
        self.after_id=self.root.after(500, self.startcount)

    def setup(self):

        #print(check)
        if self.check==0:
            self.check=1
            self.start.config(text="Stop",fg="red")
            self.startcount()

        elif self.check==1:
            self.check=0
            self.start.config(text="Start",fg="green")
            #self.after_id
            if self.after_id:
                self.root.after_cancel(self.after_id) 
                self.after_id = None

    def create_workstation(self):
        station=Toplevel()
        station.title("Add Name")
        self.e1=tk.Entry(station)
        btn=tk.Button(station,text="Save",command=self.verarbeiten)
        self.e1.pack()
        btn.pack()

    def verarbeiten(self):
        self.labels=[]
        self.labels2=[]
        self.checkboxes=[]
        self.combox=[]
        self.frames=[]

        try:
            self.f4.destroy()
            self.f7.destroy()
        except:
            pass

        self.f4=tk.Frame(self.top)
        self.f4.pack(fill=X)


        self.f7=tk.Frame(self.root)
        self.f7.pack(fill=X)
        self.f7.config(bg="#1D2021")
        
        for i in self.steps:

            try:
                self.zustand=["Noch nicht","In Arbeit","Fertig"]
                self.cobox="Box"+str(self.counter)
                self.mark="lab"+str(self.counter)
                self.mark2="lab2"+str(self.counter)
                self.cebox="check"+str(self.counter)
                self.bild="frame"+str(self.counter)
                self.bild2="frame2"+str(self.counter)

                self.bild=tk.Frame(self.f4)
                self.bild.config(bg="#1D2021")
                self.bild.pack(fill=X)
                self.mark=tk.Label(self.bild,text=i,bg="red")
                self.labels.append(self.mark)
                self.frames.append(self.bild)
                #self.cobox=ttk.Combobox(self.bild,values=self.zustand)
                
                #self.cobox.pack(side=tk.RIGHT,fill=X)
                self.mark.pack(fill=X,pady=5)

                self.bild2=tk.Frame(self.f7)
                self.bild2.config(bg="#1D2021")
                self.bild2.pack(fill=X,pady=5)

                self.mark2=tk.Label(self.bild2,text=i,bg="red")
                #self.cebox=tk.Checkbutton(self.bild2,bg="#1D2021")
                #self.checkboxes.append(self.checkboxes)
                
                self.cobox=ttk.Combobox(self.bild2,values=self.zustand)
                #self.cebox.pack(side=tk.RIGHT)
                self.cobox.pack(side=tk.RIGHT,fill=X)
                self.mark2.pack(fill=X)
                self.cobox.current(0)
                self.combox.append(self.cobox)
                self.labels2.append(self.mark2)
                #self.cobox.bind("<<ComboboxSelected>>", callbackFunc)
                self.counter+=1
            except:
                pass
    
    def newtime(self):
        self.timel=[]
        try:
            self.timel=self.launchtime.get().split(":")
            self.timel[0]
            self.timel[1]
            self.timel[2]
        except:
            self.timel=["0","00","00"]
        




    def mainboard(self):
        self.top=Toplevel()
        self.top.title("Zweites Fenster")
        self.top.geometry("500x430")
        self.top.config(bg="#1D2021")

        self.top.protocol("WM_DELETE_WINDOW", self.setvar)

        f1=tk.Frame(self.top)
        self.f4=tk.Frame(self.top,bg="#1D2021")

        f1.pack()
        self.f4.pack(fill=X)
        
        self.anzeige2=tk.Label(f1,text="NONE", fg="#29A3A3",bg="#1D2021",font="Helvetika 40")

        self.anzeige2.pack(fill=X)

        

        """
        self.L1=tk.Label(f4,text="Suit UP", fg="#282828",bg="#29A3A3",font="Helvetika 15")
        self.L2=tk.Label(f4,text="Crew walk out", fg="#282828",bg="#29A3A3",font="Helvetika 15")
        self.L3=tk.Label(f4,text="Transport to Pad", fg="#282828",bg="#29A3A3",font="Helvetika 15")
        self.L4=tk.Label(f4,text="Ingress", fg="#282828",bg="#29A3A3",font="Helvetika 15")
        self.L5=tk.Label(f4,text="Hatch Close", fg="#282828",bg="#29A3A3",font="Helvetika 15")
        self.L6=tk.Label(f4,text="Access Arm Retracts", fg="#282828",bg="#29A3A3",font="Helvetika 15")
        self.L7=tk.Label(f4,text="Fuel Loading", fg="#282828",bg="#29A3A3",font="Helvetika 15")
        self.L8=tk.Label(f4,text="Terminal Count", fg="#282828",bg="#29A3A3",font="Helvetika 15")
        self.L9=tk.Label(f4,text="Launch", fg="#282828",bg="#29A3A3",font="Helvetika 15")

        self.L1.pack(fill=X,pady=5)
        self.L2.pack(fill=X,pady=5)
        self.L3.pack(fill=X,pady=5)
        self.L4.pack(fill=X,pady=5)
        self.L5.pack(fill=X,pady=5)
        self.L6.pack(fill=X,pady=5)
        self.L7.pack(fill=X,pady=5)
        self.L8.pack(fill=X,pady=5)
        self.L9.pack(fill=X,pady=5)
        """

        
        #self.labels=[self.L1,self.L2,self.L3,self.L4,self.L5,self.L6,self.L7,self.L8,self.L9]

    def setvar(self):
        self.checktop=1
        #self.top.destroy()

    def newtopwin(self):
        
        if self.checktop==1:
            self.mainboard()
            self.checktop=0
        
        else:
            pass

    def main_window(self):
        
        self.root=tk.Tk()
        self.root.geometry("500x430")
        #self.mainboard()
        #f6=tk.Frame(self.root) 
        self.root.config(bg="#1D2021")     
        self.root.minsize(500,430) 
        f2=tk.Frame(self.root)
        f3=tk.Frame(self.root)
        f5=tk.Frame(self.root)
        f6=tk.Frame(self.root)
        self.f7=tk.Frame(self.root)

        f2.config(bg="#1D2021")
        f3.config(bg="#1D2021")
        f5.config(bg="#1D2021")
        f6.config(bg="#1D2021")
        self.f7.config(bg="#1D2021")
        

        self.monat=ttk.Combobox(f2,values=["Januar","Februar","Maerz","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"])
        self.jahr=ttk.Combobox(f2,values=["2020","2021","2022","2023"])
        self.tag=ttk.Combobox(f2,values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"])
        self.launchtime=tk.Entry(f2)
        self.start=tk.Button(f3,text="Start",fg="green",command=self.setup)
        self.settime=tk.Button(f3,text="Load Time",command=self.newtime)
        self.anzeige=tk.Label(f5,text="NONE", fg="#47D1D1",bg="#1D2021",font="Helvetika 25")
        self.newwin=tk.Button(f6,text="Create Level",fg="green",command=self.newtopwin)
        self.add=tk.Button(f6,text="Label add",fg="green",command=self.create_workstation)
        self.create_steps=tk.Button(f6,text="Load",command=self.verarbeiten)
        
        

        
        f2.pack()
        f3.pack()
        #f4.pack(fill=X)
        f5.pack(fill=X)
        f6.pack()
        self.f7.pack(fill=X)
    
        self.anzeige.pack(fill=X,padx=5)
        self.newwin.pack(side=tk.LEFT,padx=5)
        self.add.pack(side=tk.LEFT,padx=5)
        self.create_steps.pack(side=tk.LEFT,padx=5)
        
        self.start.pack(side=tk.LEFT,pady=5,padx=5)
        self.settime.pack(side=tk.LEFT,pady=5,padx=5)
        self.jahr.pack(padx=5, pady=20, side= tk.LEFT)
        self.jahr.current(0)
        #e1.pack()
        self.monat.pack(padx=5, pady=20, side= tk.LEFT)
        self.tag.pack(side= tk.LEFT)
        self.launchtime.pack(side=tk.LEFT, padx=5)
        self.monat.current(0)
        self.tag.current(0)

        

        




        #monat.bind("<<ComboboxSelected>>", callbackFunc)
        #ende=tk.Button(root,text="Ende",fg="red",command=stop)

        #ende.pack()
        self.root.mainloop() 

"""

def callbackFunc(event):
    print("Element")

def startcount():
    global after_id
    global index

    countl=["4:00:00","3:10:00","3:05:00","2:15:00","1:50:00","0:40:00","0:35:00","0:05:00","0:00:00","def"]
    labels=[L1,L2,L3,L4,L5,L6,L7,L8,L9]
    print(monat.current())
    zeit=datetime.datetime.now()
    zeit=zeit.replace(microsecond=0)
    zeitab=datetime.datetime(int(jahr.get()),monat.current()+1,int(tag.get()),22,31,00)-zeit
    #zeitab=zeitab.replace(microsecond=0)
    print(zeitab)
    if(str(zeitab)==countl[index]):
        print("Count ab")
       
        labels[index].config(bg="green")

        index+=1


    anzeige.config(text=zeitab)
    anzeige2.config(text=zeitab)
    after_id=root.after(500, startcount)

def show_column(name):
        #btnname.config(bg="red")
        print(name)

def setup():
    global check
    #print(check)
    if check==0:
        check=1
        start.config(text="Stop",fg="red")
        startcount()

    elif check==1:
        check=0
        start.config(text="Start",fg="green")
        global after_id
        if after_id:
            root.after_cancel(after_id) 
            after_id = None

def stop():
    global check
    check=1

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def myprint(event):
    print("test")

root=tk.Tk()
root.geometry("500x430")
top=Toplevel()
top.title("Zweites Fenster")
top.geometry("500x430")
top.config(bg="#1D2021")
f6=tk.Frame(root)



container = tk.Frame(f6)
canvas = tk.Canvas(container)
canvas.config(bg="black")

scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)
scrollable_frame.config(bg="blue")



scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)


f1=tk.Frame(top)
f2=tk.Frame(root)
f3=tk.Frame(root)
f5=tk.Frame(root)
f4=tk.Frame(top,bg="#1D2021")

monat=ttk.Combobox(f2,values=["Januar","Februar","Maerz","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"])
jahr=ttk.Combobox(f2,values=["2020","2021","2022","2023"])
tag=ttk.Combobox(f2,values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"])
start=tk.Button(f3,text="Start",fg="green",command=setup)
anzeige=tk.Label(f1,text="NONE", fg="#47D1D1",bg="#1D2021",font="Helvetika 50")
anzeige2=tk.Label(f5,text="NONE", fg="#29A3A3",bg="#1D2021",font="Helvetika 25")
L1=tk.Label(f4,text="Suit UP", fg="#282828",bg="#29A3A3",font="Helvetika 15")
L2=tk.Label(f4,text="Crew walk out", fg="#282828",bg="#29A3A3",font="Helvetika 15")
L3=tk.Label(f4,text="Transport to Pad", fg="#282828",bg="#29A3A3",font="Helvetika 15")
L4=tk.Label(f4,text="Ingress", fg="#282828",bg="#29A3A3",font="Helvetika 15")
L5=tk.Label(f4,text="Hatch Close", fg="#282828",bg="#29A3A3",font="Helvetika 15")
L6=tk.Label(f4,text="Access Arm Retracts", fg="#282828",bg="#29A3A3",font="Helvetika 15")
L7=tk.Label(f4,text="Fuel Loading", fg="#282828",bg="#29A3A3",font="Helvetika 15")
L8=tk.Label(f4,text="Terminal Count", fg="#282828",bg="#29A3A3",font="Helvetika 15")
L9=tk.Label(f4,text="Launch", fg="#282828",bg="#29A3A3",font="Helvetika 15")

f1.pack()
f2.pack()
f3.pack()
f4.pack(fill=X)
f5.pack(fill=X)
f6.pack()

anzeige.pack()
anzeige2.pack(fill=X)
start.pack(side=tk.BOTTOM,pady=5)
jahr.pack(padx=5, pady=20, side= tk.LEFT)
jahr.current(0)
#e1.pack()
monat.pack(padx=5, pady=20, side= tk.LEFT)
tag.pack(side= tk.LEFT)
monat.current(0)
tag.current(0)

L1.pack(fill=X,pady=5)
L2.pack(fill=X,pady=5)
L3.pack(fill=X,pady=5)
L4.pack(fill=X,pady=5)
L5.pack(fill=X,pady=5)
L6.pack(fill=X,pady=5)
L7.pack(fill=X,pady=5)
L8.pack(fill=X,pady=5)
L9.pack(fill=X,pady=5)


canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

for i in range(50):
    mytext=str(i)+" Textzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    name=str(i)
    
    namebtn=name+"btn"
    name=tk.Label(scrollable_frame, text=mytext)
    name.pack(side="left",fill=X)
    name.bind("<MouseWheel>", _on_mousewheel)
    namebtn=ttk.Button(scrollable_frame,text=i,command=lambda i=i: show_column(i))
    namebtn.pack()
    namebtn.bind("<MouseWheel>", _on_mousewheel)
    #tk.Label(scrollable_frame).pack(side="top",fill=X)
    #tk.Label(scrollable_frame).pack()

canvas.bind("<MouseWheel>", _on_mousewheel)
scrollable_frame.bind("<MouseWheel>", _on_mousewheel)
scrollable_frame.bind("<Button-1>", myprint)

container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


#monat.bind("<<ComboboxSelected>>", callbackFunc)
#ende=tk.Button(root,text="Ende",fg="red",command=stop)

#ende.pack()
root.mainloop() 
"""


if __name__ == "__main__":
    
    countdown().main_window()