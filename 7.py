print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

import tkinter  
import random

colours = ['Red','Blue','Green','Pink','Black',  
           'Yellow','Orange','White','Purple','Brown']
score = 0
timeleft = 120
current_colour = ""
game_started = False
def startGame(event):
    global timeleft, game_started
    if not game_started:
        game_started = True
        countdown()
        nextColour()
    else:
        nextColour()

def nextColour():
    global score  
    global timeleft
    global current_colour, game_started
    if timeleft > 0:
        e.focus_set()
        S = e.get().lower()
        if current_colour != "":
            if S == current_colour.lower():
                score += 2
            else:
                score += 1
                if score < 0:
                    score = 0
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg = colours[1], text = colours[0])
        current_colour = colours[1]
        scoreLabel.config(text ="Score:" + str(score))
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)
root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x200")
instructions = tkinter.Label(root, text = "Type in the colour" 
                                          " of the words, and not the word text!",
                             font =  ('Helvetica', 12))
instructions.pack()  
scoreLabel = tkinter.Label(root, text = "Press enter to start",  
                           font = ('Helvetica', 12))  
scoreLabel.pack()
timeLabel = tkinter.Label(root, text = "Time left: " + str(timeleft),
                          font = ('Helvetica', 12))  
timeLabel.pack()
label = tkinter.Label(root, font = ('Helvetica', 60))  
label.pack()

e = tkinter.Entry(root)
root.bind('<Return>', startGame)  
e.pack()
e.focus_set()
root.mainloop()
 
 
 
 
 

