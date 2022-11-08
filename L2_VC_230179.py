import os
import subprocess
import sys
import pandas as pd


# EXERCISE 1 - AUDIO PARSER
def parser():
    # Give codec type, name and bit rate of BBB_vid.mp4
    print("Three relevant data from the container are:")
    os.system("ffprobe -v error -select_streams v:0 -show_entries stream=codec_type,codec_name,bit_rate -of "
              "default=noprint_wrappers=1 BBB_vid.mp4")


# EXERCISE 2 - AUDIO EXPORTER AND REPLACER
def audio_exporter():
    # Generate aac audio from BBB_vid.mp4
    subprocess.call(["ffmpeg", "-y", "-i", "BBB_vid.mp4", f"{'BBB_mp3'}.{'mp3'}"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
    # Generate mp3 audio from BBB_vid.mp4
    subprocess.call(["ffmpeg", "-y", "-i", "BBB_vid.mp4", f"{'BBB_AAC'}.{'aac'}"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)

    # Create new mp4 by substituting audio from BBB_vid.mp4 for new aac audio
    os.system("ffmpeg -i BBB_vid.mp4 -i BBB_AAC.aac -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 BBB_vid_AAC.mp4")
    # Create new mp4 by substituting audio from BBB_vid.mp4 for new mp3 audio
    os.system("ffmpeg -i BBB_vid.mp4 -i BBB_mp3.mp3 -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 BBB_vid_MP3.mp4")


# EXERCISE 3 - RESOLUTION CHANGER
def resolution_changer(file):
    ty = input("Is the file we are working with a: \n 1. Video \n 2. Image \n 3. Audio \n")
    if ty == '1':

        # Use BBB_vid.mp4 for example
        output_name = "resized_" + file
        size = input("Input the size you'd like the video to be in the format 123:123 ")
        sizing = "scale=" + size
        os.system("ffmpeg -i " + file + " -vf " + sizing + " " +output_name)

    elif ty == '2':

        # Use tryout_im.png example image if wanted
        output_name = "resized_"+ file
        size = input("Input the size you'd like the video to be in the format 123:123 ")
        sizing = "scale=" + size
        os.system("ffmpeg -i " + file + " -vf " + sizing + " " + output_name)

        # Use BBB_vid.mp4 for example
    elif ty == '3':
        output_name = "resized_audio_" + file
        size = input("Choose an audio bit rate to change audio resolution in the format 1k: ")
        os.system("ffmpeg -i " + file + " -b:v 2M -b:a " + size + " " + output_name)

    else:
        print("You did not input a possible input! Try again!")


# EXERCISE 4 - AUDIO TRACKER
class Ex4:
    def __init__(self, file):
        vid_codec = subprocess.check_output("ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of "
                                            "default=noprint_wrappers=1 " + file, shell=True)
        vid_codec = str(vid_codec).split("=")[1]
        self.vid_codec = vid_codec[0:4]

        audio_codec = subprocess.check_output(
            "ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of "
            "default=noprint_wrappers=1 " + file, shell=True)
        audio_codec = str(audio_codec).split("=")[1]
        self.audio_codec = audio_codec[0:3]

    def audio_tracker(self):

        audio_codec = self.audio_codec
        vid_codec = self.vid_codec

        DVB_vid = ["MPEG2", "h264"]
        DVB_audio = ["aac", "ac3", "mp3"]
        ISDB_vid = ["MPEG2", "h264"]  # VIDEO CHANNELS ISDB
        ATSC_vid = ["MPEG2", "h264"]  # VIDEO CHANNELS ATSC
        DTMV_vid = ["avs", "avs+", "MPEG2", "h264"]  # VIDEO CHANNELS DTMV
        DTMV_audio = ["dra", "aac", "ac3", "mp2", "mp3"]  # AUDIO CHANNELS DTMV

        if audio_codec in DVB_audio:
            if vid_codec in DVB_vid:
                print("The video may have been encoded through DVB.")

        if audio_codec == "aac":
            if vid_codec in ISDB_vid:
                print("The video may have been encoded through ISDB.")

        if audio_codec == "ac3":
            if vid_codec in ATSC_vid:
                print("The video may have been encoded through ATSC.")

        if audio_codec in DTMV_audio:
            if vid_codec in DTMV_vid:
                print("The video may have been encoded through DTMB.")





def main():
    print("Welcome to LAB 2 of video coding. We will start with exercise 1.")
    print("In this exercise we will use parsing to obtain some data from our video BBB.")
    parser()
    print("Now we will export the audio from the BBB video in both mp3 and aac and will replace"
          "the original audio from the video with the new expoerted audios. \n"
          "You can find the result in the folder named BBB_vid_[type].mp4")
    audio_exporter()
    ex_2 = True
    print("The following exercise allows the user to resize audios, videos and images.")
    while ex_2:
        file = input("Input the file you'd like to resize: ")
        resolution_changer(file)
        answer = input("Would you like to resize a another file? [y/n] ")
        if answer == "n":
            ex_2 = False
    print("Please, enter a file you want to know what broadcasting standard may have been used.")
    file = input("Please, input the file you want to study: ")
    tracker = Ex4(file)
    tracker.audio_tracker()


main()