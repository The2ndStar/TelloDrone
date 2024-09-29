from djitellopy import Tello
import time, cv2

# create and connect
#
tello = Tello()
tello.connect()

# configure drone
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(2)


tello.takeoff()
tello.move_up(30)
pad = tello.get_mission_pad_id()

# detect and react to pads until we see pad #1
while pad != 1:
    if pad == 3:
        tello.move_up(30)
        tello.rotate_counter_clockwise(90)
        tello.rotate_clockwise(90)
        tello.move_forward(30)

    if pad == 8:
        tello.move_down(30)
        tello.rotate_counter_clockwise(90)
        tello.move_forward(30)

    if pad == 2:
        tello.streamon()
        frame_read = tello.get_frame_read()
        cv2.imwrite("picture18.png", frame_read.frame)
        tello.streamoff()
        tello.land()

    pad = tello.get_mission_pad_id()

# termination
tello.disable_mission_pads()
tello.land()

tello.end()
