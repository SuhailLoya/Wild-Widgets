import tkinter as tk
import platform
import os
import keyboard
import time
import random
from threading import Thread
import pyautogui as pg

pg.FAILSAFE = False

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
        self.s1 = None
        self.normalKeyboard = False
       
        self.normalMouseControls = False
        
        def nothing():
            return
        self.root.protocol('WM_DELETE_WINDOW', nothing)
        self.create_buttons()

        self.consecutive_presses_required = random.randint(2, 6)
        
        self.move_cursor_randomly()
        self.start_keyboard_control()
        self.root.after(20000*3*60, self.update)
        print("asfuafssa")
        self.callVolume()
        print("asfuafssa")

    def callVolume(self):
        from Volume.volume import open_volume_game
        self.s3 = open_volume_game(self.root)
        print(self.s3)
        self.s3.mainloop()


    def update(self):
        print("hi")
        if self.s1 is not None:
            self.s1.destroy()
            self.s1 = None
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

    def move_cursor_randomly(self):
        print("A")
        if self.normalMouseControls == False:
            x = random.randint(0, 3000)
            print("b")
            y = random.randint(0, 1900)
            pg.moveTo(x, y)
            self.root.after(2000, self.move_cursor_randomly) 

    def setNormalKeyboard(self):
        self.normalKeyboard = True

    def setNormalMouse(self):
        self.normalMouseControls = True        

    def top_left_redirect(self):
        self.root.withdraw()
        if self.s1 is None:
            from mouseGame import open_mouse_game
            self.s1 = open_mouse_game(self.root,self)
            print(self.s1)
            self.s1.mainloop()
        else:
            self.s1.deiconify()
            print("ausfhiashga")
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
            from Volume.volume import open_volume_game
            self.s3 = open_volume_game(self.root)
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
        Top_Left = tk.Button(self.root, bg='#ff0000', command=self.top_left_redirect, text="Mouse Control", font="Serif 13 bold")
        Top_Left.place(x=0, y=0, width=self.WIDTH/2, height=self.HEIGHT/2)

        Top_Right = tk.Button(self.root, bg='#3cb371', command=self.top_right_redirect, text="Keyboard Control", font="Serif 13 bold")
        Top_Right.place(x=self.WIDTH/2, y=0, width=self.WIDTH/2, height=self.HEIGHT/2)

        Bottom_Left = tk.Button(self.root, bg='#eee7da', command=self.bottom_left_redirect, text="Volume Control", font="Serif 13 bold")
        Bottom_Left.place(x=0, y=self.HEIGHT/2, width=self.WIDTH/2, height=self.HEIGHT/2)

        Bottom_Right = tk.Button(self.root, bg='#fad7a0', command=self.bottom_right_redirect, text="Brightness Control", font="Serif 13 bold")
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

open_main_menu(None).mainloop()