from calendar import c
from tkinter import *
from cell import Cell
import settings
import utils


root = Tk()

# Override window settings
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Mineweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',   # Change to black later
    width=settings.WIDTH,
    height=utils.height_perc(25),
)

top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black',   # Change to black later
    width=utils.width_perc(25),
    height=utils.height_perc(75)
)

left_frame.place(x=0, y=utils.height_perc(25))

center_frame = Frame(
    root,
    bg='black', # Change to black later
    width=utils.width_perc(75),
    height=utils.height_perc(75)
)

center_frame.place(
    x=utils.width_perc(25),
    y=utils.height_perc(25)
)



for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

# c1 = Cell()
# c1.create_btn_object(center_frame)
# c1.cell_btn_object.grid(
#     column=0, row=0
# )

# c2 = Cell()
# c2.create_btn_object(center_frame)
# c2.cell_btn_object.grid(
#     column=1, row=0
# )




# Run The Window
root.mainloop()