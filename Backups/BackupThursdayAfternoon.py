# test.py
import tkinter as tk  # for python 3
import pygubu
from tkinter import filedialog


class Application:
    def __init__(self, master):

        # 1: Create a builder
        self.builder = builder = pygubu.Builder()

        # 2: Load an ui file
        builder.add_from_file('FibreAnalysis.ui')

        # 3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('mainwindow', master)
       

        self.shared_data = {
            "vol_file" : 1,
            "working_dir" : "select working directory",
            "sigma" : 2,
            "alpha1" : 1,
            "alpha2" : 0.5,
            "low_thresh" : 0,
            "up_thresh" : 255,
            "config_file" : "select config file",
            "output_dir" : "select output directory"
        }

        def select_volume_file():
            v_file = filedialog.askopenfilename(
                  initialdir="/home/lena/Downloads", title="Volume Header File Select", filetypes=[("JPG files", ".jpg")]) 
            self.shared_data["vol_file"] = v_file
            #print(self.shared_data["vol_file"])


        self.callbacks = {
              #'self' : self,
            'select_volume_file' : select_volume_file
        }
        builder.connect_callbacks(self.callbacks)
            
           



if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
