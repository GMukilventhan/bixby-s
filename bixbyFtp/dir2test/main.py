# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *


# --------------------------------GLOBAL VAR--------------------------------#
def testCommand(number):
    for i in range(number):
        print(i)


# --------------------------------GLOBAL VAR--------------------------------#
TITLE = "Bixby Administration Tool"
WELCOME_MESSAGE = "Bienvenue dans l'application de gestion BIXBY!"
AUTHORS = "Authors: Mukil - Jelil - Manveer"

# --------------------------------MAIN START--------------------------------#

# Window creation with tkinter
mainWindow = Tk()
# Window title
mainWindow.title(TITLE)
# Window background color
mainWindow['bg'] = 'white'


# Frame 1
frame1 = Frame(mainWindow, borderwidth=2, relief=GROOVE)

# Text label
welcomeLabel = Label(frame1, text=WELCOME_MESSAGE)

# Text label
authorLabel = Label(frame1, text=AUTHORS)

# Button to connect as admin
adminButton = Button(frame1, text="Administrateur")
# Button to connect as user
userButton = Button(frame1, text="Utilisateur")

# Button to exit window
quitButton = Button(frame1, text="Close", command=mainWindow.quit)

# Packaging in the window
frame1.pack(padx=100, pady=50)
welcomeLabel.pack(pady=5)
authorLabel.pack(pady=5)
adminButton.pack(pady=10)
userButton.pack(pady=10)
quitButton.pack(pady=10)

# Launch Window
mainWindow.mainloop()
