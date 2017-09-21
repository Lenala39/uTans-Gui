import os
from Tkinter import *
Outputfileobject=os.popen("./FibreSeperator")
Output=Outputfileobject.read()
Outputfileobject.close()
root=Tk()
root.title("Output text")
Text=Label(root,text=Output).pack()
root.mainloop()