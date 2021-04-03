from tkinter import *

# Creacion de centana principal
root = Tk()
root.title("Ajedrez")


def changePosition():
    buttonP.grid(row=5, column=3)


# Creacion del frame tablero
# ------------------------------------------------------------------------------
frameBoard = Frame(root)
frameBoard.grid(row=0, column=0, padx=5, pady=5)

listBoard = []
image0 = PhotoImage(file="Images/frame0.png")
image1 = PhotoImage(file="Images/frame1.png")

for i in range(0, 8):

    listBoard.append([])

    for j in range(0, 8):

        if i % 2 == 0:

            if j % 2 == 0:
                listBoard[i].append(
                    Label(frameBoard, image=image0, borderwidth=0))
                listBoard[i][j].grid(row=i, column=j)
            else:
                listBoard[i].append(Label(frameBoard, image=image1, borderwidth=0))
                listBoard[i][j].grid(row=i, column=j)

        else:

            if j % 2 == 0:
                listBoard[i].append(Label(frameBoard, image=image1, borderwidth=0))
                listBoard[i][j].grid(row=i, column=j)
            else:
                listBoard[i].append(Label(frameBoard, image=image0, borderwidth=0))
                listBoard[i][j].grid(row=i, column=j)
# ------------------------------------------------------------------------------


# Creacion del frame de estado
# ------------------------------------------------------------------------------
frameState = Frame(root)
frameState.grid(row=0, column=1, padx=5, pady=5)

labelPlayer0 = Label(frameState, text="Jugador #1", font=16)
labelPlayer0.grid(row=0, column=0)

labelPlayer1 = Label(frameState, text="Jugador #2", font=16)
labelPlayer1.grid(row=1, column=0)
# ------------------------------------------------------------------------------

buttonP = Button(frameBoard, text="HOLA", command=changePosition)
buttonP.grid(row=0, column=0)


root.resizable(0, 0)
root.mainloop()
