from tkinter import *
from functools import partial

player = 0
playing_field_machine = []

def update(i, j, button_list):
    global player
    global playing_field_machine
    if playing_field_machine[i][j] == -1:
        player = (player + 1) % 2
        playing_field_machine[i][j] = player
        player_move(button_list[i][j])


def player_move(button):
    global player
    if player == 0:
        text = "O"
    else:
        text = "X"
    button.config(text=text, command=None)

def generate(x, y, button_list, playing_field):
    global playing_field_machine
    for i in range(x):
        playing_field_machine.append([])
        button_list.append([])
        for j in range(y):
            playing_field_machine[i].append(-1)

            button_list[i].append(Button(playing_field, command=partial(update, i, j, button_list)))
            button_list[i][j].grid(column=i, row=j)

root = Tk()

player_frame = Frame(root)
playing_field = Frame(root)

button_list = []

v_size = 20
h_size = 19

generate(h_size, v_size, button_list, playing_field)

playing_field.pack()
root.mainloop()

