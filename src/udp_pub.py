#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64MultiArray
import numpy as np
import socket



UDP_IP = '192.168.50.78'
UDP_PORT = 2001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind((UDP_IP, UDP_PORT))
closeSocket = False

class RosNode:
    def __init__(self):
        rospy.init_node("ros_node")
        rospy.loginfo("Starting RosNode.")
        self.message_pub = rospy.Publisher("pub_road", Float64MultiArray, queue_size=10)
        self.rate = rospy.Rate(100)
        pass


if __name__ == "__main__":
    ros_node = RosNode()
    hearing = Float64MultiArray()

    while not rospy.is_shutdown():
        try:
            data, addr = sock.recvfrom(8192)

            if data and not closeSocket:
                rospy.loginfo("Recieving Socket Data")
                closeSocket = True

     
            data_hear = list(data.decode())

            print(data_hear)

            # ros_node.message_pub.publish(hearing)
            ros_node.rate.sleep()
            rospy.loginfo(hearing.data)
            # print(sensor_array)
        except socket.error as e:
            rospy.loginfo("RosNode and UDP Socket Shutting Down")
            sock.close()
            print(e)