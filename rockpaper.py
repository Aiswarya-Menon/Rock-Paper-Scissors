from tkinter import *
from PIL import Image, ImageTk
from random import randint
window = Tk()
window.title("Rock paper Scissors")
window.configure(background="black")

rock_l = ImageTk.PhotoImage(Image.open("rock left.png"))
paper_l = ImageTk.PhotoImage(Image.open("paper left.png"))
scissors_l = ImageTk.PhotoImage(Image.open("scissors left.png"))

rock_r = ImageTk.PhotoImage(Image.open("rock right.png"))
paper_r = ImageTk.PhotoImage(Image.open("paper right.png"))
scissors_r = ImageTk.PhotoImage(Image.open("scissors right.png"))


label_player = Label(window, image=scissors_r)
label_computer = Label(window, image=scissors_l)
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

compuer_score = Label(window, text=" 0 ", font=(
    'arial', 60, "bold"),  fg="blue")
player_score = Label(window, text=" 0 ", font=('arial', 60, "bold"), fg="blue")

compuer_score.grid(row=1, column=1)
player_score.grid(row=1, column=3)

player_indicator = Label(window, font=(
    'arial', 40, "bold"), text="PLAYER", bg="cyan", fg="blue")
computer_indicator = Label(window, font=(
    'arial', 40, "bold"), text="COMPUTER", bg="cyan", fg="blue")

computer_indicator.grid(row=0, column=1)
player_indicator.grid(row=0, column=3)

final_message = Label(window, font=('arial', 40, "bold"),
                      text="Start", bg="red", fg="white")
final_message.grid(row=3, column=2)


def msg_update(a):
    final_message['text'] = a


def Comp_update():
    final = int(compuer_score['text'])
    final += 1
    compuer_score['text'] = str(final)


def Player_update():
    final = int(player_score['text'])
    final += 1
    player_score['text'] = str(final)


def winner(p, c):
    if (p == c):
        msg_update("Its a tie")
    elif p == "rock":
        if c == "paper":
            msg_update("Computer Wins !!!")
            Comp_update()
        else:
            msg_update("Player Wins !!!")
            Player_update()
    elif p == "paper":
        if (c == "scissors"):
            msg_update("Computer Wins !!!")
            Comp_update()
        else:
            msg_update("Player Wins !!!")
            Player_update()
    elif p == "scissors":
        if c == "rock":
            msg_update("Computer Wins !!!")
            Comp_update()
        else:
            msg_update("Player Wins !!!")
            Player_update()
    else:
        pass


to_select = ["rock", "paper", "scissors"]


def choice_update(a):
    choice_comp = to_select[randint(0, 2)]
    if (choice_comp == "rock"):
        label_computer.configure(image=rock_l)
    elif (choice_comp == "paper"):
        label_computer.configure(image=paper_l)
    else:
        label_computer.configure(image=scissors_l)

    if (a == "rock"):
        label_player.configure(image=rock_r)
    elif (a == "paper"):
        label_player.configure(image=paper_r)
    else:
        label_player.configure(image=scissors_r)

    winner(a, choice_comp)


button_rock = Button(window, text="Rock", width=20, height=4, font=(
    "arial", 20, "bold"), bg="magenta", fg="black", command=lambda: choice_update("rock")).grid(row=2, column=1)
button_paper = Button(window, text="Paper", width=20, height=4, font=(
    "arial", 20, "bold"), bg="magenta", fg="black", command=lambda: choice_update("paper")).grid(row=2, column=2)
button_sci = Button(window, text="Scissors", width=20, height=4, font=(
    "arial", 20, "bold"), bg="magenta", fg="black", command=lambda: choice_update("scissors")).grid(row=2, column=3)
window.mainloop()
