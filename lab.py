import tkinter as tk
import subprocess

def run_script():
    subprocess.run(['python', 'toolbox.py'])

root = tk.Tk()
root.title('Run Script')

run_button = tk.Button(root, text='Run Script', command=run_script)
run_button.pack()

root.mainloop()
