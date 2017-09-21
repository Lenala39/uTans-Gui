# test.py
import tkinter as tk  # for python 3
import pygubu
from tkinter import filedialog
from tkinter import scrolledtext
import os 
import subprocess 
from os import system 
import sys 
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
        self.volume_file = builder.get_variable("volume_file")
        self.working_directory = builder.get_variable("working_directory")
        self.sigma = builder.get_variable("sigma")
        self.alpha1 = builder.get_variable("alpha1")
        self.alpha2 = builder.get_variable("alpha2")
        self.low_thresh = builder.get_variable("low_thresh")
        self.up_thresh = builder.get_variable("up_thresh")
        self.output_dir = builder.get_variable("output_dir")
        

        #get GUI elements like scales
        self.scale_sigma = builder.get_object("scale_sigma")
        self.scale_sigma.set(4)
        self.scale_low_thresh = builder.get_object("scale_low_thresh")
        self.scale_low_thresh.set(4.4)
        self.scale_up_thresh = builder.get_object("scale_up_thresh")
        self.scale_up_thresh.set(255)
        self.entry_alpha1 = builder.get_object("entry_alpha1")
        self.entry_alpha1.insert(0, "0.5")
        self.entry_alpha2 = builder.get_object("entry_alpha2")
        self.entry_alpha2.insert(0, "2.0")


       

        #checks if output dir is set
        self.checkOutputDir = False


        def select_volume_file():
            ''' 
            opens filedialog and select volume file 
            '''

            #open file dialog to open header file
            tmp = filedialog.askopenfilename(
                  initialdir="/home/lena/Downloads", title="Volume Header File Select", filetypes=[("Volume Header", ".nhdr")])
            #update variable to display correct text in Entry
            self.volume_file.set(tmp)

           
        
        def select_working_dir():
            '''
            opens file dialog to select working directory
            '''
            #open file dialog to open header file
            tmp = filedialog.askdirectory()
            #update variable to display correct text in Entry
            self.working_directory.set(tmp)

        def select_config_file():
            '''
            opens file dialog to select optional configuration file 
            '''
            tmp = filedialog.askopenfilename(initialdir="/home/lena/Downloads", title="Configuration File Select", filetypes=[("JPG files", ".jpg")])
            self.config_file.set(tmp)

        def select_output_directory():
            '''
            opens file dialog to select output directory
            '''
            #open file dialog to open header file
            tmp = filedialog.askdirectory()
            #update variable to display correct text in Entry
            self.output_dir.set(tmp)
            self.checkOutputDir = True


        def run_application():
            print("hello")
            
            #optional output directory
            #if none selected, equivalent to working directory
            if(self.checkOutputDir == False):
                self.output_dir.set(self.working_directory.get())

            #check correct thresholds
            if(self.up_thresh.get() <= self.low_thresh.get()):
                print("error")
            else:                
                command = "cd %s && ./FibreSeparator %s --sigma %d  --alpha1 %s --alpha2 %s --lowthresh %d --upthresh %d" % (self.working_directory.get(), self.volume_file.get(), self.scale_sigma.get(), self.entry_alpha1.get(), self.entry_alpha2.get(), self.scale_low_thresh.get(), self.scale_up_thresh.get())
                print(command)
                system(command)
                
            

        def print_vars():
            print("volume File Path:", self.volume_file.get()) 
            
            print("working directory path:", self.working_directory.get()) 

            print("sigma:", self.scale_sigma.get())

            print("alpha1:", self.entry_alpha1.get())

            print("alpha2:", self.entry_alpha2.get())

            print("low_thresh:", self.scale_low_thresh.get())

            print("up_thresh:", self.scale_up_thresh.get())

            print("output_dir: ", self.output_dir.get())

        self.callbacks = {
            'select_volume_file' : select_volume_file,
            'select_working_dir' : select_working_dir,
            'select_config_file' : select_config_file,
            'select_output_directory' : select_output_directory,
            'print_vars' : print_vars,
            'run_application' : run_application, 
            
        }

        builder.connect_callbacks(self.callbacks)
            
           



if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

