from tkinter import * #import all from tkinter libary. allows use of Button() instead of tkinter.Button()

window=Tk() #create window

def conversion(): #function used to for onClick on button command=
    value = e1_value.get() #value from value(editText) need to use .get()
    grams= float(value) * 1000 #convert value to float multiply
    pounds=float(value) * 2.20462
    ounces=float(value) * 35.274
    t1.insert(END,grams) #insert something in to t1 ,param's where to put text, e1_value variable wanting to insert
    t2.insert(END,pounds) #insert something in to t2 ,param's where to put text, e1_value variable wanting to insert
    t3.insert(END,ounces) #insert something in to t3 ,param's where to put text, e1_value variable wanting to insert

l1=Label(window, text="Kg:") #Label (call to window, display text "Kg:")
l1.grid(row=0,column=0) #postions Label widget on grid

e1_value=StringVar() #declare string variable to store Entry() data
e1=Entry(window, textvariable=e1_value) #entry widget (editText)(textvariable = e1_value)
e1.grid(row=0,column=1) #postions entry widget on grid

b1=Button(window, text="Convert",command=conversion) #create button (places in window, text="String",command=call's function without ())
b1.grid(row=0,column=2) #places the button on the window can define postion with .grid(grid can have row=0, column=0 for easier placement, rowspan=number of grid row the button will span) or .pack

t1=Text(window,height=1,width=20) #text widget(textView)
t1.grid(row=1,column=0) #postions text widget on grid

t2=Text(window,height=1,width=20) #text widget(textView)
t2.grid(row=1,column=1) #postions text widget on grid

t3=Text(window,height=1,width=20) #text widget(textView)
t3.grid(row=1,column=2) #postions text widget on grid

window.mainloop() #allows window to remain open permentaly keep this at end of code
