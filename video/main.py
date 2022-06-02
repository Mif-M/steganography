import glob
import os
from datetime import datetime

import cv2


def video_to_frames(path):
    videoCapture = cv2.VideoCapture()
    videoCapture.open(path)
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    print("fps=", int(fps), "frames=", int(frames))
    for i in range(int(frames)):
        ret, frame = videoCapture.read()
        cv2.imwrite("Frame_Decoder_2/frame%d.jpg" % (i), frame)


def f(x):
    return int(x[17:-4])


if __name__ == '__main__':
    t1 = datetime.now()
    video_to_frames("output_video_3.mp4")
    t2 = datetime.now()
    print("Time cost = ", (t2 - t1))

    # vid_capture = cv2.VideoCapture('2.mp4')
    # frameSize = (int(vid_capture.get(3)), int(vid_capture.get(4)))
    # fps = int(vid_capture.get(5))
    # # out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc('D','I','V','X'), fps, frameSize)
    # out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, frameSize)
    # # print(sorted(glob.glob('Frame_Coder/frame*.jpg'), key=f))
    # for filename in sorted(glob.glob('Frame_Coder/frame*.jpg'), key=f):
    #     img = cv2.imread(filename)
    #     out.write(img)
    # out.release()
