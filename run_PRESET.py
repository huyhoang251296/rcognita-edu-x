import subprocess
import numpy as np


def run_nominal_control():
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
                
def run_Stanley_control():
    ks = [0.1, 0.5, 1]
    trajectories = [
        "sine",
        "inf"
    ]
    Ls = [
        0.2,
        1
    ]
    strategy = [
        "simple", "tempo"
    ]
    
    for traj in trajectories:
        for L in Ls:
            for k in ks:
                for st in strategy:
                    # Only run strategy tempo with inf trajectory
                    if not (traj == "sine" and st == "tempo"):
                        continue

                    subprocess.check_output([
                        "python", "PRESET_3wrobot_NI.py",
                        "--ctrl_mode", "Stanley_CTRL",
                        "--experiment", "multi_pose",
                        "--t1", str(30),
                        "--init_robot_pose_x", "-1",
                        "--init_robot_pose_y",  "-1",
                        "--Stanley_L", str(L),
                        "--Stanley_k", str(k),
                        "--Stanley_traj", traj,
                        "--Stanley_strategy", str(st),
                        ])

if __name__ == "__main__":
    # run_nominal_control()
    run_Stanley_control()
