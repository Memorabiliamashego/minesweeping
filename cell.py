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
   
   
    def show_mine(self):
        
        '''logic to interrupt the game & display msg'''
        self.cell_btn_object.configure(bg="red")
    
    def show_cell(self):
        pass


    def left_click_act(self, event):
        ''' logic for left click'''
        if self.is_mine:
            self.show_mine
        else:
            self.show.cell()

    

    def right_click_act(self, event):
        
        '''logic for right click'''
    


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