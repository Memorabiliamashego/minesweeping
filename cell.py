from __future__ import print_function
from tkinter import Button
import random
import settings 


class Cell:
    '''Cell Object'''
    all = []
    def __init__(self, x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

    # Append the object to the cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        '''button object function'''
        
        btn = Button(
            
            location,
            width=8, 
            height=4,
        )

        btn.bind('<Button-1>', self.left_click_act) #left click
        btn.bind('<Button-3>', self.right_click_act)    # right click


        self.cell_btn_object = btn
   
   
    def left_click_act(self, event):
        ''' logic for left click'''
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    

    def right_click_act(self, event):
        
        '''logic for right click'''
    

    def show_mine(self):
        
        '''logic to interrupt the game & display msg'''
        self.cell_btn_object.configure(bg="red")
    
    def show_cell(self):
        
        surrounding_cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        print(surrounding_cells)

    def get_cell_by_axis(self, x,y):
        # Return a cell object based on the values of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    

    @staticmethod

    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINE_COUNT
        )
        print(picked_cells)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"