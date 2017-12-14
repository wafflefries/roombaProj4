#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Int32

s = [0,0,0,0,0,0]
logic = 0
x = 200

def callback(msg):
        print msg.data
        #Display the message received:
        global s,logic,x
        s = msg.data


#Define the name of the node:
rospy.init_node('navigator',anonymous=True)

#define the subscriber and publisher:
rospy.Subscriber('sensor_msg', Int32MultiArray,callback)
pub = rospy.Publisher('nav_msg', Int32, queue_size=10)
rate = rospy.Rate(2)

#define the trigger point for the IR sensors:

#The logic to control the Roomba:
while not rospy.is_shutdown():
        if s[0]>x and s[1]>x and s[2]>x and s[3]>x and s[4]>x and s[5]>x:
                # back up
                logic = 1
                pub.publish(logic)
        if s[0]>x and s[1]>x and s[2]>x:
                # need to turn right
                logic = 3
                pub.publish(logic)
        elif s[3]>x and s[4]>x and s[5]>x:
                # need to turn left
                locig = 2
                pub.publish(logic)
        else:
                # go straight
                logic = 4
                pub.publish(logic)


if __name__ == '__main__':
       try:
           navigator()
       except rospy.ROSInterruptException:
           pass
rospy.spin()
