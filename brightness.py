import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame
import screen_brightness_control as sbc
from tkinter import ttk



class ImageGame:
    def __init__(self, master, parent):
        #super().__init__()
        self.root = master
        self.parent = parent
        self.root.title("Image Game")
        self.root.config(cursor="arrow")  # Set the cursor to a standard arrow cursor

        # Global variables
        self.selected_image = None

        pygame.init()
        # Declare PIL images globally
        self.images = [
            Image.open("jumpscare1.jpg"),
            Image.open("jumpscare2.jpg"),
            Image.open("jumpscare3.jpg"),
            Image.open("jumpscare4.jpg"),
            Image.open("jumpscare5.jpg"),
            Image.open("jumpscare6.jpg"),
            Image.open("jumpscare7.jpg"),
            Image.open("jumpscare8.jpg")
        ]

        self.audio_files = [
            pygame.mixer.Sound('scare1.mp3'),
            pygame.mixer.Sound('scare2.mp3'),
            pygame.mixer.Sound('scare4.mp3'),
            pygame.mixer.Sound('scare5.mp3')
        ]
       
        

        sbc.fade_brightness(5)
        self.resized_image = self.images[0].resize((800, 600))
        self.mystery_image = ImageTk.PhotoImage(self.resized_image)

        self.selected_image = self.images[0]

        self.random_audio = random.choice(self.audio_files)
        self.random_audio.play()

        self.image_label = tk.Label(master=self.root, width=800,height=600)
        self.tmp()

        
        self.display_image()

        # style = ttk.Style()
        # style.configure('TButton', font=('Helvetica', 12), padding=(10, 5), foreground='white', background='#4CAF50')


        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 10), padding=(7, 5), foreground='black', background='white', bordercolor='black')

        self.open_button = ttk.Button(self.root, text="Back", style='TButton', command=self.open_another_window)
        self.open_button.pack(pady=20)

        jumpscare_button = ttk.Button(self.root, text="Jumpscare", style='TButton', command=self.display_image)
        jumpscare_button.pack(pady=20)

        # Create a custom style for the "Jumpscare" button with a different background color
        # style.map('Special.TButton',
        #           foreground=[('active', 'blue'), ('disabled', 'blue')],
        #           background=[('active', 'blue'), ('disabled', 'blue')])

    
    def tmp(self):
        self.image_label = tk.Label(image=self.mystery_image)
        self.image_label.pack()

    def open_another_window(self):
        
        if(self.parent is not None):
            if(self.parent.s2 is not None):
                self.parent.s2.destroy()
            if(self.parent.s3 is not None):
                self.parent.s3.destroy()
            self.parent.destroy()
        self.root.withdraw()
        from app import open_main_menu
        self.parent = open_main_menu(self.root)
        self.parent.mainloop()

    def display_image(self):
        # Images array
        print("a")
        self.selected_image = random.choice(self.images)
        self.resized_image = self.selected_image.resize((800, 600))

        self.random_audio = random.choice(self.audio_files)
        self.random_audio.play()

        new_image = ImageTk.PhotoImage(image=self.resized_image)
        self.image_label.config(image=new_image)
        self.image_label.image = new_image

        # Create a list of brightness levels
        brightness_levels = list(range(101))  # 0 to 100

        # Assign weights: significantly higher for 0-20
        lower_range_weight = 97
        upper_range_weight = 5
        weights = [lower_range_weight if level <= 20 else upper_range_weight for level in brightness_levels]

        # Use weighted choice to select a brightness level
        random_brightness = random.choices(brightness_levels, weights=weights, k=1)[0]

        # Set the screen brightness to this random value
        sbc.set_brightness(random_brightness)


def open_brightness_game(parent):
    root = tk.Tk()

    def nothing(): return
    root.protocol("WM_DELETE_WINDOW", nothing)

    game = ImageGame(root, parent)


    return root

open_brightness_game(None).mainloop()
