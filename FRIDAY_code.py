from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
import gpiozero

# Initialize the PiCamera
camera = PiCamera()
image_width = 640
image_height = 480
camera.resolution = (image_width, image_height)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(image_width, image_height))

# Define the center of the image and object area thresholds
center_image_x = image_width / 2
center_image_y = image_height / 2
minimum_area = 250
maximum_area = 100000

# Initialize the robot
robot = gpiozero.Robot(left=(22, 27), right=(17, 23))
forward_speed = 1.0
turn_speed = 0.8

# Define the target hue value for object detection (in HSV color space)
HUE_VAL = 29

# Define the lower and upper bounds for the target color
lower_color = np.array([HUE_VAL - 10, 100, 100])
upper_color = np.array([HUE_VAL + 10, 255, 255])

# Main loop for object tracking
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array

    # Convert the captured image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Create a color mask to isolate the target color
    color_mask = cv2.inRange(hsv, lower_color, upper_color)

    # Find contours in the color mask
    contours, hierarchy = cv2.findContours(color_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize variables to track the largest object
    object_area = 0
    object_x = 0
    object_y = 0

    # Loop through detected contours
    for contour in contours:
        x, y, width, height = cv2.boundingRect(contour)
        found_area = width * height
        center_x = x + (width / 2)
        center_y = y + (height / 2)
        
        # Check if the current object is larger than the previous largest
        if object_area < found_area:
            object_area = found_area
            object_x = center_x
            object_y = center_y

    # Check if an object was found
    if object_area > 0:
        object_location = [object_area, object_x, object_y]
    else:
        object_location = None

    # Control the robot based on object location
    if object_location:
        if (object_location[0] > minimum_area) and (object_location[0] < maximum_area):
            if object_location[1] > (center_image_x + (image_width / 3)):
                robot.right(turn_speed)
                print("Turning right")
            elif object_location[1] < (center_image_x - (image_width / 3)):
                robot.left(turn_speed)
                print("Turning left")
            else:
                robot.forward(forward_speed)
                print("Forward")
        elif (object_location[0] < minimum_area):
            robot.stop()
            print("Target isn't large enough, searching")
        else:
            robot.stop()
            print("Target large enough, stopping")
    else:
        robot.stop()
        print("Target not found, searching")

    # Clear the video buffer
    rawCapture.truncate(0)
