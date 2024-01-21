# import tkinter as tk
# import random
# import time
# import keyboard

# class KeyBoardGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Keyboard Game")

#         # self.paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#         self.paragraph = "Ipsum"
#         self.current_index = 0

#         self.label = tk.Label(root, text=self.get_display_text(), font=("Helvetica", 14))
#         self.label.pack(pady=10)

#         self.user_input = tk.Entry(root, font=("Helvetica", 14), width=5)
#         self.user_input.pack(pady=5)

#         self.time_limit = 90  # Set time limit in seconds
#         self.start_time = time.time()

#         self.root.bind('<Key>', self.check_key_press)

#         self.update()

#     def get_display_text(self):
#         x = "\u0332".join(self.paragraph[self.current_index] + " ")
#         return self.paragraph[:self.current_index] + x + self.paragraph[self.current_index + 1:]

#     def update(self):
#         elapsed_time = time.time() - self.start_time

#         if elapsed_time >= self.time_limit:
#             self.reset_game()

#         if self.current_index == len(self.paragraph):
#             self.label.config(text="Congratulations! You typed it correctly!")
#             self.user_input.config(state=tk.DISABLED)
#             self.root.destroy()  # Close the Tkinter window

#         else:
#             self.label.config(text=self.get_display_text())
#             self.root.after(100, self.update)  # Update every 100 milliseconds

#     def check_key_press(self, event):
#         if event.keysym.isalnum():  # Check if the pressed key is an alphanumeric character
#             if event.char == self.paragraph[self.current_index]:
#                 self.current_index += 1
#                 self.user_input.delete(0, tk.END)
#             else:
#                 # Incorrect key press, restart the game
#                 self.reset_game()

#     def reset_game(self):
#         self.label.config(text="Game Over! Please restart.")
#         self.user_input.config(state=tk.DISABLED)
#         self.root.after(2000, self.restart)

#     def restart(self):
#         # self.paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#         self.paragraph = "Ipsum"
#         self.current_index = 0
#         self.start_time = time.time()

#         self.label.config(text=self.get_display_text())
#         self.user_input.config(state=tk.NORMAL)
#         self.user_input.delete(0, tk.END)

#         self.update()

# # Main program
# root = tk.Tk()

# def nothing(): return

# root.protocol("WM_DELETE_WINDOW", nothing)
# root.overrideredirect(True)

# # root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# game = KeyBoardGame(root)
# root.mainloop()


import tkinter as tk
import random
import time
import keyboard
from tkinter import ttk


class KeyBoardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Keyboard Game")

        self.paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        # self.paragraph = "Ipsum"
        self.current_index = 0

        # self.label = tk.Label(root, text=self.get_display_text(), font=("Helvetica", 14))
        # self.label.pack(pady=10)

        # self.user_input = tk.Entry(root, font=("Helvetica", 14), width=5)
        # self.user_input.pack(pady=5)

        # Padding for the entire GUI
        self.padding_x = 20
        self.padding_y = 20

        # Center the window
        self.root_width = 800 + 2 * self.padding_x
        self.root_height = 600 + 2 * self.padding_y
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_position = (screen_width - self.root_width) // 2
        y_position = (screen_height - self.root_height) // 2
        self.root.geometry(f"{self.root_width}x{self.root_height}+{x_position}+{y_position}")

        # Themed styles
        style = ttk.Style()
        style.configure('TLabel', font=('Helvetica', 14), padding=(10, 5))
        style.configure('TEntry', font=('Helvetica', 14), padding=(10, 5))
        style.configure('TButton', font=('Helvetica', 12), padding=(10, 5), foreground='white', background='#4CAF50')

        # Create and pack the label
        self.label = ttk.Label(root, text="Enter something:", style='TLabel')
        self.label.pack(pady=20)

        # Create and pack the entry widget
        self.user_input = ttk.Entry(root, style='TEntry', width=30)
        self.user_input.pack(pady=10)

        # Button to go back
        self.open_button = ttk.Button(root, text="Back", style='TButton', command=self.open_another_window)
        self.open_button.pack(pady=20)

        self.time_limit = 90  # Set time limit in seconds
        self.start_time = time.time()

        self.root.bind('<Key>', self.check_key_press)

        self.update()
        # self.open_button = tk.Button(self.root, text="Back", command=self.open_another_window)
        # self.open_button.pack()

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


root = tk.Tk()

padding_x = 20
padding_y = 20
root_width = 800 + 2 * padding_x
root_height = 600 + 2 * padding_y
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - root_width) // 2
y_position = (screen_height - root_height) // 2
root.geometry(f"{root_width}x{root_height}+{x_position}+{y_position}")


def nothing(): return

root.protocol("WM_DELETE_WINDOW", nothing)
root.overrideredirect(True)

# root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

game = KeyBoardGame(root)
root.mainloop()