# import tkinter as tk
# import time

# root = tk.Tk()
# root.configure(bg='#ffa500')
# WIDTH, HEIGHT = root.winfo_screenwidth(), root.winfo_screenheight()
# root.geometry(f'{WIDTH}x{HEIGHT}')
# root.title('Annoying app')

# def nothing(): return
# root.protocol('WM_DELETE_WINDOW', nothing)

# def top_left_redirect():
#     root.destroy()
#     import trial

# def top_right_redirect():
#     root.destroy()
#     import mouse_chase

# def bottom_left_redirect():
#     root.destroy()
#     # import trial

# def bottom_right_redirect():
#     root.destroy()
#     # import game2

# Top_Left = tk.Button(root, bg='#ff0000', command=top_left_redirect)
# Top_Left.place(x=0, y=0, width=WIDTH/2, height=HEIGHT/2)

# Top_Right = tk.Button(root, bg='#3cb371', command=top_right_redirect)
# Top_Right.place(x=WIDTH/2, y=0, width=WIDTH/2, height=HEIGHT/2)

# Bottom_Left = tk.Button(root, bg='#eee7da', command=bottom_left_redirect)
# Bottom_Left.place(x=0, y=HEIGHT/2, width=WIDTH/2, height=HEIGHT/2)

# Bottom_Right = tk.Button(root, bg='#fad7a0', command=bottom_right_redirect)
# Bottom_Right.place(x=WIDTH/2, y=HEIGHT/2, width=WIDTH/2, height=HEIGHT/2)

# root.mainloop()

import tkinter as tk
from tkmacosx import Button
import platform

class AnnoyingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg='#ffa500')
        self.WIDTH, self.HEIGHT = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        self.root.title('Annoying app')
        self.s3 = None

        def nothing():
            return
        self.root.protocol('WM_DELETE_WINDOW', nothing)

    def top_left_redirect(self):
        self.root.destroy()
        # import trial

    def top_right_redirect(self):
        self.root.destroy()
        # import mouse_chase

    def bottom_left_redirect(self):
        self.root.withdraw()
        if self.s3 is None:
            from Volume.volume import open_mouse_game
            self.s3 = open_mouse_game(self.root)
            print(self.s3)
            self.s3.mainloop()
        else:
            self.s3.deiconify()

    def bottom_right_redirect(self):
        self.root.destroy()

    def create_buttons(self):
        if platform.system() == 'Windows':
            Top_Left = tk.Button(self.root, bg='#ff0000', command=self.top_left_redirect)
            Top_Left.place(x=0, y=0, width=self.WIDTH/2, height=self.HEIGHT/2)

            Top_Right = tk.Button(self.root, bg='#3cb371', command=self.top_right_redirect)
            Top_Right.place(x=self.WIDTH/2, y=0, width=self.WIDTH/2, height=self.HEIGHT/2)

            Bottom_Left = tk.Button(self.root, bg='#eee7da', command=self.bottom_left_redirect)
            Bottom_Left.place(x=0, y=self.HEIGHT/2, width=self.WIDTH/2, height=self.HEIGHT/2)

            Bottom_Right = tk.Button(self.root, bg='#fad7a0', command=self.bottom_right_redirect)
            Bottom_Right.place(x=self.WIDTH/2, y=self.HEIGHT/2, width=self.WIDTH/2, height=self.HEIGHT/2)
        else:
            Top_Left = Button(self.root, bg='#ff0000', command=self.top_left_redirect, text="Top Left")
            Top_Left.place(x=0, y=0, width=self.WIDTH/2, height=self.HEIGHT/2)

            Top_Right = Button(self.root, bg='#3cb371', command=self.top_right_redirect, text="Top Right")
            Top_Right.place(x=self.WIDTH/2, y=0, width=self.WIDTH/2, height=self.HEIGHT/2)

            Bottom_Left = Button(self.root, bg='#eee7da', command=self.bottom_left_redirect, text="Bottom Left")
            Bottom_Left.place(x=0, y=self.HEIGHT/2, width=self.WIDTH/2, height=self.HEIGHT/2)

            Bottom_Right = Button(self.root, bg='#fad7a0', command=self.bottom_right_redirect, text="Bottom Right")
            Bottom_Right.place(x=self.WIDTH/2, y=self.HEIGHT/2, width=self.WIDTH/2, height=self.HEIGHT/2)

    def run(self):
        self.create_buttons()
        self.root.mainloop()

if __name__ == "__main__":
    app = AnnoyingApp()
    app.run()
