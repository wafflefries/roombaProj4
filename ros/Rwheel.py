#!/usr/bin/env python
from __future__ import print_function
import rospy
from std_msgs.msg import Int32
from pycreate2 import Create2
import time

logic = 0

def callback(msg):
        print(msg.data)
        global logic
        logic = msg.data

#Initilize the connection with the other nodes:
rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('nav_msg', Int32, callback)

# Create a Create2 Bot
port = '/dev/ttyUSB0'  # this is the serial port on my raspberry pi
baud = {'default': 115200}
bot = Create2(port=port, baud=baud['default'])

# define a movement path

while not rospy.is_shutdown():
        # path to move
        if logic == 1:
                bot.drive_direct(-50,-50)
        elif logic == 2:
                bot.drive_direct(50,-50)
        elif logic == 3:
                bot.drive_direct(-50,50)
        elif logic == 4:
                bot.drive_direct(50,50)
        #else:
                #raise Exception('invalid movement command')
print('shutting down ... bye')
bot.drive_stop()
time.sleep(0.1)

rospy.spin()

