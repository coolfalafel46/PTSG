import requests
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
class gui(ttk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)
        self.create_gui()
    def create_gui(self):
        container=ttk.Frame(self,padding=10)
        container.pack(fill=X)
        self.buttons=[ttk.Button(master=container,text="Get 101% Save File",bootstyle=PRIMARY, command=self.getfullsavefile),
                      ttk.Button(master=container,text="Exit",bootstyle="DANGER OUTLINE", command=self.onclick),
                      ]
        for button in self.buttons:
            button.pack(side=LEFT, fill=X, expand=YES, pady=10, padx=5)
    def onclick(self):
        self.quit()

    def getfullsavefile(self, path: str = "fullsavefile.ini"):
        full_savefile = requests.get(
            "https://gist.githubusercontent.com/FexinShifter/821845203c24ad3d6d527471e5b4a9e7/raw/fcee0d0c84736a67031ee9664d48a41573225a4d/101%2525",
            stream=True)
        file = open(path, "wb")
        file.write(full_savefile.content)
        file.close()

# Workaround that helps to use this script as a module.
if __name__ == '__main__':
    print('Welcome to PTSG')
    app = ttk.Window(
        title="Pizza Tower Save Generator",
        themename="superhero",
        resizable=(False, False)
    )
    gui(app)
    app.mainloop()
