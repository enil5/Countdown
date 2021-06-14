"""
Author: enil5
Version: 2.0
Description:
    The program is written for a time line during a Spacex Falcon 9 start with 
    human on board. The first Version did automatic the next step. This Version 
    you are able to consider the time and for the end. Also you can set the seteps 
    on your own.
"""
import datetime
import time
import tkinter as tk
from tkinter import ttk
from tkinter import *

class countdown:

    def __init__(self):
        #This function initialites all important variables 
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
        #this is the main part of the program 
        #it calles it selfe all 500ms 
        #this progam sets the labels in the choosen colouer. 
    
        zaehler=0
        countl=["0:00:00","def"]
        
        zeit=datetime.datetime.now()
        zeit=zeit.replace(microsecond=0)
        

        if self.wtime==0:
            zeitab=datetime.datetime(int(self.jahr.get()),self.monat.current()+1,int(self.tag.get()),int(self.timel[0]),int((self.timel[1])),int(self.timel[2]))-zeit
        elif self.wtime==1:
            zeitab=zeit-datetime.datetime(int(self.jahr.get()),self.monat.current()+1,int(self.tag.get()),int(self.timel[0]),int((self.timel[1])),int(self.timel[2]))
 
        print(zeitab)
        
        if(str(zeitab)==countl[self.index]):
            print("Count ab")
            print(self.labels[8])
        
            self.combox[8].current(2)
            self.index+=1

        if str(zeitab)=="0:00:00":
            self.wtime=1

        try:
            for i in range (0,len(self.combox),1):

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
                
        except:
            pass

        self.anzeige.config(text=zeitab)
        try:
            self.anzeige2.config(text=zeitab)
        except:
            pass
        
        self.after_id=self.root.after(500, self.startcount)

    def setup(self):
        #this function starts and stops the counter
        #in addition the colour of the boutten will change

        if self.check==0:
            self.check=1
            self.start.config(text="Stop",fg="red")
            self.startcount()

        elif self.check==1:
            self.check=0
            self.start.config(text="Start",fg="green")

            if self.after_id:
                self.root.after_cancel(self.after_id) 
                self.after_id = None

    def create_workstation(self):
        #This function adds a lable to the main Window 
        #But this function is not good implemented 
        station=Toplevel()
        station.title("Add Name")
        self.e1=tk.Entry(station)
        btn=tk.Button(station,text="Save",command=self.verarbeiten)
        self.e1.pack()
        btn.pack()

    def verarbeiten(self):
        #This function is importatn for the secound window 
        #It looks if the secound window is generated. if not the founction is irrelevant
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
                
                self.mark.pack(fill=X,pady=5)

                self.bild2=tk.Frame(self.f7)
                self.bild2.config(bg="#1D2021")
                self.bild2.pack(fill=X,pady=5)

                self.mark2=tk.Label(self.bild2,text=i,bg="red")
                
                
                self.cobox=ttk.Combobox(self.bild2,values=self.zustand)
                self.cobox.pack(side=tk.RIGHT,fill=X)
                self.mark2.pack(fill=X)
                self.cobox.current(0)
                self.combox.append(self.cobox)
                self.labels2.append(self.mark2)
                self.counter+=1
            except:
                pass
    
    def newtime(self):
        #This function takes the time of the entry field 
        self.timel=[]
        try:
            self.timel=self.launchtime.get().split(":")
            self.timel[0]
            self.timel[1]
            self.timel[2]
        except:
            self.timel=["0","00","00"]
        
    def mainboard(self):
        #generates an empty secound window 
        self.top=Toplevel()
        self.top.title("Zweites Fenster")
        self.top.geometry("500x430")
        self.top.config(bg="#1D2021")

        self.top.protocol("WM_DELETE_WINDOW", self.setvar)      #this command disables the option to close the window with the X

        f1=tk.Frame(self.top)
        self.f4=tk.Frame(self.top,bg="#1D2021")

        f1.pack()
        self.f4.pack(fill=X)
        
        self.anzeige2=tk.Label(f1,text="NONE", fg="#29A3A3",bg="#1D2021",font="Helvetika 40")

        self.anzeige2.pack(fill=X)

    def setvar(self):
        self.checktop=1

    def newtopwin(self):
        #this functions checks if a secound window is already genearated.
        
        if self.checktop==1:
            self.mainboard()
            self.checktop=0
        
        else:
            pass

    def main_window(self):
        #generates a main Window.
        #In this Window you can choose the time. Start/Stop the countdown.
        #And you can set the labels to the actual status if what ever you want.
        
        self.root=tk.Tk()
        self.root.geometry("500x430")
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
        self.monat.pack(padx=5, pady=20, side= tk.LEFT)
        self.tag.pack(side= tk.LEFT)
        self.launchtime.pack(side=tk.LEFT, padx=5)
        self.monat.current(0)
        self.tag.current(0)

        self.root.mainloop() 


if __name__ == "__main__":
    
    countdown().main_window()
