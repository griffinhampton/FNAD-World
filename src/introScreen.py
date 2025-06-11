# Griffin Hampton in the case of a login esque page
from symtable import Class
from tkinter import *
import tkinter.messagebox
import customtkinter
import dependancyStuff.passwordStuff.password
from dependancyStuff.passwordStuff.passwordConfig import *


root=customtkinter.CTk()
root.geometry('450x450')
root.title('Login')

customtkinter.set_default_color_theme('blue')
customtkinter.set_appearance_mode('dark')
class LoginManager:
    def __init__(self):
        self.username = ""
        self.password = ""

    def login(self):
        radiohelp=radio.get()
        self.username = loginArea.get()
        self.password = passwordArea.get()
        self.guest = False

        if radiohelp==1:
            tkinter.messagebox.showinfo(title='hello',message=GUESTWARNING)
            self.guest = True
        else:
            if dependancyStuff.passwordStuff.password.password(self.username,self.password) == USERFOUND:
                tkinter.messagebox.showinfo(title='hello',message=USERFOUND)
            else:
                tkinter.messagebox.showinfo(title='hello', message=USERADDED)
        root.destroy()




loginManager = LoginManager()
frame=customtkinter.CTkFrame(master=root)
mainTitle=customtkinter.CTkLabel(master=root,font=('font',30,'bold'),text='FNAD User Login')
loginText=customtkinter.CTkLabel(master=frame,font=('font',20),text='Username')
loginArea=customtkinter.CTkEntry(master=frame,font=('font',15),width=200,placeholder_text='    Please insert username')
passwordText=customtkinter.CTkLabel(master=frame,font=('font',20),text='Password')
passwordArea=customtkinter.CTkEntry(master=frame,font=('font',15),width=200,placeholder_text='  Please insert password')
radio=customtkinter.CTkCheckBox(master=frame,text='Play as guest',font=('font',15))
loginButton=customtkinter.CTkButton(master=frame,text='Login',command=loginManager.login, font=('font',20))


mainTitle.pack(pady=5)
frame.pack(expand=True,fill='both',padx=20,pady=20)
loginText.pack(side=TOP)
loginArea.pack(side=TOP,pady=20)
passwordText.pack(side=TOP)
passwordArea.pack(side=TOP,pady=20)
loginButton.pack(side=BOTTOM,pady=60)
radio.place(x=250,y=225)

