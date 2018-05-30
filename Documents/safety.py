#!/usr/bin/env python

'''
Author: Edgar LV
30/05/2018

'''
import rospy
import numpy as np
from ackermann_msgs.msg import AckermannDriveStamped
from sensor_msgs.msg import LaserScan 
 

class Safety_Node:
    def __init__(self):
        # subscribe to Ackermann
        rospy.Subscriber("ackermann_cmd_mux/output", AckermannDriveStamped,self.ackermann_cmd_input_callback)
        rospy.Subscriber("/scan", LaserScan, self.laser_callback)
 
        # publish to Ackermann
        self.cmd_pub = rospy.Publisher('/vesc/ackermann_cmd_mux/input/safety', AckermannDriveStamped, queue_size = 10)

        self.drive = True
        self.min_distance = 0.35 #meters
        #self.angle_range = 45*np.pi/180 #setting 45 degrees to look up front, turning them to rads
    
    def laser_callback(self,msg):
        #Read from a specific set fo laser shots
        ranges = msg.ranges
        #get average
        average = 0
        counter = 0
        for i in range(len(ranges)-600, len(ranges)-400):
            counter += 1
            average += ranges[i]
        average /= counter

        #If average reading from a set of front laser is equal or less to min_distance:
        if average < self.min_distance:
            self.drive = False
            print ranges[540]
            self.ackermann_cmd_input_callback(AckermannDriveStamped())
        

    def ackermann_cmd_input_callback(self, msg):
        if self.drive == False:
            msg.header.stamp = rospy.Time.now()
            msg.drive.speed = -.1
            msg.drive.acceleration = -1.5
            msg.drive.steering_angle = 0.0
            print "stop"
            self.cmd_pub.publish(msg)
            rospy.Time
            msg.drive.speed = -0.000000001
            self.cmd_pub.publish(msg)
        else:
            print "safe"
             
 
if __name__ == "__main__":
    rospy.init_node("safety_controller")
    node = Safety_Node()
rospy.spin()