"""
This GUI is for any number of shortcuts and uses tkinter and pywin32 clipboard.
Copy, hit buttons, and paste to use, feel free to make your own copy and change things or add 
your own!
"""


import win32clipboard as clp
from tkinter import *


'''FUNCTION DECLARATIONS'''
def cammaListClp():
    clp.OpenClipboard()
    text = clp.GetClipboardData().strip()
    data = ",".join([str(i) for i in set(text.split())])
    clp.EmptyClipboard()
    clp.SetClipboardText(data)
    clp.CloseClipboard()

    
def tickClp():
    clp.OpenClipboard()
    data = clp.GetClipboardData().strip()
    data = "'" + "','".join([str(i) for i in set(data.split('\r\n'))]) + "'"
    clp.EmptyClipboard()
    clp.SetClipboardText(data)
    clp.CloseClipboard()

    
def tickcommaClp():
    clp.OpenClipboard()
    data = clp.GetClipboardData().strip()
    data = "'"+ "','".join([str(i.strip()) for i in set(data.split(","))]) + "'"
    clp.EmptyClipboard()
    clp.SetClipboardText(data)
    clp.CloseClipboard()

    
def barListClip():
    clp.OpenClipboard()
    text = clp.GetClipboardData().strip()
    data = "|".join([str(i) for i in set(text.split())])
    clp.EmptyClipboard()
    clp.SetClipboardText(data)
    clp.CloseClipboard()


def rmduplicatesClip():
    clp.OpenClipboard()
    data = clp.GetClipboardData().strip()
    data = "\n".join([str(i) for i in set(data.split())])
    clp.EmptyClipboard()
    clp.SetClipboardText(data)
    clp.CloseClipboard()

    
def setClipText():
    setClip("""Put saved phrase in here!""")

    
root = Tk()
root.title("Shortcuts")
root.attributes('-topmost', True)
root.update()
#root.minsize(200, 225)

width = 30
bg = '#95A8F4' 
relief = 'raised'

queryFrame = Frame(root, width=width, relief=relief, borderwidth=5, background=bg)
queryFrame.pack(fill=X)
otherFrame = Frame(root, width=width, relief=relief, borderwidth=5, background=bg)
otherFrame.pack(fill=X)


###########################################################################
# queryframe Labels and Buttons
queryLabel = Label(queryFrame, text="Short Cuts", fg="white", bg="black")
queryLabel.pack(fill=X)

commaButton = Button(queryFrame, text="Comma Separate a List", command=cammaListClp)
commaButton.pack(fill=X)

roundButton = Button(queryFrame, text='Tick Separate a List', command=tickClp)
roundButton.pack(fill=X)

roundButton = Button(queryFrame, text='Tick a Comma List', command=tickcommaClp)
roundButton.pack(fill=X)

barButton = Button(queryFrame, text="Bar Separate a List", command=barListClip)
barButton.pack(fill=X)


###########################################################################
# Divider
queryLabel = Label(otherFrame, width=width, text="Other Shortcuts", fg="white", bg="black")
queryLabel.pack(fill=X)

###########################################################################
# textFrame Labels and Buttons
rm_redundantButton = Button(otherFrame, text='Remove Duplicates', command=rmduplicatesClip)
rm_redundantButton.pack(fill=X)

questconcButton = Button(otherFrame, text="Paste Saved Phrase", command=setClipText)
questconcButton.pack(fill=X)

###########################################################################


root.mainloop()



