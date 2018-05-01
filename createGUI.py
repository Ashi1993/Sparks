import nltk
import tkinter
from tkinter import messagebox
from tkinter import *
from evaluateDoc import termfreq

top = tkinter.Tk()
top.title('SPARKS')
top.geometry('400x400') # Size 200, 200

# labelframe = LabelFrame(top, height= 3)
# labelframe.pack(fill="both", expand="yes")

var = StringVar()
label = Label(top, textvariable=var, relief=RAISED, height=2)

var.set("SPARKS - Old History Book Library")
label.pack()

description = "Access to the most old history books."+"\n"+"Search any book you want just in one tap"
text = Text(top, height=4)
text.insert(INSERT, description)
text.pack()

input = StringVar()
L1 = Label(top, text = "Search", width= 8)
L1.pack( side = LEFT)
E1 = Entry(top, bd = 5, textvariable = input, width=32)
E1.pack(side = RIGHT)

def helloCallBack():
    input = E1.get()

    result = ""
    if input in termfreq.keys():
        docs = termfreq[input]
        for doc in docs:
            result = result + "\n" + doc
    else:
        result = "No Results Found"

    msg = messagebox.showinfo("Result", result)

B = Button(top, text = "Search", command = helloCallBack, height = 2, width= 10)
B.pack(side=BOTTOM)
top.mainloop()
