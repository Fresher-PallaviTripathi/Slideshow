from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

# Initialize Tkinter
root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of Image Paths
image_paths = [
    r"img1.jpg",
    r"img2.jpeg",
    r"img3.jpeg",
    r"img4.jpeg",
    r"img5.jpeg",
    r"img6.jpeg",
    r"img7.jpeg",
    r"img8.jpeg",
    r"img9.jpeg",
]

# Resize images to 1080x1080
image_size = (1550, 1550)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

# Create a Label Widget
label = tk.Label(root)
label.pack()

# Create an Image Iterator using cycle
slideshow = cycle(photo_images)

def update_image():
    """ Update the label with the next image in the slideshow """
    label.config(image=next(slideshow))
    root.after(3000, update_image)  # Change image every 3 seconds

# Start the slideshow
play_button = tk.Button(root, text='Play Slideshow', command=update_image)
play_button.pack()


# Control buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_btn = tk.Button(button_frame, text="▶ Play", command=start_slideshow, width=10)
start_btn.grid(row=0, column=0, padx=10)

pause_btn = tk.Button(button_frame, text="⏸ Pause", command=pause_slideshow, width=10)
pause_btn.grid(row=0, column=1, padx=10)


root.mainloop()




# from itertools import cycle
# from PIL import Image, ImageTk
# import tkinter as tk

# # Initialize Tkinter
# root = tk.Tk()
# root.title("Image Slideshow Viewer")

# # List of Image Paths
# image_paths = [
#     r"img1.jpg",
#     r"img2.jpeg",
#     r"img3.jpeg",
#     r"img4.jpeg",
#     r"img5.jpeg",
#     r"img6.jpeg",
#     r"img7.jpeg",
#     r"img8.jpeg",
#     r"img9.jpeg",
# ]

# # Resize images
# image_size = (1080, 1080)
# images = [Image.open(path).resize(image_size) for path in image_paths]
# photo_images = [ImageTk.PhotoImage(image) for image in images]

# # Image Label
# label = tk.Label(root)
# label.pack(pady=20)

# # Counter Label
# counter_label = tk.Label(root, text="", font=("Arial", 14))
# counter_label.pack()

# # Cycle with index
# slideshow = cycle(enumerate(photo_images))
# current_index = 0
# is_running = False  # Slideshow state

# def update_image():
#     global current_index
#     if is_running:
#         current_index, image = next(slideshow)
#         label.config(image=image)
#         counter_label.config(text=f"Image {current_index + 1} of {len(photo_images)}")
#         root.after(3000, update_image)

# def start_slideshow():
#     global is_running
#     if not is_running:
#         is_running = True
#         update_image()

# def pause_slideshow():
#     global is_running
#     is_running = False

# # Control buttons
# button_frame = tk.Frame(root)
# button_frame.pack(pady=10)

# start_btn = tk.Button(button_frame, text="▶ Play", command=start_slideshow, width=10)
# start_btn.grid(row=0, column=0, padx=10)

# pause_btn = tk.Button(button_frame, text="⏸ Pause", command=pause_slideshow, width=10)
# pause_btn.grid(row=0, column=1, padx=10)

# root.mainloop()
