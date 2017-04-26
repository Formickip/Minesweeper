# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import random


root = Tk()
squares = []
punkty = []
bg_color = "white"
C = Canvas(root, bg=bg_color, height=200, width=200, bd=0)
mines = 10
flags = 10
correct_flags = 0

class Field:
    def __init__(self, x, y):
        self.x = 0
        self.y = 0
        self.type = 0 # 0 - normal, 1 - bomb
        self.flag = 0
        self.ilosc = 0 # ilosc bomb

for i in range(10):
    for j in range(10):
        punkty.append(Field(j, i))
        squares.append(C.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill=bg_color))

for i in range(10):
    x = random.randint(1,100)
    print(x)
    punkty[x].type = 1
    punkty[x].ilosc = 3

def leftclick(event):
    i = [(event.x // 20), (event.y // 20)]
    print(i)
    if punkty[i[0] + i[1] * 10].type == 1:
        C.itemconfig(squares[i[0] + i[1] * 10], fill="red")
        gameover()


def rightclick(event):
    i = [(event.x // 20), (event.y // 20)]
    global flags
    global correct_flags
    if punkty[i[0] + i[1] * 10].flag == 1:  #Odznaczenie gdy flaga juz jest
        C.itemconfig(squares[i[0] + i[1] * 10], fill=bg_color)
        punkty[i[0] + i[1] * 10].flag = 0
        flags += 1
        if punkty[i[0] + i[1] * 10].type == 1:
            correct_flags -= 1
            print(correct_flags)
    else:
        if flags > 0:                       #Zaznaczenie gdy nie ma flagi, spelnia warunek >0
            C.itemconfig(squares[i[0] + i[1] * 10], fill="yellow")
            punkty[i[0] + i[1] * 10].flag = 1
            flags -= 1
            if punkty[i[0] + i[1] * 10].type == 1:
                correct_flags += 1
                print(correct_flags)
                if correct_flags == 10:
                    victory()

def gameover():
    messagebox.showinfo("Game Over", "Kaboom ! You Lose!")
    global root
    root.destroy()

def victory():
    messagebox.showinfo("Game Over", "You Win!")
    global root
    root.destroy()

root.title("Minesweeper")
C.bind("<Button-1>", leftclick)
C.bind("<Button-3>", rightclick)
C.pack()
root.mainloop()

"""
TO DO
3 buttony odnosnie ilosci bomb,
ustawianie wysokosci i szerokosci w jakis sposob

"""
