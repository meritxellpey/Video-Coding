import os


# EXERCISE 1
def hls_converter():
    os.system("ffmpeg -i BBB_vid.mp4 -c:v libx264 -c:a aac -strict -2 -f hls -hls_list_size 0 -hls_time 5 output.m3u8")


# EXERCISE 2
def get_info():
    command = 'mp4info BBB_vid.mp4'
    os.system(command)


def fragment():
    command = 'mp4fragment --fragment-duration 35000 BBB_vid.mp4 BBB_fragmented.mp4'
    os.system(command)


def dash_file():
    command = 'mp4dash --mpd-name dash_BBB.mpd BBB_fragmented.mp4 '
    os.system(command)


def bento_functions():
    print("We'll now proceed to get the info for our mp4 video.")
    get_info()
    print("We'll now fragment our video.")
    fragment()
    print("We'll now dash our file.")
    dash_file()


# EXERCISE 3
def video_streamer():
    command = 'ffmpeg -re -i BBB_vid.mp4 -c:v libx264 -f flv rtmp://localhost/show/stream'
    os.system(command)


def main():
    # START BY CREATING AN HLS CONVERTER
    hls_converter()
    # PLAY WITH BENTO FUNCTIONS
    bento_functions()
    # VIDEO STREAMER
    video_streamer()


main()