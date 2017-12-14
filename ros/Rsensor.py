#!/usr/bin/env python
from __future__ import print_function
from pycreate2 import Create2
import time
import rospy
from std_msgs.msg import Int32MultiArray

rospy.init_node('SENSOR')
pub = rospy.Publisher('sensor_msg',Int32MultiArray)
r = rospy.Rate(2)
bot = Create2(port='/dev/ttyUSB0', baud=115200)
bot.start()
bot.full()
print('Starting ...')
ss = [0,0,0,0,0,0]
while not rospy.is_shutdown():
        ss[0] = bot.get_sensors().light_bumper_left
        ss[1] = bot.get_sensors().light_bumper_front_left
        ss[2] = bot.get_sensors().light_bumper_center_left
        ss[3] = bot.get_sensors().light_bumper_center_right
        ss[4] = bot.get_sensors().light_bumper_front_right
        ss[5] = bot.get_sensors().light_bumper_right
        s_s = Int32MultiArray(data=ss)
        pub.publish(s_s)
        r.sleep()
