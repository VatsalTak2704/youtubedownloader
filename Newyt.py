
from os import pat
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube, Playlist
import shutil




# functions
def select_path():
    # allow user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    # get user path bjo
    get_link = link_field.get()
    
    # get selected path
    user_path = path_label.cget("text")
    Screen.title('Downloading....')
    
    # download video

    mp4_video = YouTube(get_link).streams.get_by_resolution("720p").download()
    mp4_video = YouTube().streams.get_highest_resolution().download()
    vid_Clip = VideoFileClip(mp4_video)
    vid_Clip.close()
    # move file to selected directary
    shutil.move(mp4_video, user_path)
    Screen.title('Download Complete! Download Another File....')


Screen = Tk() 
title = Screen.title('Youtube Download')
canvas = Canvas(Screen,width=550 ,height=500)
canvas.pack()
# ...................................................
# #image logo
logo_img = PhotoImage(file='yt.png')
# ...........................................
# #resize
logo_img = logo_img.subsample(2,2)
canvas.create_image(250, 80, image=logo_img)

# ............................................
# link field
link_field = Entry(Screen, width=50)
link_label = Label(Screen, text="Enter Download link:", font=('Arial',15))


#...............................................
# Select path for saving the file
path_label = Label(Screen, text="Select Path For Download", font=("Arial",15))
select_btn = Button(Screen, text="Select", command = select_path)

#...............................................................
# Add to window
canvas.create_window(250,270,window= path_label)
canvas.create_window(250,320,window= select_btn)


#................................................................
# add widgets to window 

canvas.create_window(250,170,window= link_label)
canvas.create_window(250,200,window= link_field)

#..............................................................
#  # Download btns

download_btn = Button(Screen, text="Download File", command=download_file)

#............................................................. 
# Add to canvas
canvas.create_window(250,360, window=download_btn)

Screen.mainloop()