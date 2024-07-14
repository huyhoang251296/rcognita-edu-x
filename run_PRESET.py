import subprocess
import numpy as np


if __name__ == "__main__":
    initial_theta = [
        0.001, np.pi, np.pi/2
    ]

    initial_position = np.array(np.meshgrid([-3, 0, 3], [-3, 0, 3])).T.reshape(-1, 2) 

    for theta in initial_theta:
        for pos in initial_position:
            if not np.all(pos):
                continue

            subprocess.check_output([
                "python", "PRESET_3wrobot_NI.py",
                "--ctrl_mode", "N_CTRL",
                "--experiment", "Nominal_multi_pos",
                "--init_robot_pose_x", str(pos[0]),
                "--init_robot_pose_y",  str(pos[1]),
                "--init_robot_pose_theta",  str(theta),
                ])
