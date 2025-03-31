import tkinter as tk

def make_move(index):
    global turn
    if buttons[index]['text'] == "":
        buttons[index]['text'] = turn
        turn = "O" if turn == "X" else "X"
        if vs_computer and turn == "O":
            computer_move()

def computer_move():
    available_moves = [i for i in buttons if buttons[i]['text'] == ""]
    if available_moves:
        move = random.choice(available_moves)
        buttons[move]['text'] = "O"
        global turn
        turn = "X"

def reset_board():
    global turn
    turn = "X"
    for button in buttons.values():
        button['text'] = ""

def start_game(mode):
    global vs_computer
    vs_computer = True if mode == "vs_computer" else False
    reset_board()

import random
root = tk.Tk()
root.title("Juego del Gato")

turn = "X"
vs_computer = False
buttons = {}

frame = tk.Frame(root)
frame.pack()

for i in range(1, 10):
    buttons[i] = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2,
                           command=lambda i=i: make_move(i))
    buttons[i].grid(row=(i-1)//3, column=(i-1)%3)

control_frame = tk.Frame(root)
control_frame.pack()

tk.Button(control_frame, text="Jugador vs Jugador", command=lambda: start_game("vs_player")).pack(side=tk.LEFT, padx=10)
tk.Button(control_frame, text="Jugador vs Computadora", command=lambda: start_game("vs_computer")).pack(side=tk.RIGHT, padx=10)

tk.Button(root, text="Reiniciar", command=reset_board).pack(pady=10)

root.mainloop()
