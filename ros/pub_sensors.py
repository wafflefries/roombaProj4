#!/usr/bin/env python
# ----------------------------------------------------------------------------
# MIT License
# shows how to get sensor data from the create 2
from __future__ import print_function
from pycreate2 import Create2
from std_msgs.msg import Int32
import rospy
import time
if __name__ == "__main__":
        rospy.init_node('topic_publisher')
        pub = rospy.Publisher('pub_sensors', Int32)
        rate = rospy.Rate(2)
        port = '/dev/ttyUSB0'
        baud = {'default': 115200}
        bot = Create2(port=port, baud=baud['default'])
        bot.start()
        bot.safe()
        print('Starting ...')
        sensor_state = [0,0,0,0,0,0]
        while True:
                # Packet 100 contains all sensor data.
                sensor_state[0] = bot.get_sensors().light_bumper_left
                sensor_state[1] = bot.get_sensors().light_bumper_front_left
                sensor_state[2] = bot.get_sensors().light_bumper_center_left
                sensor_state[3] = bot.get_sensors().light_bumper_center_right
                sensor_state[4] = bot.get_sensors().light_bumper_front_right
                sensor_state[5] = bot.get_sensors().light_bumper_right
                pub.Publisher('pub_sensors', Int32)
                rate = rospy.Rate(2)
                print('==============Updated Sensors==============')
                print(sensor_state)
                time.sleep(2)