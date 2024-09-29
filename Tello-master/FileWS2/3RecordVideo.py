import time, cv2
from threading import Thread
from djitellopy import Tello

tello = Tello()

tello.connect()

keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()

def videoRecorder():
    # create a VideoWrite object, recording to ./video.avi
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video8.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()

# we need to run the recorder in a separate thread, otherwise blocking options
# would prevent frames from getting added to the video

recorder = Thread(target=videoRecorder)
recorder.start()

tello.takeoff()
tello.move_up(20)

# Extend the recording for 5 seconds
time.sleep(5)

tello.land()

keepRecording = False
recorder.join()

