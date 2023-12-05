from pupper_controller.src.pupperv2 import pupper
import math
import time
import numpy as np
import json
from absl import app
from enum import Enum

"""doesn't work"""
class Leg(Enum):
    FRONT_RIGHT = 0
    FRONT_LEFT = 1
    BACK_RIGHT = 2
    BACK_LEFT = 3

def record_joint_angles():
    pup = pupper.Pupper(run_on_robot=True,
                        plane_tilt=0)

    # print("Deactivating motors") 
    pup.hardware_interface.deactivate()
    # pup.hardware_interface.activate()
    # pup.hardware_interface.home_motors()
    # # pup.hardware_interface.activate()

    # time.sleep(5)
    # pup.slow_stand()
    # pup.hardware_interface.deactivate_leg(0)
    # print("Deactivated")

    file_name = input("Enter a file name to save your recordings to: ")
    f = open("joint_pos/" + file_name, 'w')

    positions = []
    try:
        key_press = ""
        while key_press != "q":
            key_press = input("Hit enter to record joint positions: ")
            
            joint_angles = pup.get_observation()[-12:]

            print(joint_angles)
            positions.append(list(joint_angles))
    finally:
        f.write(json.dumps(positions))
        f.close()
        pass

def go_to_pos(filename):
    pup = pupper.Pupper(run_on_robot=True,
                        plane_tilt=0)
    pup.hardware_interface.deactivate()
    pup.hardware_interface.activate()
    time.sleep(0.1)
    pup.hardware_interface.home_motors()
    time.sleep(5)

    f = open(filename)
    positions = json.load(f)

    for x in range(3):
        for pos in positions:
            pup.hardware_interface.set_actuator_postions(np.array(pos["position"]))
            time.sleep(pos["duration"])
    
    pup.hardware_interface.deactivate()

def main(_):
    go_to_pos("joint_pos/stepout2")
    # record_joint_angles()

app.run(main)   
