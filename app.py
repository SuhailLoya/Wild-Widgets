import tkinter as tk
import time

root = tk.Tk()
root.configure(bg='#ffa500')
WIDTH, HEIGHT = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('Annoying app')

def nothing(): return
root.protocol('WM_DELETE_WINDOW', nothing)

def top_left_redirect():
    root.destroy()
    import trial

def top_right_redirect():
    root.destroy()
    import mouse_chase

def bottom_left_redirect():
    root.destroy()
    # import trial

def bottom_right_redirect():
    root.destroy()
    # import game2

Top_Left = tk.Button(root, bg='#ff0000', command=top_left_redirect)
Top_Left.place(x=0, y=0, width=WIDTH/2, height=HEIGHT/2)

Top_Right = tk.Button(root, bg='#3cb371', command=top_right_redirect)
Top_Right.place(x=WIDTH/2, y=0, width=WIDTH/2, height=HEIGHT/2)

Bottom_Left = tk.Button(root, bg='#eee7da', command=bottom_left_redirect)
Bottom_Left.place(x=0, y=HEIGHT/2, width=WIDTH/2, height=HEIGHT/2)

Bottom_Right = tk.Button(root, bg='#fad7a0', command=bottom_right_redirect)
Bottom_Right.place(x=WIDTH/2, y=HEIGHT/2, width=WIDTH/2, height=HEIGHT/2)

root.mainloop()
