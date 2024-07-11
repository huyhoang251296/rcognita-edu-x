python3.10 main_turtlebot_ros.py \
           --ctrl_mode MPC \
           --pred_step_size_multiplier 8 \
           --Nactor 4 \
           --dt 0.2 \
           --goal_robot_pose_x 3 \
           --goal_robot_pose_y 1 \
           --distortion_enable false \
           --distortion_x 1 \
           --distortion_y 1
