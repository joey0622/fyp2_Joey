#!/usr/bin/env python3
# coding: utf-8
from time import sleep
from math import pi
import rospy,sys
import moveit_commander
from geometry_msgs.msg import PoseStamped

from moveit_commander.move_group import MoveGroupCommander
from moveit_commander import MoveGroupCommander, PlanningSceneInterface

if __name__ == '__main__':
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node("dofbot_set_move")  
    scene = PlanningSceneInterface()
    robot = moveit_commander.RobotCommander()
    dofbot = MoveGroupCommander("dofbot")
    dofbot.set_max_velocity_scaling_factor(1)
    dofbot.set_max_acceleration_scaling_factor(1)
    dofbot.allow_replanning(True)
    dofbot.set_planning_time(5)
    dofbot.set_num_planning_attempts(10)
    dofbot.set_goal_position_tolerance(0.01)
    dofbot.set_goal_orientation_tolerance(0.01)
    dofbot.set_goal_tolerance(0.01)

    dofbot.set_named_target("up")
    dofbot.go()
    sleep(0.5)

    # We can plan a motion for this group to a desired pose for the end-effector
    target_joints1 = [-1.32, -1.13, -0.34, -1.02, 0.05]
    target_joints2 = [1.32, -1.13,-0.34, -1.02, 0.05]

    tool_size = [0.03, 0.03, 0.03]
    # get the name of end efefctor
    end_effector_link = dofbot.get_end_effector_link()
    # Setting the position of tools
    p = PoseStamped()
    p.header.frame_id = end_effector_link
    p.pose.position.x = 0
    p.pose.position.y = 0
    p.pose.position.z = 0.10
    p.pose.orientation.x = 0
    p.pose.orientation.y = 0
    p.pose.orientation.z = 0
    p.pose.orientation.w = 1

    # attach tool to the end effector
    scene.attach_box(end_effector_link, 'tool', p, tool_size)

    # get the name of the reference frame for this robot
    print (("============ Reference frame: %s") % dofbot.get_planning_frame())
    # print the name of the end-effector link for this group
    print (("============ Reference frame: %s") % dofbot.get_end_effector_link())
    # get a list of all the groups in the robot
    print ("============ Robot Groups:===============================")
    print (robot.get_group_names())
    print ("============ Printing robot state========================")
    print (robot.get_current_state())
    print ("=========================================================")

    box_ground = -0.5
    # length,width, height
    box_size = [0.15, 0.15, 0.22]
    # add table into scene
    box_pose = PoseStamped()
    box_pose.header.frame_id = 'base_link'
    box_pose.pose.position.x = -0.29
    box_pose.pose.position.y = 0.0
    box_pose.pose.position.z = box_ground+ box_size[2] / 2.0
    box_pose.pose.orientation.w = 1.0
    scene.add_box('bin', box_pose, box_size)
    rospy.sleep(0.5)
   
    print("----------------------------------------------------------")
    print("Welcome to the MoveIt Motion Planning ")
    print("----------------------------------------------------------")
    print("Press Ctrl-Z to exit at any time")
    print("")
    for i in range(2):
        # ????
        dofbot.set_joint_value_target(target_joints1)
        dofbot.go()
        sleep(0.05)
        dofbot.set_joint_value_target(target_joints2)
        dofbot.go()
        sleep(0.05)
        print("plan success")
        break
    else:
        print("plan error")
    #exit and shutdown moveit
    moveit_commander.roscpp_shutdown()
    moveit_commander.os._exit(0)
