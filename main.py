from tkinter import *
from functools import partial


player = 0
playing_field_machine = []
button_list = []


def checkForWin(i, j, win_label):
    global playing_field_machine
    global player
    global button_list

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

        for dir2 in dir:
            x , y = dir2
            i , j = defaultCords

            while playing_field_machine[i][j] == player:
                count += 1
                i += y
                j += x
                # IndexError prevention
                if i >= size_v or j >= size_h:
                    break
                if count > 5:
                    win_label.config(text = f"Player {player} wins!!!")
                    
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


def changeButtonText(button):
    global player
    if player == 0:
        text = "O"
    else:
        text = "X"
    button.config(text=text, command=None)

def _generateBottomLevel(x, y, button_list, playing_field, winLabel):
    global playing_field_machine
    for i in range(x):
        playing_field_machine.append([])
        button_list.append([])
        for j in range(y):
            playing_field_machine[i].append(-1)

            button_list[i].append(Button(playing_field, command=partial(updatePlayingField, i, j, button_list, winLabel), width=1))
            button_list[i][j].grid(column=i, row=j)

def generateTopLevel(entry1, entry2, info_frame, errorLabel):
    isNotError = True
    try:
        h_size = int(entry1.get())
        v_size = int(entry2.get())
        if h_size < 0 or v_size < 0:
            isNotError = False
    except ValueError:
        isNotError = False
    if isNotError:
        # Reusing errorLabel as victory anouncer
        _generateBottomLevel(h_size, v_size, button_list, playing_field, errorLabel)
        info_frame.destroy()
    else:
        errorLabel.config(text="Please enter a positive number")


root = Tk()

# Declares root part
error_label = Label(root)
info_frame = Frame(root)
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