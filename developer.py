import tkinter
from tkinter.ttk import*
from tkinter import*
from PIL import ImageTk,Image
from time import strftime
from tkinter import messagebox



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x690+0+0")
        self.root.title("Developers")

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

        lbl = Label(title_lbl, font =('calibri',16,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=-5,width=120,height=55)
        time()

        b1_2=Button(title_lbl,text="BACK",cursor="hand2",command=self.bhagbc,font=("calibri",15,"bold"),bg="darkblue",fg="white")
        b1_2.place(x=1170,y=3,width=150,height=35) 

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=15,y=55,width=1320,height=600)
        title1_lbl=Label(main_frame,text="MEET OUR TEAM",font=("Britannic Bold",20,"bold"),bg="white",fg="blue")
        title1_lbl.place(x=0,y=0,width=1270,height=35) 

        #left label
        Left_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,text=" NISHANT PRAJAPATI ",font=("calibri",20,"bold"))
        Left_frame.place(x=10,y=40,width=420,height=500)
        
        img_left=Image.open(r"Nishant.jpg")
        
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=10,width=400,height=220)

        #Middle label
        Middle_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,text=" YASH SRIVASTAV ",font=("calibri",20,"bold"))
        Middle_frame.place(x=430,y=40,width=440,height=500)
        
        img_middle=Image.open(r"yash.jpg")
        
        self.photoimg_middle=ImageTk.PhotoImage(img_middle)
        
        f_lbl=Label(Middle_frame,image=self.photoimg_middle)
        f_lbl.place(x=10,y=10,width=400,height=220)

        #right label
        Right_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,text=" APOORVA MISHRA ",font=("calibri",20,"bold"))
        Right_frame.place(x=870,y=40,width=430,height=500)
        
        img_right=Image.open(r"apoorva.jpg")
        
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=10,y=10,width=400,height=220)

    def bhagbc(self):
        self.bhagbc=parent=self.root
        self.root.destroy()


if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()