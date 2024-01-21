import tkinter as tk
import random
from tkinter import ttk

class CircleGame:
    def __init__(self, root, parent, parentObject):
        print("0928905u238957035923")
        print(parent)
        self.root = root
        self.parent = parent
        self.parentObject = parentObject
        self.root.title("Circle Game")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight() -300
        window_width = self.root.winfo_screenwidth() # Set your desired window width
        window_height = self.root.winfo_screenheight() - 200   # Set your desired window height

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2 +100

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")



        self.canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="white")
        self.canvas.pack()

        self.circle_radius = 20
        self.circle_x = random.randint(self.circle_radius, screen_width - self.circle_radius)
        self.circle_y = random.randint(self.circle_radius, screen_height - self.circle_radius)

        self.circle = self.canvas.create_oval(
            self.circle_x - self.circle_radius,
            self.circle_y - self.circle_radius,
            self.circle_x + self.circle_radius,
            self.circle_y + self.circle_radius,
            fill="blue"
        )

        self.clicked = False
        self.canvas.bind("<Button-1>", self.on_click)
        self.deltax = 0
        self.deltay = 0
        self.update()
        self.move_circle()
        # self.open_button = tk.Button(self.root, text="Back", command=self.open_another_window)
        # self.open_button.pack()

        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12), padding=(10, 5), foreground='white', background='#4CAF50')

        self.open_button = ttk.Button(self.root, text="Back", style='TButton', command=self.open_another_window)
        self.open_button.pack(pady=20)
        print("==========")
        print(self.parent)

    def open_another_window(self):
        self.root.withdraw()
        self.parent.deiconify()

    def update(self):
        self.deltax = random.randint(15, 30)
        self.deltay = random.randint(15, 30)
        self.deltax *= random.choice([-1, 1])
        self.deltay *= random.choice([-1, 1])
        self.root.after(2000, self.update)

    def move_circle(self):
        if not self.clicked:
            self.circle_x += self.deltax
            self.circle_y += self.deltay

            # Ensure the circle stays within the canvas bounds
            if self.circle_x - self.circle_radius < 0:
                self.circle_x = self.circle_radius
                self.deltax*=-1
            elif self.circle_x + self.circle_radius > self.root.winfo_screenwidth():
                self.circle_x = self.root.winfo_screenwidth() - self.circle_radius
                self.deltax *= -1

            if self.circle_y - self.circle_radius < 0:
                self.circle_y = self.circle_radius
                self.deltay*=-1
            elif self.circle_y + self.circle_radius > self.root.winfo_screenheight()-300:
                self.circle_y = self.root.winfo_screenheight() - 300 - self.circle_radius
                self.deltay*=-1

            self.canvas.coords(
                self.circle,
                self.circle_x - self.circle_radius,
                self.circle_y - self.circle_radius,
                self.circle_x + self.circle_radius,
                self.circle_y + self.circle_radius
            )

            self.root.after(100, self.move_circle)

    def on_click(self, event):
        if (
            self.circle_x - self.circle_radius < event.x < self.circle_x + self.circle_radius
            and self.circle_y - self.circle_radius < event.y < self.circle_y + self.circle_radius
        ):
            self.clicked = True
            self.canvas.itemconfig(self.circle, fill="green")
            self.canvas.create_text(self.root.winfo_screenwidth() // 2, self.root.winfo_screenheight() // 2, text="You Win!", font=("Helvetica", 20))
            self.parentObject.setNormalMouse()

def open_mouse_game(parent, parentObject):
    root = tk.Tk()
    #root.attributes('-fullscreen', True)  # Set to full screen

    def nothing(): return
    root.protocol("WM_DELETE_WINDOW", nothing)

    game = CircleGame(root, parent, parentObject)

    return root

#open_mouse_game(None, None).mainloop()
