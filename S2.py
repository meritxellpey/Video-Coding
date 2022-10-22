import subprocess
import ffmpeg
import time
import sys
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


# Function to cut videos
def cutter(N):
    start_time = 0.0      # Define starting time
    end_time = 10.0 - N   # Define ending time
    ffmpeg_extract_subclip("BBB_vid.mp4", start_time, end_time, targetname="cut_BBB.mp4")


def yuv_hist():
    # The following function is divided in
    # 1. "ffplay video -vf histogram" that creates the histogram
    # 2. "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" that creates an overlay between the video and histogram
    subprocess.call(['ffplay', 'BBB_vid.mp4', '-vf', 'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay'])


def resizer(size):
    sizing = "scale="+size
    os.system("ffmpeg -i BBB_vid.mp4 -vf "+sizing+" resized_BBB.mp4")


def audio_changer():
    os.system("ffmpeg -i BBB_vid.mp4 -ac 2 stereo_BBB.mp4")
    os.system("ffmpeg -i stereo_BBB.mp4 -ac 1 mono_BBB.mp4")


def main():
    print("Welcome to Seminar 2, I will guide you through the exercises.")
    print("We will start by cutting a video by certain seconds.")
    N = float(input('Choose the number of seconds you want to cut the video by between 0 and 30: '))
    if N > 30:
        N = 29
    cutter(N)
    print("You can now find the cut video saved in the project folder.")
    print("We will now visualize it next to its yuv histogram.")
    input("Press Enter to continue when you are ready...")
    yuv_hist()
    print("Hope you enjoyed it :) Now, would you like to resize the video?")
    print('Please, choose between the following sizes:')
    options = ['1280:720', '640:480', '360:240', '160:120']
    i = 1
    for option in options:
        print(str(i)+'. '+option)
        i += 1
    size = input('Choose one of the sizing options from 1 to 4 ')
    resizer(options[int(size)-1])
    print('Great! Now you have your cut and resized video saved in the project folder.')
    print("We will proceed by changing the audio from the original to stereo and from stereo to mono.")
    audio_changer()
    time.sleep(20)
    sys.exit(0)


main()
