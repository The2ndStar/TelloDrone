from djitellopy import Tello
import time

tello = Tello()
tello.connect()

power = tello.get_battery()
print("Power Level =", power, "%")

# Take off
tello.takeoff()

# Wait for the drone to stabilize
time.sleep(3)  # Wait for 3 seconds

# Execute flip
tello.flip("f")  # 'f' for front, can also be 'b' for back, 'l' for left, or 'r' for right

# Wait a moment after flipping
time.sleep(2)  # Adjust delay as needed

# Land the drone
tello.land()
