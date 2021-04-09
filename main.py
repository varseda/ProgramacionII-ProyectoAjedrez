from tkinter import *
from string import ascii_letters
from Cell import Cell

# Creacion de centana principal
root = Tk()
root.title("Ajedrez")


def changePosition():
    buttonP.grid(row=5, column=3)


# Creacion del frame tablero con posiciones
# ------------------------------------------------------------------------------
frameBoardPositions = Frame(root, background="black")
frameBoardPositions.grid(row=0, column=0)
# ------------------------------------------------------------------------------

# Creacion etiquetas de posiciones
# ------------------------------------------------------------------------------
listPositionsLetters = []
listPositionsNumbers = []

for i in range(0, 8):

    listPositionsLetters.append(
        Label(frameBoardPositions, foreground="white", background="black", text=ascii_letters[i], font=("Verdana", 12)))
    listPositionsLetters[i].grid(row=0, column=(i + 1))

    listPositionsNumbers.append(
        Label(frameBoardPositions, foreground="white", background="black", text=str(i), font=("Verdana", 12)))
    listPositionsNumbers[i].grid(row=(i + 1), column=0, padx=5, pady=5)
# ------------------------------------------------------------------------------

# Creacion del frame tablero
# ------------------------------------------------------------------------------
frameBoard = Frame(frameBoardPositions)
frameBoard.grid(row=1, column=1, rowspan=8, columnspan=8)

listBoard = [[None] * 8] * 8
image0 = PhotoImage(file="Images/frame0.png")
image1 = PhotoImage(file="Images/frame1.png")

for i in range(0, 8):

    for j in range(0, 8):

        if i % 2 == 0:

            if j % 2 == 0:

                listBoard[i][j] = Cell(frame=frameBoard, row=i, column=j)
                listBoard[i][j].label.config(image=image0)

            else:

                listBoard[i][j] = Cell(frame=frameBoard, row=i, column=j)
                listBoard[i][j].label.config(image=image1)

        else:

            if j % 2 == 0:

                listBoard[i][j] = Cell(frame=frameBoard, row=i, column=j)
                listBoard[i][j].label.config(image=image1)

            else:

                listBoard[i][j] = Cell(frame=frameBoard, row=i, column=j)
                listBoard[i][j].label.config(image=image0)
# ------------------------------------------------------------------------------


# Creacion del frame de estado
# ------------------------------------------------------------------------------
# frameState = Frame(root)
# frameState.grid(row=0, column=1, padx=5, pady=5)

# labelPlayer0 = Label(frameState, text="Jugador #1", font=16)
# labelPlayer0.grid(row=0, column=0)

# labelPlayer1 = Label(frameState, text="Jugador #2", font=16)
# labelPlayer1.grid(row=1, column=0)
# ------------------------------------------------------------------------------

buttonP = Button(frameBoard, text="HOLA", command=changePosition)
buttonP.grid(row=0, column=0)


root.resizable(0, 0)
root.mainloop()
