from tkinter import *
from Module2 import user_interface as UI


def app():
    root = Tk()
    root.geometry("600x430+300+100")
    root.title("Image Blur")
    root.resizable(False, False)

    frame = UI(root)
    frame.place()

    root.mainloop()


if __name__ == '__main__':
    app()
