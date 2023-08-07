import tkinter as tk
from tkinter import ttk
import time
import requests
from tkinter import messagebox
from playsound import playsound

numbers=[0,1,2,3,4,5,6,7,8,9]
def download_mp3(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print("MP3 file downloaded successfully.")
        else:
            print("Failed to download MP3 file. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

def play_sound(file_path):
    try:
        playsound(file_path)
    except Exception as e:
        print("An error occurred:", e)


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)
def controlname(name,reference):
    if not name:
        messagebox.showerror('Error', f'{reference} empty')
        return False
    elif len(name)<3:
        messagebox.showerror('Error', f'{reference} is too short')
        return False
    elif has_numbers(name):
        messagebox.showerror('Error', f'{reference} has numbres')
        return False
    
    return True
def controlnum(phonenumber,reference):
    if not phonenumber:
        messagebox.showerror('Error', f'{reference} empty')
        return False
    elif phonenumber.isnumeric() ==False:
        messagebox.showerror('Error', f'Wrong {reference} (wrong input)')
        return False
    elif len(phonenumber)!=11:
        messagebox.showerror('Error', f'Wrong {reference} length (start with 0)')
        return False


    return True
def controlage(age):
    if not age:
        messagebox.showerror('Error', f'age empty (3-99)')
        return False
    elif age.isnumeric()==False:
        messagebox.showerror('Error', f'Wrong age (3-99)')
        return False
    elif len(age)>2:
        messagebox.showerror('Error', f'Wrong age (3-99)')
        return False

    return True
        

        #BalloonPop.goflag=True
namee='test'
def submit():       
    with open('personal_info.txt', 'a') as f:
        #if controlname(name_entry.get(),'First name') and controlname(last_name_entry.get(),'Last name') and controlnum(fathers_phone_entry.get(),"Father's Phone Number") and controlnum(mothers_phone_entry.get(),"Mother's Phone Number") and controlage(age_entry.get()) and controlname(major_entry.get(),'Major') :
            f.write(f'First Name: {name_entry.get()}\n')
            f.write(f'Last Name: {last_name_entry.get()}\n')
            f.write(f"Father's Phone Number: {fathers_phone_entry.get()}\n")
            f.write(f"Mother's Phone Number: {mothers_phone_entry.get()}\n")
            f.write(f'Age: {age_entry.get()}\n')
            f.write(f'Major: {major_entry.get()}\n\n')
            global namee
            namee=name_entry.get()
            root.destroy()

            
    return namee

def on_submit():
    global result_variable
    result_variable = submit()
    #return result_variable


root = tk.Tk()
root.title('Personal Information Form')

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

name_label = ttk.Label(mainframe, text='First Name:')
name_label.grid(column=1, row=1, sticky=tk.W)
name_entry = ttk.Entry(mainframe)
name_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

last_name_label = ttk.Label(mainframe, text='Last Name:')
last_name_label.grid(column=1, row=2, sticky=tk.W)
last_name_entry = ttk.Entry(mainframe)
last_name_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))

fathers_phone_label = ttk.Label(mainframe, text="Father's Phone Number:")
fathers_phone_label.grid(column=1, row=3, sticky=tk.W)
fathers_phone_entry = ttk.Entry(mainframe)
fathers_phone_entry.grid(column=2, row=3, sticky=(tk.W, tk.E))

mothers_phone_label = ttk.Label(mainframe, text="Mother's Phone Number:")
mothers_phone_label.grid(column=1,row=4 ,sticky=tk.W)
mothers_phone_entry = ttk.Entry(mainframe)
mothers_phone_entry.grid(column=2,row=4 ,sticky=(tk.W, tk.E))

age_label = ttk.Label(mainframe,text='Age:')
age_label.grid(column=1,row=5 ,sticky=tk.W)
age_entry = ttk.Entry(mainframe)
age_entry.grid(column=2,row=5 ,sticky=(tk.W, tk.E))

major_label = ttk.Label(mainframe,text='Major:')
major_label.grid(column=1,row=6 ,sticky=tk.W)
major_entry = ttk.Entry(mainframe)
major_entry.grid(column=2,row=6 ,sticky=(tk.W, tk.E))

submit_button = ttk.Button(mainframe, text='Submit', command=on_submit)
submit_button.grid(column=2,row=7)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5,pady=5)

root.mainloop()
print(namee)