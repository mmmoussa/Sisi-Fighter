from tkinter import *
from egyptGame import EgyptGame

# --- Setting up window ---
root = Tk()
root.minsize(600,300)
root.geometry("600x300")
rTitle = root.title("Sisi Game")

# --- Window Menu ---
menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Start game", command=EgyptGame)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

# --- Character info display ---
characterFrame = Frame(root, bg="blue") # Character info frame
characterFrame.pack(side=TOP, fill=X)
playerLabel = Label(characterFrame, text="This is the player!", justify=LEFT)
vLabel = Label(characterFrame, text=" vs. ")
enemyLabel = Label(characterFrame, text="This is the enemy!", justify=RIGHT)
playerLabel.pack(side=LEFT)
vLabel.pack(fill=X, side=LEFT)
enemyLabel.pack(side=LEFT)

root.mainloop()
