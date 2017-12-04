#!/usr/bin/env python

import rospy

from std_msgs.msg import Int32
#define the display text
def publish_wheel(data):
    rospy.loginfo("I receive %s", data.data)
    pub = rospy.Publisher('nav_msg', Int32, queue_size=10)
    sensor_data = data.data.split()
    
    if (sensor_data[0] || sensor_data[1] || sensor_data[2]):
        if (sensor_data[3] || sensor_data[4] || sensor_data[5]):
            # need to back up
            msg.left=-1
            msg.right=-1
        else:
            # need to turn right
            msg.left=-1
            msg.right=1
    elif (sensor_data[3] || sensor_data[4] || sensor_data[5]):
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
    rospy.Subscriber('sensor_msg', String, callback)
    rospy.spin()

if __name__=='__main__':
    navigation()
