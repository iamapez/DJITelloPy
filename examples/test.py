import time

import robomaster.config
from robomaster import robot

# robomaster.config.LOCAL_IP_STR = "192.168.2.20"

if __name__ == '__main__':

    # https://dl.djicdn.com/downloads/RoboMaster+TT/Tello_SDK_3.0_User_Guide_en.pdf

    """ *** POPULATE OBJECTS HERE *** """
    tl_drone = robot.Drone()  # instance of the Drone class
    tl_drone.initialize()  # Initialize the robot object. Currently, no input parameters are required for the initialization of education-series drones.

    tl_flight = tl_drone.flight  # Use the get_module() method of the Drone object to obtain the specified object.
    tl_led = tl_drone.led

    drone_battery_threshold = 20
    travel_height = 37

    """ *** PRINT ANY INFORMATION YOU WANT ABOUT THE DRONE BEFORE THE FLIGHT HERE *** """
    # get the sdk version running on the drone
    drone_version = tl_drone.get_sdk_version()
    print("Drone sdk version: {0}".format(drone_version))

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
    user_instruction = 0

    while user_instruction != 3:
        print('=== Flight Controls Menu ===')
        print("""
            1.) Hover 
            2.) Pre-determined map
            3.) Exit
        """)

        tl_led.set_led(0, g=0, b=0)
        tl_flight.takeoff().wait_for_completed()
        user_instruction = int(input('Enter the drone instruction number:'))

        if user_instruction == 1:
            time.sleep(5)
            counter = 0
            start_time = time.time()
            print('Entering while loop')
            while 1:
                baro = tl_drone.get_baro()
                if baro < travel_height:
                    diff = travel_height - baro
                    tl_flight.up(distance=diff).wait_for_completed()
                    time.sleep(2)
                    diff = baro - travel_height
                    tl_flight.down(distance=diff).wait_for_completed()
                    time.sleep(2)
                else:
                    time.sleep(2)

                if counter == 15:
                    print("--- %s seconds ---" % (time.time() - start_time))
                    break

                counter += 1
        elif user_instruction == 2:
            print('execute pre-determined path')
        else:
            print('breaking!')
            break

    print('FINAL baro:', tl_drone.get_baro())

    # tl_flight.forward(distance=25).wait_for_completed()
    tl_led.set_led(r=255, g=0, b=0)

    """ *** READY TO LAND *** """
    tl_flight.land().wait_for_completed()
    tl_drone.close()  # release the robot resources
