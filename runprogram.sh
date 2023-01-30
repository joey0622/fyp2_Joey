#!/bin/bash
#roslaunch usb_cam usb_cam-test.launch &
#sleep 20
#roslaunch dofbot_moveit yolov5.launch &
#to increase sleep time during exact detection
#sleep 100
#echo "done garbage detection" &
#rosnode kill detect &
#rosnode kill usb_cam &
#rosnode kill image_view &
#sleep 15
roslaunch dofbot_config demo.launch &
sleep 260
echo "publish result" &
rosrun dofbot_moveit publish_result.py &
echo "start movement subscriber"
rosrun dofbot_moveit combpub_subsgrip.py &
#rosrun dofbot_moveit 06_try_move.py &
#echo "06_try_move end"
sleep 180
rosnode kill dofbot_set_move
rosnode kill garbage_node
#pkill -f "combpub_subsgrip.py" 
#pkill -f "publish_result.py"
sleep 30
#echo "wait end"
rosrun dofbot_moveit gripper_publisher.py &
rosrun dofbot_moveit gripper_subscriber.py & 
sleep 60
pkill -f "gripper_publisher.py"
pkill -f "gripper_subscriber.py"
sleep 60
#echo "killed gripper"
rosrun dofbot_moveit Classif_garbage.py
sleep 120
pkill -f "Classif_garbage.py"
rosrun dofbot_moveit gripper_publisher.py &
rosrun dofbot_moveit gripper_subscriber.py 
##trap - SIGINT
pkill -f "gripper_publisher.py"
pkill -f "gripper_subscriber.py"
echo "killed gripper"
rosnode kill -a
killall --exact rosrun
killall --exact roscore
killall --exact python
echo "program end"
