#!/usr/bin/env python
import rospy
from rotors_comm.msg import WindSpeed

def callback(data):
    rospy.loginfo("direction x: [" + str(data.velocity.x) + "]")
    rospy.loginfo("direction y: [" + str(data.velocity.y) + "]")
    rospy.loginfo("direction z: [" + str(data.velocity.z) + "]")

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/firefly/wind_speed", WindSpeed, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()