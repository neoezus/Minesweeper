
from tkinter import *
import random
list = []

class grill: #class grill
    def __init__(self, x, y, counter=64, its_a_mine=False):
        self.its_a_mine = its_a_mine
        self.btn_objet = None
        self.x = x
        self.y = y
        self.counter = counter
        list.append(self)#permet de mettre tous les elements dans une liste

    def creat_btn(self,location):#methode qui permet de fair un display des bouttons
        btn= Button(location,width=10,height=3)
        self.btn_objet = btn

        btn.bind('<Button-1>', self.action)
        self.btn_objet = btn

    def action(self, event):#methode des actions lors que cliques sur les boutons
        if self.its_a_mine:
            self.shown_mine()
            self.counter -= 1
        else:
            self.show_cell()

    def get_cell(self, x, y):
        for cell in list:
            if cell.x == x and cell.y == y:
                return cell

    def count_surrounding_mines(self):
        count = 0
        cells = [
            self.get_cell(self.x - 1, self.y - 1),
            self.get_cell(self.x - 1, self.y),
            self.get_cell(self.x - 1, self.y + 1),
            self.get_cell(self.x, self.y - 1),
            self.get_cell(self.x + 1, self.y - 1),
            self.get_cell(self.x + 1, self.y),
            self.get_cell(self.x + 1, self.y + 1),
            self.get_cell(self.x, self.y + 1)

        ]
        cells = [cell for cell in cells if cell is not None]
        for cell in cells:
            if cell.its_a_mine:
                count += 1
        return count


    def show_cell(self):
         count = self.count_surrounding_mines()
         self.btn_objet.configure(text=str(count))



    def shown_mine(self):
        self.btn_objet.configure(bg="red")
        self.btn_objet.configure(text="*")








    @staticmethod
    def random_mine_generator():
        bombe_cells = random.sample(list,15)
        for bombe_cells in bombe_cells:
            bombe_cells.its_a_mine= True


    def __repr__(self):
         return f"grill({self.x}, {self.y})"






