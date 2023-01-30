#!/usr/bin/env python3
# coding: utf-8
import time 
from time import sleep
import rospy
from moveit_commander.move_group import MoveGroupCommander
#import Arm_Lib
from Arm_Lib import Arm_Device
from signal import pthread_kill, SIGTSTP
from math import pi
from sensor_msgs.msg import JointState
from std_msgs.msg import String, Float64
import threading, time

RA2DE = 180 / pi


def topic(msg):
   
    if not isinstance(msg, JointState): return
    #90 is open, 180 is close
    joints = [0.0, 0.0, 0.0, 0.0, 0.0, 30.0]
   
    for i in range(5): joints[i] = (msg.position[i] * RA2DE) + 90
  
    sbus.Arm_serial_servo_write6_array(joints, 1000)

def move_right():
    print("search to right")
    dofbot.set_joint_value_target([1.49, 0.42, -1.57, -1.57, -0.00])
    dofbot.go()
    sleep(0.5)


if __name__ == '__main__':

    rospy.init_node("dofbot_set_move_right")
    
    dofbot = MoveGroupCommander("dofbot")
    
    dofbot.allow_replanning(True)
    
    dofbot.set_planning_time(5)
   
    dofbot.set_num_planning_attempts(10)
  
    dofbot.set_goal_position_tolerance(0.01)
  
    dofbot.set_goal_orientation_tolerance(0.01)
  
    dofbot.set_goal_tolerance(0.01)
    
    dofbot.set_max_velocity_scaling_factor(1)
  
    dofbot.set_max_acceleration_scaling_factor(1)
    
    sbus = Arm_Device()
    time.sleep(.1)
    rospy.Subscriber("/joint_states", JointState, topic)
    move_right()
    rospy.spin()
    
