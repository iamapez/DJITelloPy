import sys
import time
import cv2
import logging
import constants
from DJITelloPy.api import Tello


def main():
    """ Connect to the Drone"""
    tello = Tello()

    tello.LOGGER.info(constants.MESSAGES.try_connect_drone)
    try:
        tello.connect()
    except Exception as e:
        tello.LOGGER.error(constants.MESSAGES.failed_connect_drone)
        sys.exit('*** Exiting program. Could not connect to the drone.***')

    tello.LOGGER.info(constants.MESSAGES.successful_connect_drone)

    start_time = time.time()    # start the flight timer

    """ Do some pre-flight checks before continuing"""
    tello.turn_motor_on()
    time.sleep(5)

    """ Actually execute a flight"""
    tello.turn_motor_off()

    tello.LOGGER.info("--- %s seconds ---" % (time.time() - start_time))
    exit(1)


if __name__ == '__main__':
    main()
