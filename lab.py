import tkinter as tk
from tkinter import ttk

def submit():
    result = "Your submission was successful!"
    return result

def on_submit():
    global result_variable
    result_variable = submit()

root = tk.Tk()
root.title("Submit and Fetch Example")

mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

submit_button = ttk.Button(mainframe, text='Submit', command=on_submit)
submit_button.grid(column=1, row=2, sticky=tk.W)

result_variable = tk.StringVar()
result_label = ttk.Label(mainframe, textvariable=result_variable)
result_label.grid(column=1, row=3, columnspan=2)

root.mainloop()

# After the mainloop has finished, you can print the result_variable value
print(result_variable.get())
