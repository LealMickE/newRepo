import tkinter as tk
import tkinter.font as tkFont

#create tkinter object
app = tk.Tk()
#set app title
app.winfo_toplevel().title("Project")
# set object's size
app.geometry("640x480")

#create font style to use in app
fontStyle = tkFont.Font(family="Lucida Grande", size=30)

# create a label
labelExample = tk.Label(app, text="The system is idle", font=fontStyle)

# create a virtual image to be used for sizing the buttons in pixels insted of text units
pixelVirtual = tk.PhotoImage(width=1, height=1)

def bgOn():
    #change lable text
    labelExample.config(text = "System Running.")

def bgOff():
    #change lable text
    labelExample.config(text = "System Off.")


#put the lable in the app using pack example (TOP, BOTTOM, LEFT, RIGHT)
labelExample.pack(side=tk.TOP)

buttonOn = tk.Button(app,text = "System On", image=pixelVirtual,width=200, height=100, compound="c", command = bgOn)
buttonOn.place(x=100, y=400)

buttonOff = tk.Button(app, text="System Off", image=pixelVirtual,width=200, height=100, compound="c", command = bgOff)
buttonOff.place(x=340, y=400)

#minimal exit button and pack example (TOP,BUTTOM, LEFT, RIGHT)
buttonExit = tk.Button(app, text="EXIT", command = app.quit)
buttonExit.pack(side=tk.TOP)

app.mainloop()