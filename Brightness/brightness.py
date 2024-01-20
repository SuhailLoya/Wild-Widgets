import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame
import screen_brightness_control as sbc


# Global variables
selected_image = None
score = 0
image_label = None

pygame.init()

# Declare PIL images globally
pil_image1 = Image.open("./Brightness/jumpscare1.jpg")
pil_image2 = Image.open("./Brightness/jumpscare2.jpg")
pil_image3 = Image.open("./Brightness/jumpscare3.jpg")
pil_image4 = Image.open("./Brightness/jumpscare4.jpg")
pil_image5 = Image.open("./Brightness/jumpscare5.jpg")
pil_image6 = Image.open("./Brightness/jumpscare6.jpg")
pil_image7 = Image.open("./Brightness/jumpscare7.jpg")
pil_image8 = Image.open("./Brightness/jumpscare8.jpg")

audio_files = [
    pygame.mixer.Sound('./Brightness/scare1.mp3'),
    pygame.mixer.Sound('./Brightness/scare2.mp3'),
    pygame.mixer.Sound('./Brightness/scare3.mp3'),
    pygame.mixer.Sound('./Brightness/scare5.mp3')
]


sbc.fade_brightness(5)

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
    images = [pil_image1, pil_image2, pil_image3,pil_image4,pil_image5,pil_image6,pil_image7
                ,pil_image8]
    selected_image = random.choice(images)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    resized_image = selected_image.resize((screen_width-100, screen_height-80))

    random_audio = random.choice(audio_files)
    random_audio.play()

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
root.config(cursor="arrow")  # Set the cursor to a standard arrow cursor


initialize_window()

# jumpscare_button = tk.Button(root, text="Jumpscare", command=jumpscare)
normal_button = tk.Button(root, text="Change Brightness", command=display_image)
score_label = tk.Label(root, text=f"Score: {score}")

#jumpscare_button.pack()
normal_button.pack()
score_label.pack()

root.mainloop()
