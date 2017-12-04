#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from __future__ import print_function
import pycreate2
import time
def callback(msg):
        print msg.data
if __name__ == "__main__":
        rospy.init_node('topic_subscriber')
        sub = rospy.Subscriber('nav_msg', Int32, callback)
        rospy.spin()
        # Create a Create2 Bot
        port = '/dev/ttyUSB0'  # this is the serial port on my raspberry pi
        baud = {'default': 115200}
        bot = pycreate2.Create2(port=port, baud=baud['default'])
        # define a movement path
        #if (msg.data == )
        path = [
                ['forward', 200, 1, 'for'],
                ['back', -200, 2, 'back'],
                ['stop', 0, 0.1, 'stop'],
                ['turn right', 100, 2, 'rite'],
                ['turn left', -100, 4, 'left'],
                ['turn right', 100, 2, 'rite'],
                ['stop', 0, 0.1, 'stop']
        ]
        bot.start()
        bot.full()
        # path to move
        for mov in path:
                name, vel, dt, string = mov
                print(name)
                bot.digit_led_ascii(string)
                if name in ['forward', 'back', 'stop']:
                        bot.drive_stright(vel)
                        time.sleep(dt)
                elif name in ['turn right', 'turn left']:
                        bot.drive_turn(vel, -1)
                else:
                        raise Exception('invalid movement command')
        print('shutting down ... bye')
        bot.drive_stop()
        time.sleep(0.1)
