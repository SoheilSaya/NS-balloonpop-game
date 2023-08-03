import tkinter as tk
from tkinter import ttk
import time
import BalloonPop
def submit():
    with open('personal_info.txt', 'a') as f:
        f.write(f'First Name: {name_entry.get()}\n')
        f.write(f'Last Name: {last_name_entry.get()}\n')
        f.write(f"Father's Phone Number: {fathers_phone_entry.get()}\n")
        f.write(f"Mother's Phone Number: {mothers_phone_entry.get()}\n")
        f.write(f'Age: {age_entry.get()}\n')
        f.write(f'Major: {major_entry.get()}\n\n')
    BalloonPop.speed = 8
    BalloonPop.score = 0
    BalloonPop.startTime = time.time()
    BalloonPop.totalTime = 600

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

submit_button = ttk.Button(mainframe,text='Submit',command=submit)
submit_button.grid(column=2,row=7)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5,pady=5)

root.mainloop()
