from pupper_controller.src.pupperv2 import pupper
pup = pupper.Pupper(run_on_robot=True,
                    plane_tilt=0)

print("Deactivating motors") 
pup.hardware_interface.deactivate()