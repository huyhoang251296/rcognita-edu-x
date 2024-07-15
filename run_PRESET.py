import subprocess
import numpy as np


if __name__ == "__main__":
    initial_theta = [
        0.001, np.pi, np.pi/2
    ]

    initial_position = np.array(np.meshgrid([-3, 0, 3], [-3, 0, 3])).T.reshape(-1, 2)
    N_kappa = [
        [1.5, 9, -2.5],
        [1.5, 5, -2.5],
        [1.5, 9, -1],
        [0.5, 9, -2.5]
    ]

    for kappa in N_kappa:
        for theta in initial_theta:
            for pos in initial_position:
                if not np.any(pos):
                    continue

                if 0 not in pos:
                    continue

                subprocess.check_output([
                    "python", "PRESET_3wrobot_NI.py",
                    "--ctrl_mode", "N_CTRL",
                    "--experiment", "multi_pose",
                    "--init_robot_pose_x", str(pos[0]),
                    "--init_robot_pose_y",  str(pos[1]),
                    "--init_robot_pose_theta",  str(theta),
                    "--N_kappa", "[{}, {}, {}]".format(*kappa)
                    ])
