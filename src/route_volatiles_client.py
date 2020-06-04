#!/usr/bin/env python
from __future__ import print_function
from py_testing.srv import *
import rospy

def route_volatiles_client():
    #rospy.init_node('route_volatiles_client')
    rospy.wait_for_service('/qual_2_services/volatile_locations')
    rospy.wait_for_service('/route_volatiles')
    # test = rospy.ServiceProxy('/route_volatiles', RouteVolatiles)
    # response = test()
    # print (response)
    #try:
    qual_2_volatiles = rospy.ServiceProxy('/qual_2_services/volatile_locations', VolatileLocations)
    response = qual_2_volatiles()
    print (response)
    #except rospy.ServiceException as e:
    #    print  ("Service call failed: %s" % e)
    #rospy.spin()
    print ("Success")

if __name__=="__main__":
    route_volatiles_client()
