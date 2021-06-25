from tkinter import *

window=Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{screen_width}x{screen_height}+-8+0')


# add widgets here



def select(value):
    entry.insert(END,value)

window["bg"]="Blue"
window.title('AAC')

buttons = ["This is a test ", "I am testing you ", "Of course this is anther test ",'but is this another test ', 'and yet anotehr one', 'and so on and so forth bc']
varRow = 2
varColumn = 0

entry = Text(window, width = 100, font = ('arial', 12))
entry.grid(row=1, columnspan=40)

for button in buttons:
    command = lambda x= button: select(x)
    
    Button(window, text=button, padx=2, pady=2, bd=8, font=('arial', 15), command = command).grid(row=varRow, column = varColumn)
    varColumn += 1
    if varColumn > 1 and varRow ==3:
        varColumn = 0
        varRow+=1
    if varColumn > 1 and varRow ==4:
        varColumn=0
        varRow+=1



window.mainloop()

