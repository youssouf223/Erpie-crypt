from os import walk
import os
import tkinter as tk
import hashlib, timeit, sys
import random
from tkinter import ttk,filedialog
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
from tkinter.filedialog import askopenfile
from tkinter import filedialog
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding


def encryptFile(password, IV, filename):
    key = hashlib.sha256(password.encode()).digest()

    with open(filename, 'rb') as f:
        file_data = f.read()

    starttime = timeit.default_timer()

    cipher = AES.new(key, AES.MODE_CBC , IV)
    padded_file_data = Padding.pad(file_data, 16)
    encrypt_file_data = cipher.encrypt(padded_file_data)

    time = timeit.default_timer() - starttime

    with open(filename, 'wb') as ef:
        ef.write(encrypt_file_data)
    return 'Done in' + str(time) + 'second(s)'

def decryptFile(password, IV, filename):
    key = hashlib.sha256(password.encode()).digest()

    with open(filename, 'rb') as f:
        file_data = f.read()

    starttime = timeit.default_timer()

    cipher = AES.new(key, AES.MODE_CBC , IV)
    decrypt_file_data = cipher.decrypt(file_data)
    unpadded_file_data = Padding.unpad(decrypt_file_data, 16)

    time = timeit.default_timer() - starttime

    with open(filename, 'wb') as ef:
        ef.write(unpadded_file_data)
    return 'Done in' + str(time) + 'second(s)'


class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg="white")
        load = Image.open("login.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo, bg="white")
        label.image=photo
        label.place(x=50,y=50)
        ######## Erpie logo
        erpie_img = Image.open("erie.png")
        erie_resized_image = erpie_img.resize((200, 80))
        photo_erpie = ImageTk.PhotoImage(erie_resized_image)
        label_erpie = tk.Label(self, image=photo_erpie, bg="white")
        label_erpie.image=photo_erpie
        label_erpie.place(x=0,y=0)
        ######## End of Erpie logo
        
        ######## Drapeau logo
        drapeau_img = Image.open("drapeau.png")
        drapeau_resized_image = drapeau_img.resize((150, 30))
        drapeau_mali = ImageTk.PhotoImage(drapeau_resized_image)
        label_drapeau = tk.Label(self, image=drapeau_mali, bg="white")
        label_drapeau.image=drapeau_mali
        label_drapeau.place(x=600,y=0)
        ######## End of Drapeau logo
        
        ######## Africa digital logo
        ad_img = Image.open("africa-digital.jpg")
        ad_resized_image = ad_img.resize((100, 100))
        ad_logo = ImageTk.PhotoImage(ad_resized_image)
        label_ad = tk.Label(self, image=ad_logo, bg="white")
        label_ad.image=ad_logo
        label_ad.place(x=0,y=400)
        ######## End of Africa digital logo

        frame = tk.Frame(self, width=350, height=450, bg="white")
        frame.place(x=480, y=100)

        heading = tk.Label(frame, text="ERPIE-CRYPT", bg="white", font=("Microsoft YaHei UI Light", 25, "bold"))
        heading.place(x=70, y=0)

        connexion_text = tk.Label(frame, text="Connexion", bg="white", font=("Microsoft YaHei UI Light", 15, "bold"))
        connexion_text.place(x=120, y=40)
        ##################---------Side Images
        def on_enter(e):
            user.delete(0, 'end')
        def on_leave(e):
            name=user.get()
            if name=="":
                user.insert(0, "Nom d'utilisateur")


        user = tk.Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        user.place(x=30, y=80)
        user.insert(0, "Nom d'utilisateur")
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)

        tk.Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)
        ############################################
        def on_enter(e):
            code.delete(0, 'end')
        def on_leave(e):
            name=code.get()
            if name=="":
                code.insert(0, "Nom d'utilisateur")

        code = tk.Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11), show="*")
        code.place(x=30, y=150)
        code.insert(0, "Mot de passe")
        code.bind('<FocusIn>', on_enter)
        code.bind('<FocusOut>', on_leave)

        tk.Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)
        ######################################
        
        def login():
            try:
                with open("credential.txt", "r") as f:
                    info = f.readlines()
                    i  = 0
                    for e in info:
                        u, p =e.split(",")
                        if u.strip() == user.get() and p.strip() == code.get():
                            controller.show_frame(SecondPage)
                            i = 1
                            break
                    if i==0:
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")


        tk.Button(frame, width=39, pady=7, text="Se connecter", bg="#57a1f8", fg="white", border=0, command=login).place(x=35, y=204)
        
class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg="white")
        load = Image.open("login.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo, bg="white")
        label.image=photo
        label.place(x=350,y=50)
        ######## Erpie logo
        erpie_img = Image.open("erie.png")
        erie_resized_image = erpie_img.resize((200, 80))
        photo_erpie = ImageTk.PhotoImage(erie_resized_image)
        label_erpie = tk.Label(self, image=photo_erpie, bg="white")
        label_erpie.image=photo_erpie
        label_erpie.place(x=0,y=0)
        ######## End of Erpie logo
        
        ######## Drapeau logo
        drapeau_img = Image.open("drapeau.png")
        drapeau_resized_image = drapeau_img.resize((150, 30))
        drapeau_mali = ImageTk.PhotoImage(drapeau_resized_image)
        label_drapeau = tk.Label(self, image=drapeau_mali, bg="white")
        label_drapeau.image=drapeau_mali
        label_drapeau.place(x=600,y=0)
        ######## End of Drapeau logo
        
        ######## Africa digital logo
        ad_img = Image.open("africa-digital.jpg")
        ad_resized_image = ad_img.resize((100, 100))
        ad_logo = ImageTk.PhotoImage(ad_resized_image)
        label_ad = tk.Label(self, image=ad_logo, bg="white")
        label_ad.image=ad_logo
        label_ad.place(x=0,y=400)
        ######## End of Africa digital logo

        tk.Button(self, width=39, pady=7, text="Cryptage", bg="#57a1f8", fg="white", border=0, command=lambda: controller.show_frame(ThirdPage)).place(x=35, y=150)
        tk.Button(self, width=39, pady=7, text="Decryptage", bg="black", fg="white", border=0, command=lambda: controller.show_frame(ForthPage)).place(x=35, y=250)
        tk.Button(self, width=39, pady=7, text="Paramètre", bg="red", fg="white", border=0, command=lambda: controller.show_frame(FithPage)).place(x=400, y=400)
#Cryptage de données        
class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg="white")
        
        heading = tk.Label(self, text="Cryptage de données", bg="white", font=("Microsoft YaHei UI Light", 15, "bold"))
        heading.place(x=300, y=15)

        load = Image.open("login.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo, bg="white")
        label.image=photo
        label.place(x=400,y=150)
        ######## Erpie logo
        erpie_img = Image.open("erie.png")
        erie_resized_image = erpie_img.resize((200, 80))
        photo_erpie = ImageTk.PhotoImage(erie_resized_image)
        label_erpie = tk.Label(self, image=photo_erpie, bg="white")
        label_erpie.image=photo_erpie
        label_erpie.place(x=0,y=0)
        ######## End of Erpie logo
        
        ######## Drapeau logo
        drapeau_img = Image.open("drapeau.png")
        drapeau_resized_image = drapeau_img.resize((150, 30))
        drapeau_mali = ImageTk.PhotoImage(drapeau_resized_image)
        label_drapeau = tk.Label(self, image=drapeau_mali, bg="white")
        label_drapeau.image=drapeau_mali
        label_drapeau.place(x=600,y=0)
        ######## End of Drapeau logo
        
        ######## Africa digital logo
        ad_img = Image.open("africa-digital.jpg")
        ad_resized_image = ad_img.resize((100, 100))
        ad_logo = ImageTk.PhotoImage(ad_resized_image)
        label_ad = tk.Label(self, image=ad_logo, bg="white")
        label_ad.image=ad_logo
        label_ad.place(x=0,y=400)
        ######## End of Africa digital logo

        file_str = tk.StringVar()
        my_str = tk.StringVar()
        info = tk.StringVar()
        info.set("")
        file_direct=tk.Label(self,textvariable=my_str,bg='white',font=15)
        file_direct.place(x=50, y=125)
        
        notification=tk.Label(self,textvariable=info,bg='green', fg="white", font=15)
        notification.place(x=100, y=250)

        # trv=ttk.Treeview(self,selectmode='browse', height=12)  
        # trv.place(x=100,y=200, width=300)
        # trv['show'] = 'tree'
        my_str.set("")
        file_str.set("")
        def upload_file():
            file = filedialog.askopenfilename()
            encryptFile("password","1234567890ABCDEF".encode(), file)
            info.set("Fichier crypté avec succès!")
            # Générer une chaîne de caractères aléatoires de 64 caractères
            # random_string = random.choices('0123456789abcdef', k=120)
            # my_str.set(file)
            # if file:        
            #     # fob=open(file,'r')    
            #     i=0
            #     for data in random_string:
            #         trv.insert("",'end',iid=i,text=data)
            #         i=i+1
            # else:
            #     print("Aucun fichier choisi")
                
        my_dir = ""
        def ask_folder():
            directory = filedialog.askdirectory() # select directory 
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file:
                        # print(os.path.join(root, file))
                        encryptFile("password", "1234567890ABCDEF".encode(), os.path.join(root, file))

        tk.Button(self, text ='Choississez un fichier', width=25, pady=7, bg="#57a1f8", fg="white",command = lambda:upload_file()).place(x=80, y=80)
        tk.Button(self, text ='Choississez un dossier', width=25, pady=7, bg="#57a1f8", fg="white",command = lambda:ask_folder()).place(x=270, y=80)
        tk.Button(self, text ='Choississez un volume', width=25, pady=7, bg="#57a1f8", fg="white",command = lambda:upload_file()).place(x=460, y=80)

        tk.Button(self, text ='Rétour', width=25, pady=7, bg="#333", fg="white",command = lambda: controller.show_frame(SecondPage)).place(x=650, y=80)
        
        # tk.Button(self, text ='Chiffrer', width=25, pady=7, bg="green", fg="white",command = lambda:upload_file()).place(x=80, y=160)

        folder_direct=tk.Label(self,text=my_dir,bg='white',font=15)
        folder_direct.place(x=50, y=125)

        # ScrolledText(self, bg="white", fg="blue", font="sans 12 bold", height=10, width=20).place(x=380, y=200)
        file_content=tk.Label(self,text="",bg='white',font=15)
        file_content.place(x=380, y=200)
#Decryptage de données
class ForthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg="white")
        
        heading = tk.Label(self, text="Decryptage de données", bg="white", font=("Microsoft YaHei UI Light", 15, "bold"))
        heading.place(x=300, y=15)

        load = Image.open("login.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo, bg="white")
        label.image=photo
        label.place(x=400,y=150)
        ######## Erpie logo
        erpie_img = Image.open("erie.png")
        erie_resized_image = erpie_img.resize((200, 80))
        photo_erpie = ImageTk.PhotoImage(erie_resized_image)
        label_erpie = tk.Label(self, image=photo_erpie, bg="white")
        label_erpie.image=photo_erpie
        label_erpie.place(x=0,y=0)
        ######## End of Erpie logo
        
        ######## Drapeau logo
        drapeau_img = Image.open("drapeau.png")
        drapeau_resized_image = drapeau_img.resize((150, 30))
        drapeau_mali = ImageTk.PhotoImage(drapeau_resized_image)
        label_drapeau = tk.Label(self, image=drapeau_mali, bg="white")
        label_drapeau.image=drapeau_mali
        label_drapeau.place(x=600,y=0)
        ######## End of Drapeau logo
        
        ######## Africa digital logo
        ad_img = Image.open("africa-digital.jpg")
        ad_resized_image = ad_img.resize((100, 100))
        ad_logo = ImageTk.PhotoImage(ad_resized_image)
        label_ad = tk.Label(self, image=ad_logo, bg="white")
        label_ad.image=ad_logo
        label_ad.place(x=0,y=400)
        ######## End of Africa digital logo

        file_str = tk.StringVar()
        my_str = tk.StringVar()
        info = tk.StringVar()
        info.set("")
        file_direct=tk.Label(self,textvariable=my_str,bg='white',font=15)
        file_direct.place(x=50, y=125)
        notification=tk.Label(self,textvariable=info,bg='green', fg="white", font=15)
        notification.place(x=100, y=250)
        # trv=ttk.Treeview(self,selectmode='browse', height=12)  
        # trv.place(x=100,y=200, width=300)
        # trv['show'] = 'tree'
        my_str.set("")
        file_str.set("")
        def upload_file():
            file = filedialog.askopenfilename()
            if(file):
                decryptFile("password", "1234567890ABCDEF".encode(), file)
                info.set("Fichier decrypté avec succès!")
                # my_str.set(file)
                # if file:        
                #     fob=open(file,'r')    
                #     i=0
                #     for data in fob:
                #         trv.insert("",'end',iid=i,text=data)
                #         i=i+1
                # else:
                #     print("Aucun fichier choisi")
                
                # print(fob.read())
                #file = filedialog.askopenfile()
                #print(file.read())
        my_dir = ""
        def ask_folder():
            directory = filedialog.askdirectory() # select directory 
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file:
                        # print(os.path.join(root, file))
                        decryptFile("password", "1234567890ABCDEF".encode(), os.path.join(root, file))
                        
        tk.Button(self, text ='Choississez un fichier', width=25, pady=7, bg="#57a1f8", fg="white",command = lambda:upload_file()).place(x=80, y=80)
        tk.Button(self, text ='Choississez un dossier', width=25, pady=7, bg="#57a1f8", fg="white",command = lambda:ask_folder()).place(x=270, y=80)
        tk.Button(self, text ='Choississez un volume', width=25, pady=7, bg="#57a1f8", fg="white",command = lambda:upload_file()).place(x=460, y=80)
        
        tk.Button(self, text ='Rétour', width=25, pady=7, bg="#333", fg="white",command = lambda: controller.show_frame(SecondPage)).place(x=650, y=80)
        
        folder_direct=tk.Label(self,text=my_dir,bg='white',font=15)
        folder_direct.place(x=50, y=125)

        # ScrolledText(self, bg="white", fg="blue", font="sans 12 bold", height=10, width=20).place(x=380, y=200)
        file_content=tk.Label(self,text="",bg='white',font=15)
        file_content.place(x=380, y=200)

#Paramètrage        
class FithPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg="white")
        
        heading = tk.Label(self, text="Decryptage de données", bg="white", font=("Microsoft YaHei UI Light", 15, "bold"))
        heading.place(x=300, y=15)

        load = Image.open("login.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo, bg="white")
        label.image=photo
        label.place(x=400,y=150)
        ######## Erpie logo
        erpie_img = Image.open("erie.png")
        erie_resized_image = erpie_img.resize((200, 80))
        photo_erpie = ImageTk.PhotoImage(erie_resized_image)
        label_erpie = tk.Label(self, image=photo_erpie, bg="white")
        label_erpie.image=photo_erpie
        label_erpie.place(x=0,y=0)
        ######## End of Erpie logo
        
        ######## Drapeau logo
        drapeau_img = Image.open("drapeau.png")
        drapeau_resized_image = drapeau_img.resize((150, 30))
        drapeau_mali = ImageTk.PhotoImage(drapeau_resized_image)
        label_drapeau = tk.Label(self, image=drapeau_mali, bg="white")
        label_drapeau.image=drapeau_mali
        label_drapeau.place(x=600,y=0)
        ######## End of Drapeau logo
        
        ######## Africa digital logo
        ad_img = Image.open("africa-digital.jpg")
        ad_resized_image = ad_img.resize((100, 100))
        ad_logo = ImageTk.PhotoImage(ad_resized_image)
        label_ad = tk.Label(self, image=ad_logo, bg="white")
        label_ad.image=ad_logo
        label_ad.place(x=0,y=400)
        ######## End of Africa digital logo
    
        # Create a Combobox for Type
        values = ['AES', 'DES', 'SCS']
        sha = ttk.Combobox(self, values=values, width=42)
        sha.place(x=100, y=85)
        tk.Frame(self, width=270, height=2, bg="black").place(x=100, y=105)

        # Create a Combobox for Sha
        values = ['Sha-256', 'Sha-125', 'Sha-254']
        type = ttk.Combobox(self, values=values, width=42)
        type.place(x=100, y=125)
        tk.Frame(self, width=270, height=2, bg="black").place(x=100, y=145)

        def on_enter(e):
            file_password.delete(0, 'end')
        def on_leave(e):
            name=file_password.get()
            if name=="":
                file_password.insert(0, "Clé de chiffrement")

        file_password = tk.Entry(self, width=16, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        file_password.place(x=100, y=175)
        file_password.insert(0, "Clé de chiffrement")
        file_password.bind('<FocusIn>', on_enter)
        file_password.bind('<FocusOut>', on_leave)

        tk.Frame(self, width=270, height=2, bg="black").place(x=100, y=195)

        def set_setting():
            if type.get()!="" or sha.get()!="" or file_password.get()!="":
                with open("parametre.txt", "a") as f:
                    f.write(type.get()+","+sha.get()+","+file_password.get()+"\n")
                    messagebox.showinfo("Paramètre validé avec succès!")
            else:
                messagebox.showinfo("Erreur", "Svp veuillez renseigner tous les champs!")

        tk.Button(self, text ='Valider', width=25, pady=7, padx=7, bg="#57a1f8", fg="white", command=set_setting).place(x=125, y=250)

        tk.Button(self, text ='Rétour', width=25, pady=7, padx=7, bg="#333", fg="white",command = lambda: controller.show_frame(SecondPage)).place(x=650, y=80)



class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #creating a window
        window = tk.Frame(self)
        window.pack()
        
        window.grid_rowconfigure(0, minsize = 500)
        window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage, ForthPage, FithPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(FirstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Système de cryptage")
        self.geometry("925x500+300+200")
        self.configure(bg="#fff")
        self.resizable(False, False)
            
app = Application()
app.maxsize(925,500)
app.mainloop()