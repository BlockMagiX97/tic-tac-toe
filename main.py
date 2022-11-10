from tkinter import *
from functools import partial

# Declaring global variebles
player = 0
playing_field_machine = []
button_list = []

    # Logical part
def check_win(i, j, win_label):
    global playing_field_machine
    global player
    global button_list
    directions = (
        ((-1, -1), (1, 1)),
        ((1, -1), (-1, 1)),
        ((1, 0), (-1, 0)),
        ((0, 1), (0, -1))
           )
    size_v = len(playing_field_machine)
    size_h = len(playing_field_machine[0])
    def_dirs = (i , j)

    for dir in directions:
        count = 0
        for dir2 in dir:
            x , y = dir2
            i , j = def_dirs

            while playing_field_machine[i][j] == player:
                count += 1
                i += y
                j += x
                if i >= size_v or j >= size_h:
                    break
                if count > 5:
                    win_label.config(text = f"Player {player} wins!!!")
                    
                
# Updates playing field
def update(i, j, button_list, win):
    global player
    global playing_field_machine
    if playing_field_machine[i][j] == -1:
        playing_field_machine[i][j] = player
        player_move(button_list[i][j])
        check_win(i, j, win)
        player = (player + 1) % 2


def player_move(button):
    global player
    if player == 0:
        text = "O"
    else:
        text = "X"
    button.config(text=text, command=None)

# Generates a playing field
def _generate(x, y, button_list, playing_field, win):
    global playing_field_machine
    for i in range(x):
        playing_field_machine.append([])
        button_list.append([])
        for j in range(y):
            playing_field_machine[i].append(-1)

            button_list[i].append(Button(playing_field, command=partial(update, i, j, button_list, win), width=1))
            button_list[i][j].grid(column=i, row=j)

# Generates varieble length playing field
def generate(entry1, entry2, info_frame, error):
    isNotError = True
    try:
        h_size = int(entry1.get())
        v_size = int(entry2.get())
        if h_size < 0 or v_size < 0:
            isNotError = False
    except ValueError:
        isNotError = False
    if isNotError:
        _generate(h_size, v_size, button_list, playing_field, error)
        info_frame.destroy()
    else:
        error.config(text="Please enter a positive number")

    # Graphical part 
root = Tk()

# Makes root part
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

generateButton = Button(info_frame, text="GENERATE", command=partial(generate, wightEntry, heightEntry, info_frame, error_label))
generateButton.grid(row=0, column=2)

# Packs in tho root part
info_frame.pack()
playing_field.pack()
error_label.pack()


root.mainloop()