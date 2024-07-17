if [ -e './rcenv/bin/python' ]; then
    alias INTERPRETER='./rcenv/bin/python'
    INTERPRETER_P='./rcenv/bin/python'
else
    alias INTERPRETER=python3.10
    INTERPRETER_P='python3.10'
fi

INTERPRETER_P=${INTERPRETER_P} INTERPRETER main_turtlebot_ros.py \
        --ctrl_mode N_CTRL\
        --goal_robot_pose_x 3 \
        --goal_robot_pose_y 1 \
        --goal_robot_pose_theta 0.001 \
        --N_kappa "[0.5, 9, -2.5]"
