import requests
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def getfullsavefile(path:str = "fullsavefile.ini"):
    full_savefile = requests.get(
        "https://gist.githubusercontent.com/FexinShifter/821845203c24ad3d6d527471e5b4a9e7/raw/fcee0d0c84736a67031ee9664d48a41573225a4d/101%2525",
        stream=True)
    file = open(path, "wb")
    file.write(full_savefile.content)
    file.close()


def maintui():
    choice = input('To get 101% Pizza Tower Save File, type "101", or "exit" to quit. \n>>> ')

    if choice == "101":
        getfullsavefile()
    elif choice == "exit":
        print("Exiting...")
        exit(0)
    else:
        print(f'Invalid argument "{choice}"!')
        maintui()



def maingui():
    root = ttk.Window()

    btn_generate = ttk.Button(root, text="Generate 101% save file", bootstyle=PRIMARY)
    btn_generate.pack(side=LEFT, padx=5, pady=10)

    btn_exit = ttk.Button(root, text="Exit", bootstyle=(DANGER, OUTLINE))
    btn_exit.pack(side=LEFT, padx=5, pady=10)

    root.mainloop()

# Workaround that helps to use this script as a module.
if __name__ == '__main__':
    print('Welcome to PTSG')
    maingui()
