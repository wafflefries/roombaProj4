# Roomba Project 4
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

catkin_create_pkg Rsensor rospy

Clone Rsensor.py from github

# This takes the files from github and copies it into your Pi

cd ~/robot/src/publisher/src

curl -o Rsensor.py https://github.com/wafflefries/roombaProj4/blob/master/ros/Rsensor.py

sudo chmod u+x Rsensor.py

# Create Subscriber package

## This creates the subscriber package. The subscriber packages gets the output from the publisher package

cd ~/robot/src

catkin_create_pkg Rwheel rospy

# Clone subscriber from github

## This will copy the subscriber file from github into your pi

cd ~/robot/src/subscriber/src

curl -o Rwheel.py https://github.com/wafflefries/roombaProj4/blob/master/ros/Rwheel.py

sudo chmod u+x Rwheel.py

# Creates the navigation which is a publisher and subscriber

cd~/robot/src

catkin_create_pkg navigation rospy

Clone navigation.py from github

# Clone navigation from github

cd ~/robot/src/navigation/src

curl -o navigation.py https://github.com/wafflefries/roombaProj4/blob/master/ros/navigation.py

sudo chmod u+x navigation.py

# Now connect the Pi to Roomba using Serial cable
## Run Ros/ open the first terminal

cd ~/robot

catkin_make

source devel/setup.bash

roscore

# Run publisher

cd ~/robot

source devel/setup.bash

rosrun Rsensor Rsensor.py

# Run subscriber

cd ~/robot

source devel/setup.bash

rosrun Rwheel Rwheel.py

# Run navigation
cd ~/robot

source devel/setup.bash

rosrun navigation navigation.py

