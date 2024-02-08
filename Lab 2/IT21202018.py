import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk


# Create the main window
root = tk.Tk()
root.title("Lab 02")

# Function to open an image file and display it
def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        display_image(image)

# Function to display the image on the GUI
def display_image(image):
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)
    panel.config(image=image)
    panel.image = image

def save_profile_image():
    if panel.image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            panel.image.write(file_path)

# Create labels and text input fields
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

# Create radio buttons for gender selection
gender_label = tk.Label(root, text="Gender:")
gender_label.pack()
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
male_radio.pack()
female_radio.pack()



# Create "Save Profile" button
save_button = tk.Button(root, text="Save Profile", command=save_profile_image)
save_button.pack()

# Create "Open Image" button
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

# Create a label to display the image
panel = tk.Label(root)
panel.pack()




# Run the tkinter main loop
root.mainloop()

import cv2

# Load the saved image
input_image_path = 'C:\\Users\\chari\\OneDrive\\Documents\\Sliit\\Y3S1\\DIP\\Lab 2\\test.jpg'
input_image = cv2.imread(input_image_path)

# i. Access the image properties
height, width, channels = input_image.shape
mode = input_image.mode
print("Image Information:")
print(f"Image width: {width}")
print(f"Image height: {height}")
print(f"Format: {format}")
print(f"Color Mode: {mode}")
print(f"Number of channels: {channels}")

# ii. Access and modify pixel values at coordinates (x, y)
x = 100
y = 150
blue_pixel = input_image[y, x, 0]
green_pixel = input_image[y, x, 1]
red_pixel = input_image[y, x, 2]

# Modify the pixel values (making the pixel red)
input_image[y, x] = (0, 0, 255)

# iii. Resize the image to a new width and height
new_width = 300
new_height = 200
resized_image = cv2.resize(input_image, (new_width, new_height))

# Save the resized image
resized_image_path = 'resized_image.png'
cv2.imwrite(resized_image_path, resized_image)

# Rotate the resized image by 90 degrees
angle = 90
rotation_matrix = cv2.getRotationMatrix2D((new_width / 2, new_height / 2), angle, 1)
rotated_image = cv2.warpAffine(resized_image, rotation_matrix, (new_width, new_height))

# Save the rotated image
rotated_image_path = 'rotated_image.png'
cv2.imwrite(rotated_image_path, rotated_image)

# Display the modified and rotated images (optional)
cv2.imshow('Modified Image', input_image)
cv2.imshow('Resized Image', resized_image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()