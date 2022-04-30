from asyncio import FastChildWatcher
from tkinter import *
from turtle import width



root = Tk()

# Override window settings
root.configure(bg="black")
root.geometry('980x680')
root.title("Mineweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red',   # Change to black later
    width=980,
    height=180
)

top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='blue',   # Change to black later
    width=240,
    height=540
)

left_frame.place(x=0, y=180)

# Run The Window
root.mainloop()