import tkinter
from random import choice
who = ('Sasha' , 'Nastya' , 'Arina', 'Leo', 'Alina', 'Eva', 'Dasha', 'Tim')
def click():
    whooseturn= choice(who)
    visual.configure(text= whooseturn)
    




root=tkinter.Tk()
root.geometry('400x400')
root.title('Whoose turn?')
root['bg'] = 'midnight blue'
btn = tkinter.Button(root, text='Click on me', font=('SimSun'), bg=('white'), command=click)
btn.place(width=200, height=50 , x = 100, y=170)
visual = tkinter.Label(root, text= 'Click on the button', font=('SimSun', 20), bg= 'midnight blue', fg= 'white', justify='center')
visual.place(width=300, height= 50, x=50, y=50)








root.mainloop()

