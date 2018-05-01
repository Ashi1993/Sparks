import nltk
import tkinter
from tkinter import messagebox
from tkinter import *
from evaluateDoc import termfreq

top = tkinter.Tk()
top.title('Hello, Tkinter!')
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
    for term, docs in termfreq:
        if term == input:
            documents = docs
        else:
            documents= "No results found"
    msg = messagebox.showinfo("Hello Python", documents)

B = Button(top, text = "Hello", command = helloCallBack, height = 2, width= 10)
B.pack(side=BOTTOM)
top.mainloop()
