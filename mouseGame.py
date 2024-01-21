import tkinter as tk
import random


class CircleGame:
    def __init__(self, root, parent, parentObject):
        self.root = root
        self.parent = parent
        self.parentObject = parentObject
        self.root.title("Circle Game")
        # self.root.geometry("400x400")
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        self.canvas = tk.Canvas(root, width=root.winfo_screenwidth()-100, height= root.winfo_screenheight()-100, bg="white")
        self.canvas.pack()

        self.circle_radius = 20
        self.circle_x = random.randint(self.circle_radius, 400 - self.circle_radius)
        self.circle_y = random.randint(self.circle_radius, 400 - self.circle_radius)

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
        self.open_button = tk.Button(self.root, text="Back", command=self.open_another_window)
        self.open_button.pack()
        #self.root.withdraw()
        print("HAKIIU")

    def open_another_window(self):
        self.root.withdraw()
        self.parent.deiconify()
        
        
    def update(self):
        self.deltax = random.randint(10, 20)
        self.deltay = random.randint(10, 20)
        self.deltax *= random.choice([-1, 1])
        self.deltay *= random.choice([-1, 1])
        self.root.after(2000, self.update)
    
    

    def move_circle(self):
        if not self.clicked:
            self.circle_x += self.deltax
            self.circle_y += self.deltay

            # Ensure the circle stays within the canvas bounds
            if self.circle_x - self.circle_radius < 50:
                self.circle_x = self.circle_radius
            elif self.circle_x + self.circle_radius > self.root.winfo_screenwidth()-50:
                self.circle_x = self.root.winfo_screenwidth() -50 - self.circle_radius

            if self.circle_y - self.circle_radius < 0:
                self.circle_y = self.circle_radius
            elif self.circle_y + self.circle_radius > self.root.winfo_screenheight()-50:
                self.circle_y = self.root.winfo_screenheight() -50 -  self.circle_radius

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
            self.canvas.create_text(200, 200, text="You Win!", font=("Helvetica", 20))
            self.parentObject.setNormalMouse()

def open_mouse_game(parent, parentObject):
    root = tk.Tk()

    def nothing(): return
    root.protocol("WM_DELETE_WINDOW", nothing)

    game = CircleGame(root, parent, parentObject)

   # game.initialize_window()

    return root

open_mouse_game(None, None).mainloop()
