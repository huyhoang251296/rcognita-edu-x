if [ -e './rcenv/bin/python' ]; then
    alias INTERPRETER='./rcenv/bin/python'
    INTERPRETER_P='./rcenv/bin/python'
else
    alias INTERPRETER=python3.10
    INTERPRETER_P='python3.10'
fi

INTERPRETER_P=${INTERPRETER_P} INTERPRETER main_turtlebot_ros.py \
           --ctrl_mode MPC \
           --pred_step_size_multiplier 8 \
           --Nactor 4 \
           --dt 0.2 \
           --goal_robot_pose_x 3 \
           --goal_robot_pose_y 1 \
