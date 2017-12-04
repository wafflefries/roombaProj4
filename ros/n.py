#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Int32

#define the display text
def publish_wheel(data):
        rospy.loginfo("I receive %s", data.data)
        pub = rospy.Publisher('nav_msg', Int32, queue_size=10)
        s = data.data.split()
        x = 250
        if (s[0]>x or s[1]>x or s[2]>x):
                if (s[3]>x or s[4]>x or s[5]>x):
                        # back up
                        msg.left=-1
                        msg.right=-1
                else:
                        # need to turn right
                        msg.left=-1
                        msg.right=1
        elif (s[3]>x or s[4]>x or s[5]>x):
                # need to turn left
                msg.left=1
                msg.right=-1
        else:
                # go straight
                msg.left=1
                msg.right=1
        while not rospy.is_shutdown():
                pub.publish(msg)
#define the subscriber
def navigation():
        rospy.init_node('navigator')
        rospy.Subscriber('sensor_msg', Int32MultiArray)
        rospy.spin()

if __name__=='__main__':
        navigation()
