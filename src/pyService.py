#!/usr/bin/env python
import rospy

rospy.wait_for_service('/qual_2_services/volatile_locations')
qual_2_volitiles = rospy.ServiceProxy('/qual_2_services/volatile_locations', qual_2_volatiles_srv)
responce = qual_2_volitiles()
print (response)
