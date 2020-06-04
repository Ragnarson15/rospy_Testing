#!/usr/bin/env python
from __future__ import print_function
from py_testing.srv import *
from geometry_msgs.msg import Point
import rospy

def route_volatiles(req):
    #rospy.wait_for_service('/qual_2_services/volatile_locations')
    #qual_2_volatiles = rospy.ServiceProxy('/qual_2_services/volatile_locations', VolatileLocations)
    #response = qual_2_volatiles()
    #print (response.pose)
    route = []
    for _ in range(10):
        route.append(Point(1.0, 1.0, 1.0))
    return RouteVolatilesResponse(route)

def route_volatiles_server():
    rospy.init_node('route_volatiles_server')
    #rospy.wait_for_service('/qual_2_services/volatile_locations')
    #qual_2_volatiles = ServiceProxy('/qual_2_services/volatile_locations', VolatileLocations)
    #responce = qual_2_volatiles()
    #print (responce)
    s = rospy.Service('route_volatiles', RouteVolatiles, route_volatiles)
    print ("Ready to make a route across all volatiles")
    rospy.spin()

if __name__=="__main__":
    route_volatiles_server()
