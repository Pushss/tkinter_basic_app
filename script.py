from tkinter import * #import all from tkinter libary. allows use of Button() instead of tkinter.Button()

window=Tk() #create window

def km_to_miles():
    miles = float(e1_value.get()) * 1.6 #convert e1_value to float multiply by 1.6
    t1.insert(END,miles) #insert something in to t1 ,param's where to put text, e1_value variable wanting to insert

b1=Button(window, text="Execute",command=km_to_miles) #create button (places in window, text="String",command=call's function without ())
b1.grid(row=0,column=0) #places the button on the window can define postion with .grid(grid can have row=0, column=0 for easier placement, rowspan=number of grid row the button will span) or .pack

e1_value=StringVar() #declare string variable to store Entry() data
e1=Entry(window, textvariable=e1_value) #entry widget (editText)(textvariable = e1_value)
e1.grid(row=0,column=1) #postions entry widget on grid

t1=Text(window,height=1,width=20) #text widget(textView)
t1.grid(row=0,column=2) #postions text widget on grid

window.mainloop() #allows window to remain open permentaly keep this at end of code
