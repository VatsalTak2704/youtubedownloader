# Import the modules
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import shutil

# Create a GUI window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Create a label for the link field
link_label = tk.Label(window, text="Enter the YouTube link:")
link_label.pack()

# Create an entry for the link field
link_field = tk.Entry(window)
link_field.pack()

# Create a label for the path field
path_label = tk.Label(window, text="Select a path to save the video:")
path_label.pack()

# Create a button for the path field
path_button = tk.Button(window, text="Browse", command=lambda: select_path())
path_button.pack()

# Create a function to select a path from the explorer
def select_path():
    # Allow user to select a path from the explorer
    path = filedialog.askdirectory()
    # Update the path label with the selected path
    path_label.config(text=path)

# Create a button for the download field
download_button = tk.Button(window, text="Download", command=lambda: download_file())
download_button.pack()

# Create a function to download the file
def download_file():
    # Get user input link
    get_link = link_field.get()
    
    # Get selected path
    user_path = path_label.cget("text")
    
    # Change window title to show downloading status
    window.title("Downloading...")
    
    # Download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    
    # Move file to selected directory
    shutil.move(mp4_video, user_path)
    
    # Change window title to show download completion status
    window.title("Download Complete! Download Another File...")

# Start the main loop of the window
window.mainloop()
# Import the modules
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import shutil

# Create a GUI window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Create a label for the link field
link_label = tk.Label(window, text="Enter the YouTube link:")
link_label.pack()

# Create an entry for the link field
link_field = tk.Entry(window)
link_field.pack()

# Create a label for the path field
path_label = tk.Label(window, text="Select a path to save the video:")
path_label.pack()

# Create a button for the path field
path_button = tk.Button(window, text="Browse", command=lambda: select_path())
path_button.pack()

# Create a function to select a path from the explorer
def select_path():
    # Allow user to select a path from the explorer
    path = filedialog.askdirectory()
    # Update the path label with the selected path
    path_label.config(text=path)

# Create a button for the download field
download_button = tk.Button(window, text="Download", command=lambda: download_file())
download_button.pack()

# Create a function to download the file
def download_file():
    # Get user input link
    get_link = link_field.get()
    
    # Get selected path
    user_path = path_label.cget("text")
    
    # Change window title to show downloading status
    window.title("Downloading...")
    
    # Download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    
    # Move file to selected directory
    shutil.move(mp4_video, user_path)
    
    # Change window title to show download completion status
    window.title("Download Complete! Download Another File...")

# Start the main loop of the window
window.mainloop()
