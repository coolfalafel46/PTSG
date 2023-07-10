import requests
import tkinter as tk
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import *
from ttkbootstrap.tooltip import ToolTip
from PIL import ImageTk, Image
import os

class gui(ttk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)
        self.create_gui()

    def create_gui(self):
        container=ttk.Frame(self,padding=10)
        container.pack(fill=X)
        # Define logo
        logoimg = ImageTk.PhotoImage(Image.open("Data/Images/Logo.png"))
        self.logo = ttk.Label(master=container, image=logoimg)
        self.logo.pack(side=TOP, fill=X, expand=YES, pady=10, padx=5,)
        # Define buttons
        self.buttons=[ttk.Label(master=container, image=logoimg),
                      ttk.Button(master=container,text="Get 101% Save File",bootstyle=PRIMARY, command=self.getfullsavefile),
                      ttk.Button(master=container,text="Exit",bootstyle="DANGER OUTLINE", command=self.onclick),
                      ]
        # Create buttons from array
        for button in self.buttons:
            button.pack(side=TOP, fill=X, expand=YES, pady=10, padx=5,)
        # Tooltips
        ToolTip(self.buttons[2], text="Exit the program without affecting your current save", bootstyle=LIGHT)
        ToolTip(self.buttons[1], text="Get the 101% save file for Pizza Tower.", bootstyle=LIGHT)

    def onclick(self):  # Quit function for button
        self.quit()
        print("App closed!")
        exit(0)

    def getfullsavefile(self, path: str = "fullsavefile.ini"):  # Function for downloading the full save file
        full_savefile = requests.get(
            "https://gist.githubusercontent.com/FexinShifter/821845203c24ad3d6d527471e5b4a9e7/raw/fcee0d0c84736a67031ee9664d48a41573225a4d/101%2525",
            stream=True)
        file = open(path, "wb")
        file.write(full_savefile.content)
        file.close()
        # Define toast that appears when the download is complete
        finish_toast = ToastNotification(
            title="Save file downloaded!",
            message="Check your script folder!",
            duration=3000,
            icon="✅",
            bootstyle="SUCCESS"
        )
        print("Save file downloaded!")
        finish_toast.show_toast()  # Show the toast


# Workaround that helps to use this script as a module.
if __name__ == '__main__':
    print('Welcome to PTSG')
    app = ttk.Window(
        title="Pizza Tower Save Generator",
        themename="superhero",
        # resizable=(False, False),
        minsize=(500, 400)
    )
    gui(app)
    app.mainloop()
