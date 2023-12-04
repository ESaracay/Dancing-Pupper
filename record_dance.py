from pupper_controller.src.pupperv2 import pupper
import math
import time
from absl import app

SAMPLES_EVERY_N_SECS = 1

def record_joint_angles():
    pup = pupper.Pupper(run_on_robot=True,
                        plane_tilt=0)

    print("Deactivating motors") 
    pup.hardware_interface.deactivate_servos(pup.hardware_interface.pi, pup.hardware_interface.pwm_params)

    file_name = input("Enter a file name to save your recordings to")
    f = open(file_name, 'w')

    try:
        key_press = input("Hit enter to record joint positions")
        while True:
            sleep(SAMPLES_EVERY_N_SECS)

            observation = pup.get_observation()

            print(leg_observation)
    finally:
        f.close()
        pass

def main(_):
    record_joint_angles()

app.run(main)   
