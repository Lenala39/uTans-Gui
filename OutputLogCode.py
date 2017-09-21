self.txt = tk.Text( borderwidth=3, relief="sunken", height=10, width=5)
self.txt.config(font=("consolas", 12), undo=True, wrap='word')
self.txt.grid(row=11, column=0, sticky="nsew", padx=2, pady=2, columnspan=3)

scrollb = tk.Scrollbar(command=self.txt.yview)
scrollb.grid(row=12, column=1, sticky='nsew')
self.txt['yscrollcommand'] = scrollb.set

def print_log():
    command = "cd /home/lena/utans-filt/build && ./FibreSeparator"
    Outputfileobject=os.popen(command)
    Output=Outputfileobject.read()
    Outputfileobject.close()
    #self.log_frame["text"] = Output
    #self.log_label.config(text=Output, justify='left', anchor='ne', pady=10, wraplength=390)
