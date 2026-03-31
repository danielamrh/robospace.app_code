# PD Controller example
import numpy as np
import time

def pd_controller(target, kp=10.0, kd=1.0):
    qpos = get_qpos()
    qvel = get_qvel()
    n = get_num_actuators()
    
    # Calculate errors
    pos_error = np.array(target) - qpos[:n]
    vel_error = -qvel[:n]
    
    # PD control law
    control = kp * pos_error + kd * vel_error
    set_control(control.tolist())
    
    return np.linalg.norm(pos_error)

target_pos = [1.0, -0.5, 0.5, 0.0, 0.0, 0.0]

while True:
    # Call the function and pass your target list
    error_magnitude = pd_controller(target=target_pos, kp=50.0, kd=5.0)

    step()
    
    # Stop the loop when the robot is close enough to the target
    if error_magnitude < 0.01:
        print("Target reached successfully!")
        break 
      
    time.sleep(0.01)

