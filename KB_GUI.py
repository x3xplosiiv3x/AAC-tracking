from tkinter import *

window=Tk()
window.attributes('-alpha',1)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{screen_width}x{screen_height}+-8+0')

p = open("Phrases.txt" ,"r")
read_phrases = p.read()
phrase_list = read_phrases.splitlines()
p.close()

# add widgets here



def select(value):
    entry.insert(END,value)

def delete():
    entry.delete('1.0', 'end')


window.title('AAC')


varRow = 2
varColumn = 0


entry = Text(window, width = 170, font = ('arial', 12))
entry.grid(row=1, columnspan=40, sticky='w')

for phrases in phrase_list:
    command = lambda x= phrases: select(x)
    
    
    if phrases == 'DELETE':
        Button(window, text=phrases, background='Red', width=21, padx=2, pady=2, bd=8, font=('arial', 15), command = delete).grid(row=varRow, column = varColumn)
    if phrases != 'DELETE' and phrases[0]!= '#':
        Button(window, text=phrases, width=21, padx=2, pady=2, bd=8, font=('arial', 15), command = command).grid(row=varRow, column = varColumn)
    varColumn += 1
    if phrases[0] == '#':
        varColumn -= 1
    
    if varColumn > 5 and varRow ==2:
        varColumn = 0
        varRow+=1
    if varColumn > 5 and varRow ==3:
        varColumn = 0
        varRow+=1
        



window.mainloop()

