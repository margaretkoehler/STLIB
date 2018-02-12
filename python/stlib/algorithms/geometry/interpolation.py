# -*- coding: utf-8 -*-
import numpy as np
import math

def sampleLinearSegments(waypoints, minDistance):
    """
    Adds points along the line segments defined by the waypoints. Waypoints are always included in the interpolation.

    E.g.: .___________________._____. with min distance ____ becomes
          .____.____.____.____.__.__.

    Args:
        waypoints (list vec3f): Ordered list of points defining the segments.

        minDistance (float): Minimum allowed distance between points in the interpolation.

    Return:
        (list vec3f): sampled points

    Structure:
        (none)
    """
    points = [waypoints[0]]
    for i in range(1,len(waypoints)):
        point0 = np.array(waypoints[i-1])
        point1 = np.array(waypoints[i])
        dist = np.linalg.norm(point1-point0)
        unit = (point1-point0)/dist
        numSegments = math.ceil(dist/minDistance)
        dist = dist/numSegments
        for j in range(0,int(numSegments)):
            point1 = point0+dist*unit
            points.append(point1.tolist())
            point0 = point1
    return points
 
