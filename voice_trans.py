#!/usr/bin/env python

'''
A python code for detecting sound and sending mapped command
The original code is demo.py in Snowboy installation file.
'''


import snowboydecoder
import sys
import signal
import rospy
import tty
from std_msgs.msg import String

##Pmdl file location
pmdl_go="./resources/models/go.pmdl"
pmdl_back="./resources/models/back.pmdl"
pmdl_left="./resources/models/left.pmdl"
pmdl_right="./resources/models/right.pmdl"
pmdl_stop="./resources/models/stop.pmdl"

interrupted = False
data_box ="" #A temp variable to send via rospy

'''
data_box value
w : Going forward
a : Going left
d : Going right
x : Going backward
s : Stop current action
'''

def go():
    global data_box
    data_box='w'
    print("go")
    pub.publish(data_box)

def back():
    global data_box
    data_box='x'
    print("back")
    pub.publish(data_box)

def left():
    global data_box
    data_box='a'
    print("left")
    pub.publish(data_box)

def right():
    global data_box
    data_box='d'
    print("right")
    pub.publish(data_box)

def stop():
    global data_box
    data_box='s'
    print("stop")
    pub.publish(data_box)



def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

##Ros_init start
pub = rospy.Publisher('voice_sound',String,queue_size=10)
rospy.init_node('voice_trans', anonymous = True)

##Ros_init end

callbacks = [go, back, left, right, stop] ##Command execution list


model = [pmdl_go, pmdl_back, pmdl_left, pmdl_right, pmdl_stop] ##Detect file list the order are matched with the callback list

sensitivity_list = [0.5, 0.6, 0.6, 0.55, 0.5] #Sensitivity options for each detection file

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=sensitivity_list)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()

