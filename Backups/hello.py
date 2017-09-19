from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import tkinter as tk

'''
#from tkinter.filedialog import askopenfilename

#necessary init
root = Tk()
root.title("uTANS-Filt")

#setup of main window
mainframe = Frame()
mainframe.pack()

volume_input_frame = Frame(mainframe)
volume_input_frame.pack()
volume_header_label = Label(volume_input_frame, text="Volume Header")

volume_header_file = filedialog.askopenfilename(initialdir = "/",title = "Select file", filetypes = ((("jpeg files","*.jpg")))

root.mainloop()

'''


class Application(tk.Frame):
    # initialize Application
    def __init__(self, master):
        # super().__init__(master)
        #self.grid(rowspan=3, columnspan=3)
        #self.geometry('{}x{}'.format(460, 350))
        #self.grid_configure(rowspan=10, columnspan=2, sticky="nsew")
        #self.label.grid(row=0, column=1, sticky="nsew")
        #self.grid_rowconfigure(0, weight=1)
        #self.grid_columnconfigure(0, weight=1)
        self.create_widgets()

    # create all widgets
    def create_widgets(self):
        # Label for volume header file
        self.v_file_label = Label()
        self.v_file_label["text"] = "Volume File Header"
        self.v_file_label.grid(row=0, column=0, padx=100, pady=20)

        # Button to open file dialog
        self.v_file_select = Button(self)
        self.v_file_select['text'] = "..."
        self.v_file_select['command'] = self.select_file
        self.v_file_select.grid(row=0, column=1, padx=100, pady=20)

        # Label for selecting working dir
        self.working_dir_label = Label()
        self.working_dir_label["text"] = "Working directory"
        self.working_dir_label.grid(row=1, column=0, padx=100, pady=20)

        # Button to open directory dialog
        self.working_dir_select = Button(self)
        self.working_dir_select['text'] = "..."
        self.working_dir_select['command'] = self.select_dir
        self.working_dir_select.grid(row=1, column=1, padx=100, pady=20)

    # action to select file
    def select_file(self):
        self.v_file = filedialog.askopenfilename(
            initialdir="/home/", title="Volume Header File Select", filetypes=[("Newly raw raster data header", ".ndhr")])

    # action to select directory
    def select_dir(self):
        self.working_dir = filedialog.askdirectory()


root = Tk()
app = Application(master=root)
app.mainloop()
