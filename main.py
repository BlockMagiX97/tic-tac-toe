# Made by BlockMagiX97
# Github account https://github.com/BlockMagiX97

from tkinter import *
from functools import partial
import os, sys

player = 0
playing_field_machine = []
button_list = []
resetButton = Button

def resetPlayingField(frame, i, j, button_list, winLabel):
    global playing_field_machine
    global resetButton
    global player

    player = 0
    playing_field_machine = []
    for x in button_list:
        for button in x:
            button.destroy()
    button_list.clear()
    winLabel.config(text="")
    resetButton.destroy()
    resetButton = Button
    _generateBottomLevel(i, j, button_list, frame, winLabel)

def checkForWin(i, j, win_label):
    global playing_field_machine
    global player
    global button_list
    global resetButton

    # Adds relative cordinations
    directions = (
        ((-1, -1), (1, 1)),
        ((1, -1), (-1, 1)),
        ((1, 0), (-1, 0)),
        ((0, 1), (0, -1))
           )

    size_v = len(playing_field_machine)
    size_h = len(playing_field_machine[0])

    defaultCords = (i , j)

    for dir in directions:
        count = 0
        cells = []

        for dir2 in dir:
            x , y = dir2
            i , j = defaultCords
            try:
                while playing_field_machine[i][j] == player:
                    count += 1
                    cells.append((i, j))
                    i += y
                    j += x
                    # Winning code
                    if count > 5:
                        if player == 0:
                            msg = "O"
                        else:
                            msg = "X"
                        win_label.config(text = f"Player {player + 1}  wins!!! Player {player + 1} is {msg}.")
                        
                        # Removes ability to change buttons 
                        for x in range(len(playing_field_machine)):
                            for y in range(len(playing_field_machine[0])):
                                if playing_field_machine[x][y] == -1:
                                    playing_field_machine[x][y] = None
                        playing_field = button_list[x][y].master
                        root = playing_field.master
                        
                        resetButton = Button(root, text="RESET", command=partial(resetPlayingField, playing_field, size_v, size_h, button_list, win_label))
                        resetButton.pack()
                        # Highlights the winning place
                        for x in cells:
                            y_cor, x_cor = x
                            button_list[y_cor][x_cor].config(bg='red')
                        
            except IndexError:
                pass


                    
def updatePlayingField(i, j, button_list, win):
    global player
    global playing_field_machine
    # Checks if clicked button is empty
    if playing_field_machine[i][j] == -1:
        playing_field_machine[i][j] = player
        changeButtonText(button_list[i][j])
        checkForWin(i, j, win)
        # Changes a player
        player = (player + 1) % 2


def changeButtonText(button, empty=False):
    global player
    if player == 0:
        text = "O"
    else:
        text = "X"
    if empty and not button.cget('text'):
        text = " "
    button.config(text=text, command=None)

def _generateBottomLevel(x, y, button_list, playing_field, winLabel):
    global playing_field_machine
    for i in range(x):
        playing_field_machine.append([])
        button_list.append([])
        for j in range(y):
            playing_field_machine[i].append(-1)
            button = Button(playing_field, command=partial(updatePlayingField, i, j, button_list, winLabel), width=1)
            button_list[i].append(button)
            button_list[i][j].grid(column=i, row=j)

def generateTopLevel(entry1, entry2, info_frame, errorLabel):
    isNotError = True
    try:
        h_size = int(entry1.get())
        v_size = int(entry2.get())
        if h_size <= 0 or v_size <= 0:
            isNotError = False
    except ValueError:
        isNotError = False
    if isNotError:
        # Reusing errorLabel as victory anouncer
        error_label.config(text="")
        _generateBottomLevel(h_size, v_size, button_list, playing_field, errorLabel)
        info_frame.destroy()
    else:
        errorLabel.config(text="Please enter a positive number")


root = Tk()

root.title('Tic-Tac-Toe')
# Sets icon
if "nt" == os.name:
    program_directory=sys.path[0]
    root.wm_iconbitmap(bitmap = os.path.join(program_directory, "icon.ico"))
else:
    program_directory=sys.path[0]
    root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "icon.png")))

# Declares root part
error_label = Label(root)
info_frame = Frame(root)
resetButton = Button(root)
playing_field = Frame(root)


# Makes config screen
wightEntry = Entry(info_frame)
wightEntry.insert(0, "Insert wight")
wightEntry.grid(row=0, column=0)

heightEntry = Entry(info_frame)
heightEntry.insert(0, "Insert height")
heightEntry.grid(column=1, row=0)

generateButton = Button(info_frame, text="GENERATE", command=partial(generateTopLevel, wightEntry, heightEntry, info_frame, error_label))
generateButton.grid(row=0, column=2)


# Packs in the root part
info_frame.pack()
playing_field.pack()
error_label.pack()


root.mainloop()