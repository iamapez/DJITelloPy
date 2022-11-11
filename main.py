import sys
import time
import cv2
import logging
import constants
from DJITelloPy.api import Tello


def main():
    tello = Tello()

    tello.LOGGER.info(constants.MESSAGES.try_connect_drone)
    try:
        tello.connect()
    except Exception as e:
        tello.LOGGER.error(constants.MESSAGES.failed_connect_drone)
        sys.exit('*** Exiting program. Count not connect to the drone.***')

    tello.LOGGER.info(constants.MESSAGES.successful_connect_drone)

    tello.turn_motor_on()
    time.sleep(5)
    tello.turn_motor_off()


if __name__ == '__main__':
    main()
