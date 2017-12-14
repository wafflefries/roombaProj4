# roombaProj4

## CntrollingRoombaUsingPi
This is to control the Roomba using the Serial port connected through the Raspberry Pi 3

For the Raspberry Pi 3 you have to download Ubuntu Mate image through Google. Download a file SD card formatter.

https://www.sdcard.org/downloads/formatter_4/eula_windows/index.html

Use this formatter software to mount this image on the Micro

SD card. This is a huge image about 4 GB. For windows users you will have to download a software call Putty . This program is used to

interact with the Pi 3 using a USB to GPIO pin on the Pi 3.

The detail instructions can be found here. https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/overview

Connect your pi to your pc. Use the device manager to find out which port the pi is connected to. Open up Putty and click serial. Type the

port into serial line. Type 115200 for speed. Press open . This will open up a terminal for you to interact with the Pi . Type in your

username and password. default is pi for username and raspberry for password. You will now need to install ROS .Instruction for this can be found at http://wiki.ros.org/Installation/UbuntuARM

Click kinetic and follow the instructions to download ROS.

You will now need to install the pycreate2 for python.

https://pypi.python.org/pypi/pycreate2/0.7.3

After you hvae pycreate 2 installed you can now interact with the Roomba using the serial port through the pi 3.

This package will use subscriber and publisher nodes to pull the IR readings from the Roomba and display it on screen .

# Working with ROS
## Enter the following into terminal

This will update your pi

sudo apt-get update

sudo apt-get upgrade

sudo apt-get install git

# Now create a workspace

This will create a workspace where we will be working in

mkdir -p /robot/src

cd~/robot

catkin_init_workspace

catkin_make

source devel/setup.bash

# Create a publisher package

## This create a publisher package that will publish the sensors data out

cd~/robot/src

catkin_create_pkg publisher rospy

Clone publisher.py from github

# This takes the files from github and copies it into your Pi

cd ~/robot/src/publisher/src

curl -o publisher.py https://github.com/minh215/ControllingRoombaUsingPi/blob/master/publisher.py

sudo chmod u+x publisher.py

# Create Subscriber package

## This creates the subscirber package. The subscriber packages gets the output from the publisher package

cd ~/robot/src

catkin_create_pkg subscriber rospy

# Clone subscriber from github

## This will copy the subscriber file from github into your pi

cd ~/robot/src/subscriber/src

curl -o subscriber.py https://github.com/minh215/ControllingRoombaUsingPi/blob/master/subscriber.py

sudo chmod u+x subscriber.py

# Now connect the Pi to Roomba using Serial cable
## Run Ros/ open the first terminal

cd ~/robot

catkin_make

source devel/setup.bash

roscore

# Run publisher/ open a second terminal

cd ~/robot

source devel/setup.bash

rosrun publisher publisher.py

# Run subscriber/ Open a third terminal

cd ~/robot

source devel/setup.bash

rosrun subscriber subscriber.py

# Run navigation
cd ~/robot

source devel/setup.bash

rosrun navigation navigation.py

