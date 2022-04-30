from tkinter import Button

class Cell:
    '''Cell Object'''
    def __init__(self, x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

    def create_btn_object(self, location):
        '''button object function'''
        
        btn = Button(
            
            location,
            width=8, 
            height=4,
            text = f"{self.x},{self.y}"
        )

        btn.bind('<Button-1>', self.left_click_act) #left click
        
        btn.bind('<Button-3>', self.right_click_act)    # right click


        self.cell_btn_object = btn

    
    def left_click_act(self, event):
        ''' left click function'''
        print(event)
        print("I'm a left click")

    def right_click_act(self, event):
        ''' right click function'''
        print(event)
        print("I'm a right click")