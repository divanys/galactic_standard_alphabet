from tkinter import *
import translate, to_pictures
root = Tk()
root.title("std gal alph")
root.geometry("300x250+800+400")
to_pictures.to_pictures(translate.galactic_array)

root.mainloop()