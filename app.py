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
import platform
import os
import keyboard
import time
import random
from threading import Thread

class AnnoyingApp:
    def __init__(self, master, s4):
        self.root = master
        self.root.configure(bg='#ffa500')
        self.WIDTH, self.HEIGHT = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        self.root.title('Annoying app')
        self.s4 = s4
        self.s3 = None
        self.s2 = None
        self.normalKeyboard = False
       

        
        def nothing():
            return
        self.root.protocol('WM_DELETE_WINDOW', nothing)
        self.create_buttons()

        self.consecutive_presses_required = random.randint(2, 6)
        self.start_keyboard_control()
        self.root.after(20000*3*60, self.update)
        self.callVolume()

    def callVolume(self):
        from Volume.volume import open_mouse_game
        self.s3 = open_mouse_game(self.root)
        print(self.s3)
        self.s3.mainloop()


    def update(self):
        if self.s2 is not None:
            self.s2.destroy()
            self.s2 = None
        if self.s3 is not None:
            self.s3.destroy()
            self.s3 = None
        self.root.destroy()
        self.s4.deiconify()
        self.root.after(20000*3*60, self.update)

    def start_keyboard_control(self):
        # Disable the button while the thread is running

        # Create a thread and target it to the control_keyboard function
        thread = Thread(target=self.control_keyboard)
        # Set the thread to daemon mode so that it doesn't block the program exit
        thread.daemon = True
        # Start the thread
        thread.start()
        
        #write code to start and stop the thread based on a condition

        # Check the thread status periodically and update the button when it's done
        self.root.after(100, lambda: self.check_thread(thread))

    def check_thread(self, thread):
        # Check if the thread is still alive
        if thread.is_alive():
            self.root.after(100, lambda: self.check_thread(thread))

    def control_keyboard(self):
        print(self.normalKeyboard)
        x = random.randint(2, 6)
        print(x)
        consecutive_presses_required = x
        while True and self.normalKeyboard == False:
            cnt=0
            if self.normalKeyboard == True:
                    break
            while cnt < consecutive_presses_required - 1 and self.normalKeyboard == False:
                if self.normalKeyboard == True:
                    break
                key_event = keyboard.read_event(suppress=True)
                if key_event.event_type == keyboard.KEY_DOWN and key_event.name.isalnum():
                    cnt += 1
                if key_event.event_type == keyboard.KEY_UP and key_event.name in ['shift', 'caps lock']:
                    keyboard.release(key_event.name)
                    cnt-=1
                if key_event.event_type == keyboard.KEY_DOWN and key_event.name in ['shift', 'caps lock']:
                    keyboard.press(key_event.name)

            key_event = keyboard.read_event(suppress=False)
            while key_event.event_type != keyboard.KEY_DOWN and key_event.name.isalnum()and self.normalKeyboard == False:
                if self.normalKeyboard == True:
                    break
                key_event = keyboard.read_event(suppress=False)
                x = random.randint(2, 6)
                print(x)
                consecutive_presses_required = x

    # def control_keyboard(self):

    #     if self.normalKeyboard == False:
    #         cnt = 0

    #         while cnt < consecutive_presses_required - 1:
    #             key_event = keyboard.read_event(suppress=True)
    #             if key_event.event_type == keyboard.KEY_DOWN and key_event.name.isalnum():
    #                 # if key_event.name in ['shift', 'caps lock']:
    #                 #     # Handle Shift and Caps Lock separately if needed
    #                 #     pass
    #                 # else:
    #                 cnt += 1
    #             if key_event.event_type == keyboard.KEY_UP and key_event.name in ['shift', 'caps lock']:
    #                 keyboard.release(key_event.name)

    #             if key_event.event_type == keyboard.KEY_DOWN and key_event.name in ['shift', 'caps lock']:
    #                 keyboard.press(key_event.name)
                

    #         key_event = keyboard.read_event(suppress=False)
    #         # while key_event.event_type != keyboard.KEY_DOWN or key_event.name in ['shift', 'caps lock']:
    #         while key_event.event_type != keyboard.KEY_DOWN and key_event.name.isalnum():
    #             key_event = keyboard.read_event(suppress=False)
    #             x = random.randint(2, 6)
    #             print(x)
    #             consecutive_presses_required = x

    def setNormalKeyboard(self):
        self.normalKeyboard = True

    def top_left_redirect(self):
        self.normalKeyboard = True
      #  self.root.destroy()
        # import trial

    def top_right_redirect(self):

        self.root.withdraw()
        if self.s2 is None:
            from KeyboardGame import open_keyboard_game
            self.s2 = open_keyboard_game(self.root,self)
            print(self.s2)
            self.s2.mainloop()
        else:
            self.s2.deiconify()
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
        self.root.withdraw()
        if self.s4 is None:
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
            from brightness import open_brightness_game
            self.s4 = open_brightness_game(self.root)
            print(self.s4)
            self.s4.mainloop()
        else:
            self.s4.deiconify()

    def create_buttons(self):
        # if platform.system() == 'Windows':
        Top_Left = tk.Button(self.root, bg='#ff0000', command=self.top_left_redirect, text="Top Left")
        Top_Left.place(x=0, y=0, width=self.WIDTH/2, height=self.HEIGHT/2)

        Top_Right = tk.Button(self.root, bg='#3cb371', command=self.top_right_redirect, text="Top Right")
        Top_Right.place(x=self.WIDTH/2, y=0, width=self.WIDTH/2, height=self.HEIGHT/2)

        Bottom_Left = tk.Button(self.root, bg='#eee7da', command=self.bottom_left_redirect, text="Bottom Left")
        Bottom_Left.place(x=0, y=self.HEIGHT/2, width=self.WIDTH/2, height=self.HEIGHT/2)

        Bottom_Right = tk.Button(self.root, bg='#fad7a0', command=self.bottom_right_redirect, text="Bottom Right")
        Bottom_Right.place(x=self.WIDTH/2, y=self.HEIGHT/2, width=self.WIDTH/2, height=self.HEIGHT/2)
        # else:
        #     Top_Left = Button(self.root, bg='#ff0000', command=self.top_left_redirect, text="Top Left")
        #     Top_Left.place(x=0, y=0, width=self.WIDTH/2, height=self.HEIGHT/2)

        #     Top_Right = Button(self.root, bg='#3cb371', command=self.top_right_redirect, text="Top Right")
        #     Top_Right.place(x=self.WIDTH/2, y=0, width=self.WIDTH/2, height=self.HEIGHT/2)

        #     Bottom_Left = Button(self.root, bg='#eee7da', command=self.bottom_left_redirect, text="Bottom Left")
        #     Bottom_Left.place(x=0, y=self.HEIGHT/2, width=self.WIDTH/2, height=self.HEIGHT/2)

        #     Bottom_Right = Button(self.root, bg='#fad7a0', command=self.bottom_right_redirect, text="Bottom Right")
        #     Bottom_Right.place(x=self.WIDTH/2, y=self.HEIGHT/2, width=self.WIDTH/2, height=self.HEIGHT/2)

    def run(self):
        
        self.root.mainloop()

def open_main_menu(s4):
    root = tk.Tk()

    def nothing(): return
    root.protocol("WM_DELETE_WINDOW", nothing)

    menu = AnnoyingApp(root, s4)
   # game.initialize_window()
    #root.mainloop()
    return root

