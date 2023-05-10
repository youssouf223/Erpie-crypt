import os
import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText


def decryptage_screen():
    cryptage_screen=Tk()
    cryptage_screen.title("Page de decryptage")
    cryptage_screen.geometry("925x500+300+200")
    cryptage_screen.config(bg='#fff')


    login_frame = Frame(cryptage_screen, width=800, height=720, bg="white")
    login_frame.pack()

    # erie_crypt = tk.Label(cryptage_screen, text="ERIE-CRYPT", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    # erie_crypt.pack(pady=15)
    file_str = tk.StringVar()
    my_str = tk.StringVar()
    my_str.set("Set Path here")
    file_str.set("File str")
    text = []
    def upload_file():
        file = filedialog.askopenfilename()
        if(file):
            my_str.set(file)
            fob=open(file,'r')
            
            print(fob.read())
            #file = filedialog.askopenfile()
            #print(file.read())
            for line in fob:
                racer = line.split()
                text.append(racer)
            fob.close()
            return file_str.set(text)
    my_dir = ""
    def ask_folder():
        my_dir = filedialog.askdirectory() # select directory 
        folder_direct.config(text=my_dir) # update the text of Label with directory path

    tk.Button(cryptage_screen, text ='Choississez un fichier', width=25, pady=7, bg="#57a1f8", fg="white",command = lambda:upload_file()).place(x=80, y=80)
    tk.Button(cryptage_screen, text ='Choississez un dossier', width=25, pady=7, bg="#57a1f8", fg="white",command = lambda:ask_folder()).place(x=270, y=80)
    tk.Button(cryptage_screen, text ='Choississez un fichier', width=25, pady=7, bg="#57a1f8", fg="white",command = lambda:upload_file()).place(x=460, y=80)
    tk.Button(cryptage_screen, text ='Paramètres', width=25, pady=7, bg="#333", fg="white",command = lambda:upload_file()).place(x=650, y=80)

    folder_direct=tk.Label(cryptage_screen,text=my_dir,bg='white',font=15)
    folder_direct.place(x=300, y=150)
    
    # file_direct=tk.Label(cryptage_screen,text=my_str,bg='white',font=15)
    # file_direct.place(x=300, y=200)

    # ScrolledText(cryptage_screen, bg="white", fg="blue", font="sans 12 bold", height=10, width=20).place(x=380, y=200)
    file_content=tk.Label(cryptage_screen,text="file_str",bg='white',font=15)
    file_content.place(x=380, y=200)

    cryptage_screen.mainloop()

def cryptage_screen():
    cryptage_screen=Tk()
    cryptage_screen.title("Page de cryptage")
    cryptage_screen.geometry("925x500+300+200")
    cryptage_screen.config(bg='#fff')


    login_frame = Frame(cryptage_screen, width=800, height=720, bg="white")
    login_frame.pack()

    # erie_crypt = tk.Label(cryptage_screen, text="ERIE-CRYPT", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    # erie_crypt.pack(pady=15)
    file_str = tk.StringVar()
    my_str = tk.StringVar()
    my_str.set("Set Path here")
    file_str.set("File str")
    text = []
    def upload_file():
        file = filedialog.askopenfilename()
        if(file):
            my_str.set(file)
            fob=open(file,'r')
            
            print(fob.read())
            #file = filedialog.askopenfile()
            #print(file.read())
            for line in fob:
                racer = line.split()
                text.append(racer)
            fob.close()
            return file_str.set(text)
    my_dir = ""
    def ask_folder():
        my_dir = filedialog.askdirectory() # select directory 
        folder_direct.config(text=my_dir) # update the text of Label with directory path

    tk.Button(cryptage_screen, text ='Choississez un fichier', width=25, pady=7, bg="#57a1f8", fg="white",command = lambda:upload_file()).place(x=80, y=80)
    tk.Button(cryptage_screen, text ='Choississez un dossier', width=25, pady=7, bg="#57a1f8", fg="white",command = lambda:ask_folder()).place(x=270, y=80)
    tk.Button(cryptage_screen, text ='Choississez un fichier', width=25, pady=7, bg="#57a1f8", fg="white",command = lambda:upload_file()).place(x=460, y=80)
    tk.Button(cryptage_screen, text ='Paramètres', width=25, pady=7, bg="#333", fg="white",command = lambda:upload_file()).place(x=650, y=80)

    folder_direct=tk.Label(cryptage_screen,text=my_dir,bg='white',font=15)
    folder_direct.place(x=300, y=150)
    
    # file_direct=tk.Label(cryptage_screen,text=my_str,bg='white',font=15)
    # file_direct.place(x=300, y=200)

    # ScrolledText(cryptage_screen, bg="white", fg="blue", font="sans 12 bold", height=10, width=20).place(x=380, y=200)
    file_content=tk.Label(cryptage_screen,text="file_str",bg='white',font=15)
    file_content.place(x=380, y=200)

    cryptage_screen.mainloop()

def login():
    login_screen=Tk()
    login_screen.title("Page d'acceuil")
    login_screen.geometry("925x500+300+200")
    login_screen.config(bg='#fff')

    login_frame = tk.Frame(login_screen, width=800, height=720, bg="white")
    login_frame.place(x=0, y=0)

    erie_crypt = tk.Label(login_screen, text="ERIE-CRYPT", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    erie_crypt.place(x=350, y=50)

    tk.Button(login_frame, width=40, padx=5, pady=5,text="Cryptage", bg="#57a1f8", fg="white", border=0, command=cryptage_screen).place(x=150, y=250)
    tk.Button(login_frame, width=40, padx=5, pady=5,text="Decryptage", bg="black", fg="white", border=0, command=decryptage_screen).place(x=450, y=250)

    login_screen.mainloop()
    # try:
    #     with open("credential.txt", "r") as f:
    #         info = f.readlines()
    #         i  = 0
    #         for e in info:
    #             u, p =e.split(",")
    #             if u.strip() == user.get() and p.strip() == code.get():
    #                 home_screen = Toplevel(root)
    #                 home_screen.title("Page d'accueil")
    #                 home_screen.geometry("925x500+300+200")
    #                 home_screen.config(bg="white")

    #                 Label(home_screen, text="Hello EveryOne", bg="#fff", font=('Algerian', 50, ''))

    #                 home_screen.mainloop()
    #                 i = 1
    #                 break
    #         if i==0:
    #             messagebox.showinfo("Error", "Please provide correct username and password!!")
    # except:
    #     messagebox.showinfo("Error", "Please provide correct username and password!!")


root = Tk()
root.title="Connexion"
root.geometry("925x500+300+200")
root.configure(bg='#fff')
root.resizable(False, False)

login_img = PhotoImage(file="login.png")
Label(root, image=login_img, bg="white").place(x=50, y=50)
##################---------Side Images
####### Erpie_logo
erpie_img = Image.open("erie.png")
# Resize the image
erpie_resized_image = erpie_img.resize((200, 80))

# Convert the resized image to Tkinter format
logo_image = ImageTk.PhotoImage(erpie_resized_image)
Label(root, image=logo_image, bg="white").place(x=0, y=0)
######## End of Erpie logo

####### Mali Flag
drapeau_img = Image.open("drapeau.png")
# Resize the image
drapeau_resized_image = drapeau_img.resize((200, 30))

# Convert the resized image to Tkinter format
drapeau_image = ImageTk.PhotoImage(drapeau_resized_image)
Label(root, image=drapeau_image, bg="white").place(x=700, y=0)
####### End of Mali Flag

####### Africa-digital Flag
africa_digital_img = Image.open("africa-digital.jpg")
# Resize the image
africa_digital_resized_image = africa_digital_img.resize((100, 100))

# Convert the resized image to Tkinter format
africa_digital_image = ImageTk.PhotoImage(africa_digital_resized_image)
Label(root, image=africa_digital_image).place(x=0, y=400)
####### End of Africa-digital Flag

frame = Frame(root, width=350, height=450, bg="white")
frame.place(x=480, y=100)

heading = Label(frame, text="ERPIE-CRYPT", bg="white", font=("Microsoft YaHei UI Light", 25, "bold"))
heading.place(x=70, y=0)

connexion_text = Label(frame, text="Connexion", bg="white", font=("Microsoft YaHei UI Light", 15, "bold"))
connexion_text.place(x=120, y=40)
##################---------Side Images
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0, "Nom d'utilisateur")


user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Nom d'utilisateur")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)
############################################
def on_enter(e):
    code.delete(0, 'end')
def on_leave(e):
    name=code.get()
    if name=="":
        code.insert(0, "Nom d'utilisateur")

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Mot de passe")
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)
######################################

Button(frame, width=39, pady=7, text="Se connecter", bg="#57a1f8", fg="white", border=0, command=login).place(x=35, y=204)
Label = Label(frame, text="Vous n'avez pas de compte ?", fg="black", font=("Microsoft YaHei UI Light", 9))
Label.place(x=75, y=270)

################
sign_up = Button(frame, width=6, text="Incrire", border=0, bg="white", cursor="hand2", fg="#57a1f8")
sign_up.place(x=215, y=270)

root.mainloop()

