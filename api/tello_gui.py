import time
from threading import Thread
from typing import Optional, Union, Type, Dict
import tkinter as tk
from .tello import Tello

class GUI:

    def __init__(self,tello):

        self.tello = tello
        self.window = tk.Tk()
        self.window.title("Controller")
        self.window.geometry("1000x500")

        # Keys: Up, Down, Left, Right, KillSwitch, Takeoff
        self.upButton = tk.Button(self.window, text="↑", command=self.move_up)
        self.upButton.grid(row=3, column=2)

        self.downButton = tk.Button(self.window, text="↓", command=self.move_down)
        self.downButton.grid(row=4, column=2)

        self.leftButton = tk.Button(self.window, text="←", command=self.move_left)
        self.leftButton.grid(row=4, column=1)

        self.rightButton = tk.Button(self.window, text="→", command=self.move_right)
        self.rightButton.grid(row=4, column=3)

        self.takeOffButton = tk.Button(self.window, text="TAKEOFF", command=self.takeoff)
        self.takeOffButton.grid(row=1, column=1)

        self.landButton = tk.Button(self.window, text="LAND", command=self.land)
        self.landButton.grid(row=1, column=6)

        self.killButton = tk.Button(self.window, text="KILL", command=self.emergency)
        self.killButton.grid(row=6, column=6)

    def takeoff(self):
        """Automatic takeoff.
        """
        # Something it takes a looooot of time to take off and return a succesful takeoff.
        # So we better wait. Otherwise, it would give us an error on the following calls.
        self.send_control_command("takeoff", timeout=self.tello.TAKEOFF_TIMEOUT)
        self.is_flying = True

    def land(self):
        """Automatic landing.
        """
        self.send_control_command("land")
        self.is_flying = False

    def emergency(self):
        """Stop all motors immediately.
        """
        self.send_command_without_return("emergency")
        self.is_flying = False

    def move(self, direction: str, x: int):
        """Tello fly up, down, left, right, forward or back with distance x cm.
        Users would normally call one of the move_x functions instead.
        Arguments:
            direction: up, down, left, right, forward or back
            x: 20-500
        """
        self.send_control_command("{} {}".format(direction, x))

    def move_up(self, x: int):
        """Fly x cm up.
        Arguments:
            x: 20-500
        """
        x = 20 # Default value
        self.move("up", x)

    def move_down(self, x: int):
        """Fly x cm down.
        Arguments:
            x: 20-500
        """
        x = 20  # Default value
        self.move("down", x)

    def move_left(self, x: int):
        """Fly x cm left.
        Arguments:
            x: 20-500
        """
        x = 20  # Default value
        self.move("left", x)

    def move_right(self, x: int):
        """Fly x cm right.
        Arguments:
            x: 20-500
        """
        x = 20  # Default value
        self.move("right", x)

    def move_forward(self, x: int):
        """Fly x cm forward.
        Arguments:
            x: 20-500
        """
        x = 20  # Default value
        self.move("forward", x)

    def move_back(self, x: int):
        """Fly x cm backwards.
        Arguments:
            x: 20-500
        """
        x = 20  # Default value
        self.move("back", x)

    def rotate_clockwise(self, x: int):
        """Rotate x degree clockwise.
        Arguments:
            x: 1-360
        """
        x = 20  # Default value
        self.send_control_command("cw {}".format(x))

    def rotate_counter_clockwise(self, x: int):
        """Rotate x degree counter-clockwise.
        Arguments:
            x: 1-3600
        """
        x = 20  # Default value
        self.send_control_command("ccw {}".format(x))