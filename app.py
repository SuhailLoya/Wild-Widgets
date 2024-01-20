import tkinter as tk
import pyautogui as pg
from PIL import ImageTk, Image
import time

root = tk.Tk()
root.configure(bg='#ffa500')
root.geometry('1600x1200')
root.title('Annoying app') # placeholder

# title = tk.Label(root, text='Welcome to Chem Lab! \n\nSelect what you want to do: ', font=('Arial', 25),
#                  bg='#ffa500')
# title.pack(padx=50, pady=60)

def button1redirect():
    pass

def button2redirect():
    pass

Top_Left = tk.Canvas(root, bg='#ff0000')
Top_Left.place(x=0, y=0, width=800, height=600)

Top_Right = tk.Canvas(root, bg='#3cb371')
Top_Right.place(x=800, y=0, width=800, height=600)

Bottom_Left = tk.Canvas(root, bg='#eee7da')
Bottom_Left.place(x=0, y=600, width=800, height=600)

Bottom_Right = tk.Canvas(root, bg='#fad7a0')
Bottom_Right.place(x=800, y=600, width=800, height=600)

# click_btn1 = ImageTk.PhotoImage(Image.open("Chemistry.jpg"))
# button1 = tk.Button(root, bg='#ff0000', command=button1redirect,
#                  text='\n\n\n\n\n\n\n  Get info on   \n     a molecule     ', font=('Arial', 23))
# button1.place(x=0, y=300, height=300, width=300)

# click_btn2 = ImageTk.PhotoImage(Image.open("structural_elucidation.jpg"))
# button2 = tk.Button(root, image=click_btn2, bg='#3cb371', command=button2redirect,
#                  text='\n\n\n\n\n\n\n  Solve a structural \nelucidation problem', font=('Arial', 23))
# button2.place(x=300, y=300, height=300, width=300)

root.mainloop()


