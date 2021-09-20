#! /usr/bin/env python3

import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import PointCloud2
from sensor_msgs.point_cloud2 import create_cloud_xyz32

def fake_pub():
    pub = rospy.Publisher('pointcloud', PointCloud2, queue_size=10)
    rospy.init_node('fake_pointcloud2_pub', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        header = Header()
        header.frame_id = "map"
        header.stamp = rospy.Time.now()
        points = [[2,0,0],[2,0.2,1],[2,0.4,2],[2,0.6,3]]
        pcl_msg = create_cloud_xyz32(header, points)
        pub.publish(pcl_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        fake_pub()
    except rospy.ROSInterruptException:
        pass