from tkinter import *
from tkmacosx import *
#Defining Space for creating game:-
root = Tk()
root.geometry("500x500")
root.title("Tic-Tac-Toe Game")

#Frame 1 is for creating title:-
frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1,text="Tic Tac Toe",font=("Timesnewroman",30),bg="black")
titleLabel.pack()

#Frame 2 is for creating TIC-TAC-TOE BOARD:-
frame2 = Frame(root)
frame2.pack()

turn = 1

#Creating Function to Assign Box:
def play(event):
    global turn
    button= event.widget
    if turn==1:
        button["text"] = 'X'
        turn=0
    else:
        button["text"] = 'O'
        turn=1

##Creating First Row:-
button1 = Button(frame2,text="",width=4,height=2,font=("Timesnewroman",35),bg = 'red',highlightbackground='red',relief=RAISED)
button1.grid(row=0,column=0)
button1.bind("<Button-1>",play)

button1 = Button(frame2,text="",font=("Timesnewroman",35),width=4,height=2,bg='red')
button1.grid(row=0,column=1)
button1.bind("<Button-1>",play)

button1 = Button(frame2,text="",font=("Timesnewroman",35),width=4,height=2,bg='red')
button1.grid(row=0,column=2)
button1.bind("<Button-1>",play)

##Creating Second Row:-
button1 = Button(frame2,text="",font=("Timesnewroman",35),width=4,height=2,bg='red')
button1.grid(row=1,column=0)
button1.bind("<Button-1>",play)

button1 = Button(frame2,text="",font=("Timesnewroman",35),width=4,height=2,bg='red')
button1.grid(row=1,column=1)
button1.bind("<Button-1>",play)

button1 = Button(frame2,text="",font=("Timesnewroman",35),width=4,height=2,bg='red')
button1.grid(row=1,column=2)
button1.bind("<Button-1>",play)

##Creating Third Row:-
button1 = Button(frame2,text="",font=("Timesnewroman",35),width=4,height=2,bg='red')
button1.grid(row=2,column=0)
button1.bind("<Button-1>",play)

button1 = Button(frame2,text="",font=("Timesnewroman",35),width=4,height=2,bg='red')
button1.grid(row=2,column=1)
button1.bind("<Button-1>",play)

button1 = Button(frame2,text="",font=("Timesnewroman",35),width=4,height=2,bg='red')
button1.grid(row=2,column=2)
button1.bind("<Button-1>",play)



root.mainloop()