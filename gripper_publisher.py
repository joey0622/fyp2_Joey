#!/usr/bin/env python3
# coding: utf-8
import Arm_Lib
import rospy
from std_msgs.msg import Float64
import time 

def gripper_publisher():
    print("start gripper")
    st = time.time()
    # Initialize the ROS node
    rospy.init_node('gripper_publisher')

    # Create the publisher object
    pub = rospy.Publisher('gripper_topic', Float64, queue_size=10)

    msg = Float64()
    angle = sbus.Arm_serial_servo_read(6)
    print("Angle=", angle)
    # Make sure the angle is not None before using it in the calculation
    if angle is not None:
        if angle <= 60.0:
            msg.data = 140.0
        elif angle > 60.0 and angle <= 180.0:
            msg.data = 30.0
    else:
        # Handle the case where the angle is None
        print("Error: Angle is not defined")
    rospy.sleep(5)
    pub.publish(msg)
    print("done publish gripper")
    et = time.time()
    elapsed_time = et-st
    print('Execution time : ',elapsed_time,'seconds')


if __name__ == '__main__':
    sbus = Arm_Lib.Arm_Device()
    try:
        gripper_publisher()
    except rospy.ROSInterruptException:
        pass

