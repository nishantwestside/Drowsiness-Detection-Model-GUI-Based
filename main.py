#Created by Yash Srivastav | Nishant Prajapati 

import tkinter
from tkinter.ttk import*
from tkinter import*
from PIL import ImageTk,Image
from time import strftime
from tkinter import messagebox
from developer import Developer
import os



class Drowsiness:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x690+0+0")
        self.root.title("Drowsiness Detection Model")

        #first image
        img=Image.open(r"cover.jpg")
        img=img.resize((400,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=130)

        #second image
        img1=Image.open(r"a.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=401,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"c.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=903,y=0,width=500,height=130)

        #bg image
        img3=Image.open(r"d1.jpg")
        img3=img3.resize((1430,610),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1430,height=610)
    
        #Tittle main
        title_lbl=Label(bg_img,text="DROWSINESS DETECTION MODEL",font=("Britannic Bold",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=-2,y=0,width=1370,height=45)   

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font =('Calibri',16,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=-5,width=120,height=55)
        time() 

        #start button
        img4=Image.open(r"—Pngtree—webcam icon flat style_5170167.png")
        img4=img4.resize((200,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=open_ddm,cursor="hand2") #add link to self.,cursor between
        b1.place(x=120,y=200,width=220,height=150) 

        b1_1=Button(bg_img,text="START",command=open_ddm,cursor="hand2",font=("Calibri",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=120,y=350,width=220,height=40)                             #add link to self.,cursor between

        #About button
        img5=Image.open(r"about.png")
        img5=img5.resize((190,140),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=open_about)
        b1.place(x=420,y=200,width=220,height=150)

        b1_1=Button(bg_img,text="ABOUT",cursor="hand2",command=open_about,font=("calibri",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=420,y=350,width=220,height=40)

        #Developers button
        img7=Image.open(r"clipart1841477.png")
        img7=img7.resize((180,130),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.developer_but)
        b1.place(x=720,y=200,width=220,height=150)

        b1_1=Button(bg_img,text="DEVELOPERS",cursor="hand2",command=self.developer_but,font=("calibri",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=720,y=350,width=220,height=40)

        #Exit button
        img6=Image.open(r"PikPng.com_exit-icon-png_5910321.png")
        img6=img6.resize((170,130),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.xit,cursor="hand2")
        b1.place(x=1020,y=200,width=220,height=150)

        b1_1=Button(bg_img,text="EXIT",command=self.xit,cursor="hand2",font=("Calibri",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1020,y=350,width=220,height=40)

    def xit(self):
        self.xit=tkinter.messagebox.askyesno("Drowsiness Detection","Are you sure want to exit?",parent=self.root)
        if self.xit >0:
            self.xit=tkinter.messagebox.showinfo("Drowsiness Detection","Safe Driving....")
            self.root.destroy()
        else:
            return

    def developer_but(self):
            self.new_window=Toplevel(self.root)
            self.app=Developer(self.new_window)
def open_ddm():
    path_ddm = 'C:/Users/user/Desktop/Drowsiness Detection Final/Drowsiness_Detection.py'
    os.system('"%s"' %path_ddm)

def open_about():
    path_about = 'C:/Users/user/Desktop/Drowsiness Detection Final/about.docx'
    os.system('"%s"' %path_about)

if __name__== "__main__":
    root=Tk()
    obj=Drowsiness(root)
    root.mainloop()