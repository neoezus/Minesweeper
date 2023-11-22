from tkinter import *
import tools
from grill import grill
import tkinter.messagebox

root = Tk()
root.geometry(f'{tools.WIDTH}x{tools.HEIGHT}')
root.title('MINESWIPIT')
root.resizable(False,False)#pour que les dimensions des widgetes ne soient pas modifié
root.configure(bg='black')
title_frame = Frame(bg="#000000" ,width=tools.WIDTH,height=tools.heigh_prcntg(25))
title_frame.place(x=0, y=0)
score_frame = Frame(bg="#000000", width=tools.width_prcntg(25), height=tools.heigh_prcntg(75))
score_frame.place(x=0, y=tools.heigh_prcntg(25))
consol_frame = Frame(root, bg="#000000", width=tools.width_prcntg(75), height=tools.heigh_prcntg(75))
consol_frame.place(x=tools.width_prcntg(25), y=tools.heigh_prcntg(25))
board = None
for x in range(8):
    for y in range(8):
        board = grill(x,y)
        board.creat_btn(consol_frame)
        board.btn_objet.grid(column=x, row=y)
#on a appler les objet de la class grill pour generer une table qui contien nos boutons dynamiques
grill.random_mine_generator()
game_label= Label(title_frame,text="MineswipIT",background="#000000",fg="#00FF00",font=("Arial",32))
game_label.pack()
counter_label = Label(score_frame, text=board.counter, font=("Arial", 16), background="#000000", fg="#00FF00")
counter_label.pack()


root.mainloop()




