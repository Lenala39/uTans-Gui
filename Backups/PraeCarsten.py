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


        label_alpha1 = builder.get_variable("label_alpha1")
        

        #get GUI elements like scales
        scale_sigma = builder.get_object("scale_sigma")
        scale_low_thresh = builder.get_object("scale_low_thresh")
        scale_up_thresh = builder.get_object("scale_up_thresh")
        entry_alpha1 = builder.get_object("entry_alpha1")

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

        def set_alpha1():
            tmp = entry_alpha1.get()
            alpha1 = tmp
            print(alpha1)
            

           
        
        def select_working_dir():
            '''
            opens file dialog to select working directory
            '''
            #open file dialog to open header file
            tmp = filedialog.askdirectory()
            #update variable to display correct text in Entry
            working_directory.set(tmp)

       
        def set_sigma(self):
            '''
            updates the variable sigma with the current slider value
            open interval at 0 for sigma, so 0 made into 0.001
            '''
            sigma = scale_sigma.get()
            #print(sigma) 
            if (sigma == 0.0):
                sigma = 0.001

        def set_low_thresh(self):
            '''
            updates the variable low_thresh with current slider value
            '''
            low_thresh = scale_low_thresh.get()
        
        def set_up_thresh(self):
            '''
            updates the variable up_thresh with current slider value
            '''
            up_thresh = scale_up_thresh.get()
            

        def select_config_file():
            '''
            opens file dialog to select optional configuration file 
            '''
            tmp = filedialog.askopenfilename(initialdir="/home/lena/Downloads", title="Configuration File Select", filetypes=[("JPG files", ".jpg")])
            config_file.set(tmp)

        def select_output_directory():
            '''
            opens file dialog to select output directory
            '''
            #open file dialog to open header file
            tmp = filedialog.askdirectory()
            #update variable to display correct text in Entry
            output_dir.set(tmp)


        self.callbacks = {
            'select_volume_file' : select_volume_file,
            'select_working_dir' : select_working_dir,
            'set_sigma' : set_sigma,
            'set_low_thresh': set_low_thresh,
            'set_up_thresh' : set_up_thresh,
            'select_config_file' : select_config_file,
            'select_output_directory' : select_output_directory
            #'set_alpha1' : set_alpha1            
        }

        builder.connect_callbacks(self.callbacks)
            
           



if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
