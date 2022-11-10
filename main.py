import time

from djitellopy import Tello
import cv2

tello = Tello()

tello.connect()


tello.takeoff()
tello.land()



exit(1)