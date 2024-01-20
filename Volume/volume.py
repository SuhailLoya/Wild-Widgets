import tkinter as tk
import platform


class PumpGame:
    def __init__(self, master, parent):
        self.master = master
        self.parent = parent
        self.master.title("Pump Game")

        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="white")
        self.canvas.pack()

        # Pump container
        self.container = self.canvas.create_rectangle(150, 98, 250, 302, fill="white", outline="black", width = 3)

        # Pump handle
        handle_x = (150 + 250) / 2
        handle_y = 100

        self.handle_horizontal = self.canvas.create_line(handle_x - 20, 30, handle_x + 20, 30, width=10, fill="black")
        self.handle_vertical = self.canvas.create_line(handle_x, handle_y, handle_x, 30, width=5, fill="black")

        # Fluid level
        self.fluid_level_height = 300
        self.fluid = self.canvas.create_rectangle(155, 300, 245, 300, fill="green", outline="green")

        # Percentage label
        self.percentage_label = tk.Label(self.master, text="0%", font=("Arial", 12))
        self.percentage_label.pack()

        # Event bindings
        self.canvas.tag_bind(self.handle_horizontal, '<B1-Motion>', lambda event: self.move_handle(event))
        self.canvas.bind("<ButtonRelease-1>", self.stop_pumping)
        self.canvas.tag_bind(self.handle_horizontal, '<Button-1>', self.start_pumping)

        # Pumping variables
        self.pumping = False

        # Set system platform
        self.systemPlatform = platform.system()

        # Initialize system value
        self.set_system_volume(0)
        self.iszero = True;


        # Initiate update
        self.master.after(100, self.update_function100) #100ms
        self.master.after(2000, self.update_function2000) # 2000ms

        self.open_button = tk.Button(self.master, text="Back", command=self.open_another_window)
        self.open_button.pack()
        self.master.withdraw()

    def open_another_window(self):
        self.master.withdraw()
        self.parent.deiconify()



    def move_handle(self, event):
        if self.pumping:
            handle_x = (150 + 250) / 2
            last_handle_y = self.canvas.coords(self.handle_horizontal)[1]
            handle_y = min(max(event.y, 30), 100)
            self.canvas.coords(self.handle_horizontal, handle_x - 20, handle_y, handle_x + 20, handle_y)
         #   self.canvas.coords(self.handle_vertical, handle_x, handle_y)

            # Check if handle is moving downward
            #print(handle_y-last_handle_y)
            if handle_y > last_handle_y:
                annoyance_level = 5
                self.update_fluid_level((handle_y - last_handle_y) / annoyance_level)

    def start_pumping(self, event):
        self.pumping = True

    def stop_pumping(self, event):
        self.pumping = False

    def update_fluid_level(self, y_delta):
        current_height = max(100, self.canvas.coords(self.fluid)[1] - y_delta)
        current_height = min(300, current_height)
        if(current_height !=self.fluid_level_height):
            self.fluid_level_height = current_height
            self.canvas.coords(self.fluid, 155, current_height, 245, 300)
            
            # Update percentage label
            total_height = 200  # height of the container
            filled_height = 300 - current_height
            percentage_filled = (filled_height / total_height) * 100
            self.percentage_label.config(text=f"{int(percentage_filled)}%")

            # Set system value
            self.set_system_volume(percentage_filled / 100)
    
    def update_function100(self):
        #print("a")
        #print(self.iszero)
        self.update_fluid_level(-2)
        self.master.after(100, self.update_function100)
        
    
    def update_function2000(self):
        if self.iszero:
            self.set_system_volume(0)
        #print("h")
        self.master.after(2000, self.update_function2000)
    
    def set_system_volume(self, volume_level):
        if(volume_level == 0):
            self.iszero = True
        else: 
            self.iszero = False

        if self.systemPlatform == 'Windows':
            from ctypes import cast, POINTER
            from comtypes import CLSCTX_ALL
            from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None
            )
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            volume.SetMasterVolumeLevelScalar(volume_level, None)

        elif self.systemPlatform in ['Linux', 'Darwin']:  # Linux or macOS
            import os
            import subprocess

            if self.systemPlatform == 'Linux':
                command = f"amixer -D pulse sset Master {int(volume_level * 100)}%"
            else:  # macOS
                command = f"osascript -e 'set volume output volume {int(volume_level * 100)}'"

            subprocess.run(command, shell=True)

        else:
            print(f"Unsupported operating system: {self.systemPlatform}")


def open_mouse_game(parent):
    root = tk.Tk()

    def nothing(): return
    root.protocol("WM_DELETE_WINDOW", nothing)

    game = PumpGame(root, parent)
    return root


## comment
#open_mouse_game()