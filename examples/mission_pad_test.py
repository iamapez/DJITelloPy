import time
import cv2
import robomaster.config
from robomaster import robot
from robomaster import camera
import robomaster

# robomaster.config.LOCAL_IP_STR = "192.168.2.20"

if __name__ == '__main__':
    """ *** POPULATE OBJECTS HERE *** """
    tl_drone = robot.Drone()  # instance of the Drone class
    tl_drone.initialize()  # Initialize the robot object. Currently, no input parameters are required for the initialization of education-series drones.

    tl_flight = tl_drone.flight  # Use the get_module() method of the Drone object to obtain the specified object.
    tl_led = tl_drone.led  # control the led on the top of the robot if it is attached
    ep_camera = tl_drone.camera

    tl_flight.mission_pad_on()
    tl_flight._pad_detection(on_off=1)

    drone_battery_threshold = 20
    travel_height = 37

    """ *** PRINT ANY INFORMATION YOU WANT ABOUT THE DRONE BEFORE THE FLIGHT HERE *** """
    # get the sdk version running on the drone
    drone_version = tl_drone.get_sdk_version()
    print("Drone sdk version: {0}".format(drone_version))

    # get the port in use
    drone_port = tl_drone.local_port
    print('Drone port: {0}'.format(drone_port))

    # get battery
    tl_battery = tl_drone.battery
    battery_info = tl_battery.get_battery()
    if battery_info < drone_battery_threshold:
        print("Below safe battery threshold!")
    print("Drone battery soc: {0}".format(battery_info))

    # get the serial number of the drone
    SN = tl_drone.get_sn()
    print("drone sn: {0}".format(SN))

    """ *** FLIGHT STARTS HERE *** """
    tl_flight.takeoff().wait_for_completed()

    tl_led.set_led(r=0, g=0, b=0)
    tl_flight.jump(x=0, y=0, z=0, speed=60, yaw=0, mid1='m-1',retry=True).wait_for_completed()

    tl_led.set_led(r=0, g=0, b=255)

    """ *** READY TO LAND *** """
    # tl_flight.mission_pad_off()
    tl_flight.land().wait_for_completed()
    tl_drone.close()  # release the robot resources
