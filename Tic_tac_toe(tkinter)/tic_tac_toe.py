from tkinter import *
from tkinter import messagebox
# from random import randint
import time
# from PIL import Image,ImageTk


# GLOABAL VARIABLES
ActivePlayer = 1
p1 = []  # what player one selected
p2 = []  # what player rwo selected
Count = 0
ScoreX = 0
ScoreO = 0
new = 1

root = Tk()
root.geometry("1000x600")
root.title("Tic Tac Toe :Player 1")
# root.iconbitmap("img/sv.ico")
root.configure(background="#b92b27")
root.wm_attributes("-transparentcolor","#b92b27")

# # Declaration of variables
hour = StringVar()
minute = StringVar()
second = StringVar()

# setting the default value as 0
hour.set(" 00")
minute.set(" 0")
second.set(" 10")
#
# # Use of Entry class to take input from the user
frame=Frame(root, bg="#6dd5ed")
frame.grid(row=0, column=1, padx=5, pady=5, sticky='nsnew')


# Use of Entry class to take input from the user
hourEntry = Entry(frame, width=10, font=("Arial", 18, "bold"),
                  textvariable=hour,bd=2,bg="#C6FFDD")
hourEntry.place(x=80, y=2,height=50,width=42)

minuteEntry = Entry(frame,width=10,  font=("Arial", 18, "bold"),
                    textvariable=minute,bd=2,bg="#C6FFDD")
minuteEntry.place(x=130, y=2,height=50, width=42)

secondEntry = Entry(frame, width=10, font=("Arial", 18, "bold"),
                    textvariable=second,bd=2,bg="#C6FFDD")
secondEntry.place(x=180, y=2,height=50,width=42)
def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:

        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours = 0
        if mins > 60:
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)

        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
            root.destroy()
            openweb()

        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1


btn = Button(frame, text='Start', bd='5',font=("times new roman",15,"bold"),bg="#6b6b83",
             command=submit)
btn.place(x=250, y=5)

#---------end--

label2 = Label(root, text=f'PLAYER1: {ScoreX}\nPLAYER2: {ScoreO}', font="Times 15 bold", bg='#e55d87',
               fg='#5fc3e4', bd=4, height=1, width=10, relief=RAISED, )
label2.grid(row=4, column=0, padx=5, pady=4, sticky='nsnew')

label3 = Label(root, text='PLAYER 1', font="Times 15 bold", bg='cadet blue', fg='black', bd=4, height=2, width=10,
               relief=RAISED, )
label3.grid(row=0, column=0, padx=5, pady=4, sticky='nsnew')

label4 = Label(root, text='PLAYER 2', font="Times 15 bold", bg='white', fg='black', bd=4, height=2, width=10,
               relief=RAISED, )

# BUTTONS
b1 = Button(root, text='', font="Times 35 bold", bg='#b7bfcf', fg='black', width=8)
b1.grid(row=1, column=0, padx=5, pady=4, sticky='snew')
b1.config(command=lambda: ButtonClick(1))


b2 = Button(root, text='', font="Times 35 bold", bg='#ffc0cb', fg='black', width=8)
b2.grid(row=1, column=1, padx=5, pady=4, sticky='snew')
b2.config(command=lambda: ButtonClick(2))

b3 = Button(root, text='', font="Times 35 bold", bg='#0be7c9', fg='black', width=8)
b3.grid(row=1, column=2, padx=5, pady=4, sticky='snew')
b3.config(command=lambda: ButtonClick(3))

b4 = Button(root, text='', font="Times 35 bold", bg='#134261', fg='black', width=8)
b4.grid(row=2, column=0, padx=5, pady=4, sticky='snew')
b4.config(command=lambda: ButtonClick(4))

b5 = Button(root, text='', font="Times 35 bold", bg='#616161', fg='black', width=8)
b5.grid(row=2, column=1, padx=5, pady=4, sticky='snew')
b5.config(command=lambda: ButtonClick(5))

b6 = Button(root, text='', font="Times 35 bold", bg='#a896b6', fg='black', width=8)
b6.grid(row=2, column=2, padx=5, pady=4, sticky='snew')
b6.config(command=lambda: ButtonClick(6))

b7 = Button(root, text='', font="Times 35 bold", bg='#2f82d5', fg='black', width=8)
b7.grid(row=3, column=0, padx=5, pady=4, sticky='snew')
b7.config(command=lambda: ButtonClick(7))

b8 = Button(root, text='', font="Times 35 bold", bg='#a896b6', fg='black', width=8)
b8.grid(row=3, column=1, padx=5, pady=4, sticky='snew')
b8.config(command=lambda: ButtonClick(8))

b9 = Button(root, text='', font="Times 35 bold", bg='#420420', fg='black', width=8)
b9.grid(row=3, column=2, padx=5, pady=4, sticky='snew')
b9.config(command=lambda: ButtonClick(9))


b10 = Button(root, font="Times 15 bold",  text='RESTART', bg='#853155', fg='white', height=2, width=8)
b10.grid(row=4, column=1, padx=5, pady=4, sticky='snew')
b10.config(command=lambda: Restart())

b11 = Button(root, font="Times 15 bold", text='END', bg='cadet blue', fg='white', height=2, width=8)
b11.grid(row=4, column=2, padx=5, pady=4, sticky='snew')
b11.config(command=lambda: game_terminate())
b11.config(command=lambda:openweb())


def game_terminate():
    root.destroy()


def Restart():
    global label3
    global label4
    global ActivePlayer
    ActivePlayer = 1

    global Count
    Count = 0

    label3.destroy()
    label4.destroy()

    root.title("Tic Tac Toe :Player 1")

    label3 = Label(root, text='PLAYER 1', font="Times 15 bold", bg='cadet blue', fg='black', bd=4, height=2, width=10,
                   relief=RAISED, )
    label3.grid(row=0, column=0, padx=5, pady=5, sticky='nsnew')

    b1['state'] = 'active'
    b1['text'] = ''
    b1['bg'] = 'white'
    b2['state'] = 'active'
    b2['text'] = ''
    b2['bg'] = 'white'
    b3['state'] = 'active'
    b3['text'] = ''
    b3['bg'] = 'white'
    b4['state'] = 'active'
    b4['text'] = ''
    b4['bg'] = 'white'
    b5['state'] = 'active'
    b5['text'] = ''
    b5['bg'] = 'white'
    b6['state'] = 'active'
    b6['text'] = ''
    b6['bg'] = 'white'
    b7['state'] = 'active'
    b7['text'] = ''
    b7['bg'] = 'white'
    b8['state'] = 'active'
    b8['text'] = ''
    b8['bg'] = 'white'
    b9['state'] = 'active'
    b9['text'] = ''
    b9['bg'] = 'white'
    p1.clear()
    p2.clear()


def game_ended():
    global Count
    Count = 0

    b1['state'] = 'disable'
    b1['text'] = ''
    b2['state'] = 'disable'
    b2['text'] = ''
    b3['state'] = 'disable'
    b3['text'] = ''
    b4['state'] = 'disable'
    b4['text'] = ''
    b5['state'] = 'disable'
    b5['text'] = ''
    b6['state'] = 'disable'
    b6['text'] = ''
    b7['state'] = 'disable'
    b7['text'] = ''
    b8['state'] = 'disable'
    b8['text'] = ''
    b9['state'] = 'disable'
    b9['text'] = ''
    p1.clear()
    p2.clear()


def ButtonClick(id):
    global label3
    global label4
    global ActivePlayer
    global p15
    global p2

    if ActivePlayer == 1:

        label3.destroy()

        SetLayout(id, "x", "#BCC6CC")
        p1.append(id)

        label4 = Label(root, text='PLAYER 2', font="Times 15 bold", bg='#195882', fg='black', bd=4, height=2, width=10,
                       relief=RAISED, )
        label4.grid(row=0, column=2, padx=5, pady=5, sticky='nsnew')

        root.title("Tic Tac Toe :Player 2")
        ActivePlayer = 2
        print(f"P1:{p1}")

    else:
        label4.destroy()
        SetLayout(id, "O", "#F0FFFF")
        p2.append(id)

        label3 = Label(root, text='PLAYER 1', font="Times 15 bold", bg='#195882', fg='black', bd=4, height=2,
                       width=10, relief=RAISED, )
        label3.grid(row=0, column=0, padx=5, pady=5, sticky='nsnew')

        root.title("Tic Tac Toe :Player 1")
        ActivePlayer = 1
        print(f"P2:{p2}")
    if Count == 5 or Count > 5:
        CheckWiner()


def SetLayout(id, PlayerSymbol, colr):
    global Count
    if id == 1:
        b1['text'] = PlayerSymbol
        b1['state'] = 'disabled'
        b1['bg'] = colr
        b1['fg'] = 'black'
        Count = Count + 1

    elif id == 2:
        b2['text'] = PlayerSymbol
        b2['state'] = 'disable'
        b2['bg'] = colr
        Count = Count + 1

    elif id == 3:
        b3['text'] = PlayerSymbol
        b3['state'] = 'disable'
        b3['bg'] = colr
        Count = Count + 1

    elif id == 4:
        b4['text'] = PlayerSymbol
        b4['state'] = 'disable'
        b4['bg'] = colr
        Count = Count + 1

    elif id == 5:
        b5['text'] = PlayerSymbol
        b5['state'] = 'disable'
        b5['bg'] = colr
        Count = Count + 1

    elif id == 6:
        b6['text'] = PlayerSymbol
        b6['state'] = 'disable'
        b6['bg'] = colr
        Count = Count + 1

    elif id == 7:
        b7['text'] = PlayerSymbol
        b7['state'] = 'disable'
        b7['bg'] = colr
        Count = Count + 1
    elif id == 8:
        b8['text'] = PlayerSymbol
        b8['state'] = 'disable'
        b8['bg'] = colr
        Count = Count + 1

    elif id == 9:
        b9['text'] = PlayerSymbol
        b9['state'] = 'disable'
        b9['bg'] = colr
        Count = Count + 1


def AssignSeperateColorToWiner(id):
    if id == 'R1':
        b1['bg'] = 'light green'
        b2['bg'] = 'light green'
        b3['bg'] = 'light green'
    if id == 'R2':
        b4['bg'] = 'light green'
        b5['bg'] = 'light green'
        b6['bg'] = 'light green'
    if id == 'R3':
        b7['bg'] = 'light green'
        b8['bg'] = 'light green'
        b9['bg'] = 'light green'
    if id == 'C1':
        b1['bg'] = 'light green'
        b4['bg'] = 'light green'
        b7['bg'] = 'light green'
    if id == 'C2':
        b2['bg'] = 'light green'
        b5['bg'] = 'light green'
        b8['bg'] = 'light green'
    if id == 'C3':
        b3['bg'] = 'light green'
        b6['bg'] = 'light green'
        b9['bg'] = 'light green'
    if id == 'D1':
        b1['bg'] = 'light green'
        b5['bg'] = 'light green'
        b9['bg'] = 'light green'
    if id == 'D2':
        b3['bg'] = 'light green'
        b5['bg'] = 'light green'
        b7['bg'] = 'light green'


def CheckWiner():
    global ScoreX
    global ScoreO
    Winer = -1
    # Rows
    if ((1 in p1) and (2 in p1) and (3 in p1)):
        Winer = 1
        AssignSeperateColorToWiner('R1')
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        Winer = 2
        AssignSeperateColorToWiner('R1')

    if ((4 in p1) and (5 in p1) and (6 in p1)):
        Winer = 1
        AssignSeperateColorToWiner('R2')
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        Winer = 2
        AssignSeperateColorToWiner('R2')

    if ((7 in p1) and (8 in p1) and (9 in p1)):
        Winer = 1
        AssignSeperateColorToWiner('R3')
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        Winer = 2
        AssignSeperateColorToWiner('R3')

    # Columns
    if ((1 in p1) and (4 in p1) and (7 in p1)):
        Winer = 1
        AssignSeperateColorToWiner('C1')
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        Winer = 2
        AssignSeperateColorToWiner('C1')

    if ((2 in p1) and (5 in p1) and (8 in p1)):
        Winer = 1
        AssignSeperateColorToWiner('C2')
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        Winer = 2
        AssignSeperateColorToWiner('C2')

    if ((3 in p1) and (6 in p1) and (9 in p1)):
        Winer = 1
        AssignSeperateColorToWiner('C3')
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        Winer = 2
        AssignSeperateColorToWiner('C3')

    # Diagonals
    if ((1 in p1) and (5 in p1) and (9 in p1)):
        Winer = 1
        AssignSeperateColorToWiner('D1')
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        Winer = 2
        AssignSeperateColorToWiner('D1')

    if ((3 in p1) and (5 in p1) and (7 in p1)):
        Winer = 1
        AssignSeperateColorToWiner('D2')
    if ((3 in p2) and (5 in p2) and (7 in p2)):
        Winer = 2
        AssignSeperateColorToWiner('D2')

    # check
    if Winer == 1:
        messagebox.showinfo(title="Congrat.", message="Player 1 is the winner")
        ScoreX += 1
        label2['text'] = f'PLAYER1: {ScoreX}\nPLAYER2: {ScoreO}'
        game_ended()
    elif Winer == 2:
        messagebox.showinfo(title="Congrat.", message="Player 2 is the winner")
        ScoreO += 1
        label2['text'] = f'PLAYER1: {ScoreX}\nPLAYER2: {ScoreO}'
        game_ended()
    elif Winer == -1 and Count == 9:
        messagebox.showinfo(title="Oops!!", message="It's a Tie")
        game_ended()

for i in range(1, 4):
    root.grid_rowconfigure(i, weight=1)

for i in range(3):
    root.grid_columnconfigure(i, weight=1)

def enter_function(event):
    b10.invoke()

root.bind('<Return>', enter_function)