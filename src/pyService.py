#!/usr/bin/env python
import rospy
from rospy_Testing.srv import *

rospy.init_node('test_service_call')
rospy.wait_for_service('/qual_2_services/volatile_locations')
qual_2_volitiles = rospy.ServiceProxy('/qual_2_services/volatile_locations', qual_2_volatiles_srv)
responce = qual_2_volitiles()
print (response)
rospy.spin()
