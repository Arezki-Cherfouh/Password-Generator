import random 
import secrets
import string
import tkinter as tk
from tkinter import ttk
mn=tk.Tk()
mn.title('PasswordGenerator')
mn.geometry('500x300')
hl=tk.Label(mn,text="Option :")
hl.place(x=20,y=20)
unite=["1. Use a strong password generation system","2. Use a random password generation system"]
h=ttk.Combobox(mn,values=unite,width=38,cursor="hand2")
h.place(x=100,y=20)
hls=tk.Label(mn,text="Password length :")
hls.place(x=20,y=100)
hs=ttk.Entry(mn)
hs.place(x=150,y=100)
hp = tk.Label(mn, text="", font=("Courier", 12), fg="blue")
hp.place(x=20, y=200)
def generatepassword():
    characters = string.ascii_letters + string.digits + string.punctuation
    length=hs.get()
    try:
        length=int(length)
        password = ''.join(random.choice(characters) for c in range(length))
        hp.config(text=password)
        mn.update()
        # if hp:
        #     hp.place_forget()
        # hp=tk.Label(mn,text=password)
        # hp.place_forget()
        # hp.place(x=20,y=200)
    except ValueError:
        return
    
def generatepasswordsecure():
    characters = string.ascii_letters + string.digits + string.punctuation
    length=hs.get()
    try:
        length=int(length)
        password = ''.join(secrets.choice(characters) for c in range(length))
        # if hp:
        #     hp.place_forget()
        # hp=tk.Label(mn,text=password)
        # hp.place(x=20,y=200)
        hp.config(text=password)
        mn.update()
    except ValueError:
        return
    
# print("1. Use a strong password generation system\n2. Use a random password generation system")
def useui():
    try:
        use=h.get()
        if use=="1" or use=="1. Use a strong password generation system" or use=="s" or use=="strong" or use=="Strong":
            generatepasswordsecure()
        elif use=="2" or use=="2. Use a random password generation system" or use=="r" or use=="random" or use=="Random":
            generatepassword()
        else :return
    except ValueError:
        return
hbt=tk.Button(mn,text="Generate",bg="red",command=lambda:useui(),cursor="hand2")
hbt.place(x=400,y=100)
mn.mainloop()