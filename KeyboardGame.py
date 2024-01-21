

import tkinter as tk
import random
import time
import keyboard

class KeyBoardGame:
    def __init__(self, root, parent,parentObject):
        self.root = root
        self.parent = parent
        self.parentObject = parentObject
        self.root.title("Keyboard Game")

        self.paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        # self.paragraph = "Ipsum"
        self.current_index = 0

        self.label = tk.Label(root, text=self.get_display_text(), font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.user_input = tk.Entry(root, font=("Helvetica", 14), width=5)
        self.user_input.pack(pady=5)

        self.time_limit = 90  # Set time limit in seconds
        self.start_time = time.time()

        self.root.bind('<Key>', self.check_key_press)

        self.update()
        self.open_button = tk.Button(self.root, text="Back", command=self.open_another_window)
        self.open_button.pack()

    def open_another_window(self):
        self.root.withdraw()
        self.parent.deiconify()

    def get_display_text(self):
        x = "\u0332".join(self.paragraph[self.current_index] + " ")
        return self.paragraph[:self.current_index] + x + self.paragraph[self.current_index + 1:]

    def update(self):
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= self.time_limit:
            self.reset_game()

        if self.current_index == len(self.paragraph):
            self.label.config(text="Congratulations! You typed it correctly!")
            self.user_input.config(state=tk.DISABLED)
            self.parentObject.setNormalKeyboard()

        else:
            self.label.config(text=self.get_display_text())
            self.root.after(100, self.update)  # Update every 100 milliseconds

    def check_key_press(self, event):
        if event.keysym.isalnum():  # Check if the pressed key is an alphanumeric character
            if event.char == self.paragraph[self.current_index]:
                self.current_index += 1
                self.user_input.delete(0, tk.END)
            else:
                # Incorrect key press, restart the game
                self.reset_game()

    def reset_game(self):
        self.label.config(text="Game Over! Please restart.")
        self.user_input.config(state=tk.DISABLED)
        self.root.after(2000, self.restart)

    def restart(self):
        self.paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        # self.paragraph = "Ipsum"
        self.current_index = 0
        self.start_time = time.time()

        self.label.config(text=self.get_display_text())
        self.user_input.config(state=tk.NORMAL)
        self.user_input.delete(0, tk.END)

        self.update()


def open_keyboard_game(parent, parentObject):
    root = tk.Tk()

    def nothing(): return
    root.protocol("WM_DELETE_WINDOW", nothing)
    #root.overrideredirect(True)
    #root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    game = KeyBoardGame(root, parent,parentObject)

    return root
