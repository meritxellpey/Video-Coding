import os
import tkinter as tk
from tkinter.ttk import Combobox


# Define a function to call the encoder chosen by the user
def encoder(file, opt):
    if opt == "VP8":
        encoder_vp8(file)
    elif opt == "VP9":
        encoder_vp9(file)
    elif opt == "h.265":
        encoder_h265(file)
    elif opt == "AV1":
        encoder_av1(file)


# Encoder to VP8
def encoder_vp8(file):
    sizing = file.split("_")  # Divde file name by "_" to get size
    if len(sizing) == 3:
        sizing[2] = sizing[2].split(".")[0]
        sizing = sizing[1] + "_" + sizing[2]
        print(sizing)
    else:
        sizing = sizing[1].split(".")[0]
    out_name = "BBB_" + sizing + "_vp8.mkv"  # Define an output name
    os.system("ffmpeg -i " + file + " -c:v libvpx " + out_name)  # Call ffmpeg


# Encoder to VP9
def encoder_vp9(file):
    sizing = file.split("_")
    if len(sizing) == 3:
        sizing[2] = sizing[2].split(".")[0]
        sizing = sizing[1] + "_" + sizing[2]
        print(sizing)
    else:
        sizing = sizing[1].split(".")[0]
    out_name = "BBB_" + sizing + "_vp9.mkv"
    os.system("ffmpeg -i " + file + " -c:v libvpx-vp9 " + out_name)


# Encoder to H.265
def encoder_h265(file):  # Repeat process for all encoders
    sizing = file.split("_")
    if len(sizing) == 3:
        sizing[2] = sizing[2].split(".")[0]
        sizing = sizing[1] + "_" + sizing[2]
    else:
        sizing = sizing[1].split(".")[0]
    out_name = "BBB_" + sizing + "_h265.mp4"
    os.system("ffmpeg -i " + file + " -c:v libx265 -vtag hvc1 " + out_name)


# Encoder to AV1
def encoder_av1(file):
    sizing = file.split("_")
    if len(sizing) == 3:
        sizing[2] = sizing[2].split(".")[0]
        sizing = sizing[1] + "_" + sizing[2]
    else:
        sizing = sizing[1].split(".")[0]
    out_name = "BBB_" + sizing + "_av1.mkv"
    os.system("ffmpeg -i " + file + " -c:v libaom-av1 " + out_name)


# Create tkinter window
window = tk.Tk()
window.title("SEMINAR 3")

# Define some introductory labels
btn = tk.Label(window, text="WELCOME TO SEMINAR 3 OF VIDEO CODING.", fg='purple')
btn.pack()
btn2 = tk.Label(window, text="Choose to what you'd like to convert the BBB video:", fg='purple')
btn2.pack()

var = tk.StringVar()
var.set("Converter")


# Define combo box to choose type of encoder
data = ("VP8", "VP9", "h.265", "AV1")
cb = Combobox(window, values=data)
cb.pack()

btn3 = tk.Label(window, text="Choose what size you want the video to have:", fg='purple')
btn3.pack()


# Define combo box to choose size of video
data2 = ("160:120", "360:240", "480p", "720p")
cb2 = Combobox(window, values=data2)
cb2.pack()


# Define function that checks options chosen
def checkcmbo():

    # Check encoder type
    if cb.get() == "VP8":
        opt = "VP8"
    elif cb.get() == "VP9":
        opt = "VP9"
    elif cb.get() == "h.265":
        opt = "h.265"
    elif cb.get() == "AV1":
        opt = "AV1"

    # Check size of file type
    if cb2.get() == "160:120":
        file = "BBB_160_120.mp4"
    elif cb2.get() == "360:240":
        file = "BBB_360_240.mp4"
    elif cb2.get() == "720p":
        file = "BBB_720p.mp4"
    elif cb2.get() == "480p":
        file = "BBB_480p.mp4"

    encoder(file, opt)


# Create button that creates the video with the chosen options
btn2 = tk.Button(window, text="Make my video!", command=checkcmbo)
btn2.pack()


# Define function that creates a 4 window video
def create_4win_vid(event):
    file1 = "BBB_160_120_av1.mkv"
    file2 = "BBB_160_120_h265.mp4"
    file3 = "BBB_160_120_vp8.mkv"
    file4 = "BBB_160_120_vp9.mkv"
    # Stack two videos twice horizontally and then take the output and stack them vertically
    state1 = False
    state2 = False
    os.system("ffmpeg -i " + file1 + " -i " + file2 + " -filter_complex hstack horizontal_stack1.mp4")
    # Check that the first file has been created to move on to the second
    while not state1:
        isExist = os.path.exists("horizontal_stack1.mp4")
        if isExist:
            state1 = True
    os.system("ffmpeg -i " + file3 + " -i " + file4 + " -filter_complex hstack horizontal_stack2.mp4")
    # Check that the second file has been created to move on to the final one
    while not state2:
        isExist = os.path.exists("horizontal_stack2.mp4")
        if isExist:
            state2 = True
    # Create final video with 4 versions of it
    os.system("ffmpeg -i horizontal_stack1.mp4 -i horizontal_stack2.mp4 -filter_complex vstack 4winvid_160x120.mp4")


btn4 = tk.Label(window, text="Click the button below to create a 4 window video:", fg='purple')
btn4.pack()

# Create button that triggers the 4 window function
start = tk.Button(window, text="Make 4 Window Video")
start.pack()
start.bind("<Button-1>", create_4win_vid)

btn5 = tk.Label(window, text="Click the button below to exit the seminar", fg='purple')
btn5.pack()

# Create exit button
exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.pack()

window.mainloop()