#!/usr/bin/env python3
# coding: utf-8

import Arm_Lib
import rospy
from std_msgs.msg import Float64


def gripper_callback(msg):
    # Access the gripper position from the received message
    # open 60.0, close 150.0
    gripper_position = msg.data
   # Print the value of gripper_position
    print("Gripper position: {}".format(gripper_position))

    # Set the gripper position
    sbus.Arm_serial_servo_write(6, gripper_position, 1000)
    

def gripper_subscriber():
    # Initialize the ROS node
    rospy.init_node('gripper_subscriber')

    # Create the subscriber object
    sub = rospy.Subscriber('gripper_topic', Float64, gripper_callback)

    # Spin to keep the node running
    rospy.spin()


if __name__ == '__main__':
    sbus = Arm_Lib.Arm_Device()
    gripper_subscriber()
    
  
