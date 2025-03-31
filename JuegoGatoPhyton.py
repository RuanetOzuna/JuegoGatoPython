import tkinter as tk
from tkinter import messagebox
import random

def check_winner():
    for line in winning_combinations:
        if buttons[line[0]]['text'] == buttons[line[1]]['text'] == buttons[line[2]]['text'] != "":
            messagebox.showinfo("Juego Terminado", f"{buttons[line[0]]['text']} ha ganado!")
            reset_board()
            return True
    if all(button['text'] != "" for button in buttons.values()):
        messagebox.showinfo("Juego Terminado", "Es un empate!")
        reset_board()
        return True
    return False

def make_move(index):
    global turn
    if buttons[index]['text'] == "":
        buttons[index]['text'] = turn
        if check_winner():
            return
        turn = "O" if turn == "X" else "X"
        if vs_computer and turn == "O":
            computer_move()
    else:
        messagebox.showwarning("Movimiento inválido", "¡Esta casilla ya está ocupada!")

def computer_move():
    available_moves = [i for i in buttons if buttons[i]['text'] == ""]
    if available_moves:
        move = random.choice(available_moves)
        buttons[move]['text'] = "O"
        if check_winner():
            return
        global turn
        turn = "X"

def reset_board():
    global turn, game_over
    turn = "X"
    game_over = False
    for button in buttons.values():
        button['text'] = ""

def start_game(mode):
    global vs_computer
    vs_computer = True if mode == "vs_computer" else False
    reset_board()

root = tk.Tk()
root.title("Juego del Gato")

# Variables globales
turn = "X"
vs_computer = False
game_over = False
buttons = {}
winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                        (1, 4, 7), (2, 5, 8), (3, 6, 9),
                        (1, 5, 9), (3, 5, 7)]

# Crear tablero (3x3)
frame = tk.Frame(root)
frame.pack()

for i in range(1, 10):
    buttons[i] = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2,
                           command=lambda i=i: make_move(i))
    buttons[i].grid(row=(i-1)//3, column=(i-1)%3)

# Controles de modo de juego
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Button(control_frame, text="Jugador vs Jugador",
          command=lambda: start_game("vs_player")).pack(side=tk.LEFT, padx=10)

tk.Button(control_frame, text="Jugador vs Computadora",
          command=lambda: start_game("vs_computer")).pack(side=tk.RIGHT, padx=10)

# Botón de reinicio
tk.Button(root, text="Reiniciar", command=reset_board).pack(pady=10)

root.mainloop()
