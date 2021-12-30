from tkinter import *
import pandas as pd
import os

welcom = Tk()
welcom.geometry("600x410")
welcom.title("אילון ניסיון")

welcom_text = Label(text="Insert User Name", bg="red", fg="black", width="100", height="3").place(x=0, y=10)
welcom_text1 = Label(text="Insert Password", bg="green", fg="black", width="100", height="3").place(x=0, y=80)


def close_window():
    welcom.destroy()


username = StringVar()
password = StringVar()

un_enrty = Entry(textvariable=username, width="30").place(x=100, y=30)
pw_entry = Entry(textvariable=password, width="30").place(x=100, y=100)

button = Button(text="close", bg="green", fg="black", width="20", height="1",
                command=close_window).place(x=250, y=160)

col_a = 'Username'
col_b = 'Password'

dict = {col_a: ['eilon'], col_b: [1234]}
db_path = r'C:\Users\eilon.eilstein\Desktop\Python\users_DB.xlsx'
df_excel = pd.read_excel(db_path)
df = df_excel

df_label = Label(text=None, bg="green", fg="black", width="100", height="3").place(x=100, y=250)


def check():
    global df
    un = username.get()
    pw = password.get()
    return (len(un) > 3) and (len(pw) > 3) and (un not in list(df.Username)) and (pw not in list(df.Password))


def insert():
    global df_label
    if check():
        #df_label.destroy()
        un = username.get()
        pw = password.get()
        global df
        new_row = {col_a: un, col_b: pw}
        df = df.append(new_row, ignore_index=True)
        os.remove(db_path)
        df.to_excel(db_path, index=(False))
        df_label = Label(text=df, bg="green", fg="black", width="100", height="8").place(x=100, y=250)
    else:
        df_label = Label(text='ERROR', bg="green", fg="black", width="100", height="3").place(x=100, y=250)

def delete_db():
    global df
    os.remove(db_path)
    df = pd.DataFrame({col_a: [], col_b: []})
    df.to_excel(db_path, index=(False))
    
    

button_un = Button(text="Save Username and Password", bg="green", fg="black", width="25", height="1",
                   command=insert).place(x=50, y=160)

button_delete = Button(text="Truncate DB", bg="grey", fg="red", width="15", height="1",
                   command=delete_db).place(x=420, y=160)


welcom.mainloop()