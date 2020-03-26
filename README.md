# snowboy_ros_speech_recognition
### Overview

This is a part of a team project to recognize words using Snowboy and send the data via ROS.

It works on Jetson Nano Devkit (Ubuntu 18.04 LTS) with ROS Melodic.



### ROS connection info

Detected words are sent as a character. (e.g. the word "go" as 'w')

Default node name is voice_trans and default publisher name is voice_sound



### Requirements

1. Ubuntu 18.04 LTS on Jetson Nano Devkit
2. ROS Melodic
3. Snowboy (tested on Version: 1.3.0 (2/19/2018))



### Usage

`$python voice_trans.py`

For better word detection, you can change sensitivity by replacing sensitivity_list array value in voice_trans.py

For more information about voice recognition, check [Snowboy Github Page](https://github.com/Kitt-AI/snowboy).

⚠️ Caution: Check your ROS server IP setting before use this file.

[^1]: ROS_MASTER_URI and ROS_HOSTNAME in bash.







### Command list

| Command | Data |    Personal Model File (.pmdl)    |
| :-----: | :--: | :---------------------------: |
|   go    |  w   |  ./resources/models/go.pmdl   |
|  back   |  x   | ./resources/models/back.pmdl  |
|  left   |  a   | ./resources/models/left.pmdl  |
|  right  |  d   | ./resources/models/right.pmdl |
|  stop   |  s   | ./resources/models/stop.pmdl  |



