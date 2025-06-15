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

# Resize images
image_size = (800, 600)  # Adjust to fit your screen
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

# Slideshow state variables
slideshow = cycle(photo_images)
slideshow_running = False
after_id = None

# Create Label for Image
label = tk.Label(root)
label.pack()

def show_next_image():
    global after_id
    label.config(image=next(slideshow))
    after_id = root.after(3000, show_next_image)  # next image in 3 sec

def start_slideshow():
    global slideshow_running
    if not slideshow_running:
        slideshow_running = True
        show_next_image()

def pause_slideshow():
    global slideshow_running, after_id
    if slideshow_running:
        root.after_cancel(after_id)
        slideshow_running = False

# Control Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_btn = tk.Button(button_frame, text="▶ Play", command=start_slideshow, width=10)
start_btn.grid(row=0, column=0, padx=10)

pause_btn = tk.Button(button_frame, text="⏸ Pause", command=pause_slideshow, width=10)
pause_btn.grid(row=0, column=1, padx=10)

root.mainloop()
