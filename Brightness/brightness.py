import tkinter as tk
from PIL import Image, ImageTk
import random
import screen_brightness_control as sbc

# Global variables
selected_image = None
score = 0
image_label = None

# Declare PIL images globally
pil_image1 = Image.open("./Brightness/cat.jpg")
pil_image2 = Image.open("./Brightness/funny.jpg")
pil_image3 = Image.open("./Brightness/monkey.jpg")
sbc.fade_brightness(0)

def initialize_window():
    global image_label, selected_image

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    resized_image = pil_image1.resize((screen_width-100, screen_height-80))
    mystery_image = ImageTk.PhotoImage(resized_image)

    selected_image = pil_image1

    image_label = tk.Label(root, image=mystery_image)
    image_label.pack()




def display_image():
    global selected_image
    #Images array
    images = [pil_image1, pil_image2, pil_image3]
    selected_image = random.choice(images)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    resized_image = selected_image.resize((screen_width-100, screen_height-80))

    new_image = ImageTk.PhotoImage(resized_image)
    image_label.config(image=new_image)
    image_label.image = new_image
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

# def jumpscare():
#     global score

#     display_image()

#     if selected_image == pil_image1:
#         score += 1
#         score_label.config(text=f"Score: {score}")

#     if score == 5:
#         show_popup()

def handle_normal():
    display_image()

def show_popup():
    popup = tk.Toplevel(root)
    popup.title("Congratulations!")
    popup.geometry("300x100")
    popup_label = tk.Label(popup, text="You scored 5 points! You win!")
    popup_label.pack()
    popup_button = tk.Button(popup, text="OK", command=popup.destroy)
    popup_button.pack()

root = tk.Tk()
root.title("Image Game")
root.attributes('-fullscreen', True)

initialize_window()

# jumpscare_button = tk.Button(root, text="Jumpscare", command=jumpscare)
normal_button = tk.Button(root, text="Next", command=display_image)
score_label = tk.Label(root, text=f"Score: {score}")

#jumpscare_button.pack()
normal_button.pack()
score_label.pack()

root.mainloop()
