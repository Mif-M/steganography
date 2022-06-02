from moviepy.editor import VideoFileClip
import numpy as np
import os
from datetime import timedelta


def mp4tomp3(mp4file, mp3file):
    videoclip = VideoFileClip(mp4file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3file)
    audioclip.close()
    videoclip.close()


# mp4tomp3("2.mp4", "audio.mp3")

videoclip = VideoFileClip("output_video.mp4")
videoclip.write_videofile("output_video_2.mp4", audio='audio.mp3')
