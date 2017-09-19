# test.py
import tkinter as tk  # for python 3
import pygubu
from tkinter import filedialog
#from tkinter.filedialog import askdirectory


class Application:
    def __init__(self, master):

        # 1: Create a builder
        self.builder = builder = pygubu.Builder()

        # 2: Load an ui file
        builder.add_from_file('FibreAnalysis.ui')

        # 3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('mainwindow', master)

        #get variables from gui elements
        volume_file = builder.get_variable("volume_file")
        working_directory = builder.get_variable("working_directory")
        sigma = builder.get_variable("sigma")
        alpha1 = builder.get_variable("alpha1")
        alpha2 = builder.get_variable("alpha2")
        low_thresh = builder.get_variable("low_thresh")
        up_thresh = builder.get_variable("up_thresh")
        config_file = builder.get_variable("config_file")
        output_dir = builder.get_variable("output_dir")

        #get GUI elements like scales
        scale_sigma = builder.get_object("scale_sigma")

        '''
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
        '''

        def select_volume_file():
            ''' 
            opens filedialog and select volume file 
            '''

            #open file dialog to open header file
            tmp = filedialog.askopenfilename(
                  initialdir="/home/lena/Downloads", title="Volume Header File Select", filetypes=[("JPG files", ".jpg")])
            #update variable to display correct text in Entry
            volume_file.set(tmp)
        
        def select_working_dir():
            '''
            opens file dialog to select working directory
            '''
            #open file dialog to open header file
            tmp = filedialog.askdirectory()
            #update variable to display correct text in Entry
            working_directory.set(tmp)

        def set_sigma(self):
            sigma = scale_sigma.get() 
            if (sigma == 0.0):
                sigma = 0.001  

        self.callbacks = {
              #'self' : self,
            'select_volume_file' : select_volume_file,
            'select_working_dir' : select_working_dir,
            'set_sigma' : set_sigma   
        }
        builder.connect_callbacks(self.callbacks)
            
           



if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
