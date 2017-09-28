# test.py
import tkinter as tk  # for python 3
import pygubu
from tkinter import filedialog
import os
import subprocess
from os import system
import sys
import io
from tkinter import END, INSERT, DISABLED
#from tkinter.filedialog import askdirectory


class Application:
    def __init__(self, master):

        # 1: Create a builder
        self.builder = builder = pygubu.Builder()

        # 2: Load an ui file
        builder.add_from_file('FibreAnalysis.ui')

        # 3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('mainwindow', master)

        # get variables from gui elements
        self.volume_file = builder.get_variable("volume_file")
        self.working_directory = builder.get_variable("working_directory")
        self.sigma = builder.get_variable("sigma")
        self.alpha1 = builder.get_variable("alpha1")
        self.alpha2 = builder.get_variable("alpha2")
        self.low_thresh = builder.get_variable("low_thresh")
        self.up_thresh = builder.get_variable("up_thresh")
        self.output_dir = builder.get_variable("output_dir")
        self.use_config = builder.get_variable("use_config")
        self.config_file = builder.get_variable("config_file")

        # get GUI elements like scales
        self.title = builder.get_object("Title")
        self.scale_sigma = builder.get_object("scale_sigma")
        self.scale_low_thresh = builder.get_object("scale_low_thresh")
        self.scale_up_thresh = builder.get_object("scale_up_thresh")
        self.entry_alpha1 = builder.get_object("entry_alpha1")
        self.entry_alpha2 = builder.get_object("entry_alpha2")
        self.button_select_config = builder.get_object("button_select_config")
        self.button_run = builder.get_object("button_run")

        def set_default_values():
            '''
            sets all parameters to the default values
            '''

            self.config_file.set(" ")
            #self.use_config = False

            self.scale_sigma.set(4)
            self.scale_low_thresh.set(4.4)
            self.scale_up_thresh.set(255)

            self.entry_alpha1.delete(0, END)
            self.entry_alpha1.insert(0, "0.5")

            self.entry_alpha2.delete(0, END)
            self.entry_alpha2.insert(0, "2.0")

            self.volume_file.set(" ")
            self.checkVolumeFile = False

            self.working_directory.set(" ")
            self.checkWorkingDir = False

            self.output_dir.set(" ")
            self.checkOutputDir = False
            self.button_run.config(state=DISABLED)

        set_default_values()

        # initialize text for output log with scrollbar
        self.txt = tk.Text(borderwidth=3, relief="sunken", height=10, width=5)
        self.txt.config(font=("consolas", 10), undo=True, wrap='word')
        self.txt.grid(row=11, column=0, sticky="nsew",
                      padx=2, pady=2, columnspan=4)

        scrollb = tk.Scrollbar(command=self.txt.yview)
        scrollb.grid(row=11, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

        # font options
        self.title.config(font=("consolas", 18), height=2)

        '''
        #checks if output dir is set
        self.checkOutputDir = False
        self.checkWorkingDir = False
        self.checkVolumeFile = False'''

        def enable_Run():
            '''
            checks if necessary files are selected
            '''
            if (self.checkVolumeFile is True and self.checkWorkingDir is True):
                self.button_run.config(state='active')
            else:
                self.button_run.config(state=DISABLED)

        def select_volume_file():
            '''
            opens filedialog and select volume file
            '''

            # open file dialog to open header file
            tmp = filedialog.askopenfilename(
                initialdir="/home/lena/utans-filt/build",
                title="Volume Header File Select",
                filetypes=[("Volume Header", ".nhdr")])
            # update variable to display correct text in Entry
            self.volume_file.set(tmp)
            self.checkVolumeFile = True
            enable_Run()

        def select_working_dir():
            '''
            opens file dialog to select working directory
            '''
            # open file dialog to open header file
            tmp = filedialog.askdirectory()
            # update variable to display correct text in Entry
            self.working_directory.set(tmp)
            self.checkWorkingDir = True

            enable_Run()

        def select_config_file():
            '''
            opens file dialog to select optional configuration file 
            '''

            tmp = filedialog.askopenfilename(initialdir="/home/lena/utans-filt/build/",
                                             title="Configuration File Select",
                                             filetypes=[("Configuration files",".conf")])
            self.config_file.set(tmp)
            read_file()

        def select_output_directory():
            '''
            opens file dialog to select output directory
            '''
            # open file dialog to open header file
            tmp = filedialog.askdirectory()
            # update variable to display correct text in Entry
            self.output_dir.set(tmp)
            self.checkOutputDir = True

        def run_application():
            '''
            Runs the command with the variables from the UI
            checks if output directory is set
            checks upper and lower threshold values
            '''

            # optional output directory
            # if none selected, equivalent to working directory
            if(self.checkOutputDir == False):
                self.output_dir.set(self.working_directory.get())

            # check correct thresholds
            if(self.up_thresh.get() <= self.low_thresh.get()):
                self.txt.insert(
                    END, "ERROR: Lower threshold bigger than upper threshold")
            else:
                command = "cd %s && ./FibreSeparator %s --sigma %d  --alpha1 %s --alpha2 %s --lowthresh %d --upthresh %d" % (self.working_directory.get(
                ), self.volume_file.get(), self.scale_sigma.get(), self.entry_alpha1.get(), self.entry_alpha2.get(), self.scale_low_thresh.get(), self.scale_up_thresh.get())
                Outputfileobject = os.popen(command)
                Output = Outputfileobject.read()
                Outputfileobject.close()
                #self.txt.delete(0, END)
                self.txt.insert(END, Output)

        def check_config():
            '''
            if checkbox of config file is not set, button to select file is disabled
            '''

            if(self.use_config.get() is False):
                self.button_select_config.config(state="disabled")
                self.config_file.set(" ")
            else:
                self.button_select_config.config(state="active")

        def print_vars():
            '''
            testing method to print all variables
            '''
            print("volume File Path:", self.volume_file.get())

            print("working directory path:", self.working_directory.get())

            print("sigma:", self.scale_sigma.get())

            print("alpha1:", self.entry_alpha1.get())

            print("alpha2:", self.entry_alpha2.get())

            print("low_thresh:", self.scale_low_thresh.get())

            print("up_thresh:", self.scale_up_thresh.get())

            print("output_dir: ", self.output_dir.get())

        def read_file():
            '''
            method to read file and transform into dict
            set variables to values from file
            '''

            # open and read file
            file = open(self.config_file.get(), "r")
            lines = file.readlines()
            file.close()

            # array for the key-value pairs
            values = []
            # fill values by splitting lines and making it into a dict
            for line in lines:
                line = line.strip()
                values.append(line.split())
            values = dict(values)

            # set variables
            self.scale_sigma.set(values["sigma"])
            # delete previous content of entry before inserting new value
            self.entry_alpha1.delete(0, END)
            self.entry_alpha1.insert(0, values["diameter"])
            self.entry_alpha2.delete(0, END)
            self.entry_alpha2.insert(0, values["Materialconstant"])
            self.scale_low_thresh.set(values["lowerthreshold"])
            self.scale_up_thresh.set(values["upperthreshold"])

        self.callbacks = {
            'select_volume_file': select_volume_file,
            'select_working_dir': select_working_dir,
            'select_config_file': select_config_file,
            'select_output_directory': select_output_directory,
            'print_vars': print_vars,
            'run_application': run_application,
            'check_config': check_config,
            'read_file': read_file,
            'set_default_values': set_default_values,


        }

        builder.connect_callbacks(self.callbacks)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
