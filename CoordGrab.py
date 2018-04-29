# Copyright Google Inc. 2010 All Rights Reserved
# Main was all me; getElevation is essentially all Google.
# Honestly not compltely sure what's going on in getElevation
# but I gutted it so it gives the desired output.

import simplejson
import urllib

ELEVATION_BASE_URL = 'http://maps.google.com/maps/api/elevation/json'

def getElevation(path="47.6062, -122.3321|34.0522, -118.2437",samples="2",sensor="false", **elvtn_args):
    elvtn_args.update({
        'path': path,
        'samples': samples,
        'sensor': sensor
    })

    url = ELEVATION_BASE_URL + '?' + urllib.urlencode(elvtn_args)
    response = simplejson.load(urllib.urlopen(url))

    # Create a dictionary for each results[] object
    elevationArray = []
    
    for resultset in response['results']:
        elevationArray.append(resultset['elevation'])
        return resultset['elevation']

if __name__ == '__main__':
        
    # Collect the Latitude/Longitude input string from the user
    print("This program takes start coordinates, end coordinates,")
    print("and a number of intermediate points and prints out the")
    print("elevations (in meters) of the start, end, and each")
    print("evenly-spaced intermediate point along a straight path.")

    print("Input coordinates in the format: latitude longitude")
    startLat, startLon = raw_input("Start coordinate: ").split()
    startLat = float(startLat)
    startLon = float(startLon)
    endLat, endLon = raw_input("End coordinate: ").split()
    endLat = float(endLat)
    endLon = float(endLon)
    midpoints = int(raw_input("Number of intermediate points: "))

    # Calculate istance between each point
    latSeg = (endLat - startLat) / (midpoints + 1)
    lonSeg = (endLon - startLon) / (midpoints + 1)

    # Print start point data
    pointStr = str(startLat) + ", " + str(startLon)
    pathStr = pointStr + "|" + pointStr
    print("(" + pointStr + ") : " + str(getElevation(pathStr)))
    
    # Print intermediate point data
    i = 1
    while (i < midpoints + 1):
        tempLat = startLat + i*latSeg
        tempLon = startLon + i*lonSeg
        pointStr = str(tempLat) + ", " + str(tempLon)
        pathStr = pointStr + "|" + pointStr
        print("(" + pointStr + ") : " + str(getElevation(pathStr)))
        i = i+1

    #Print end point data
    pointStr = str(endLat) + ", " + str(endLon)
    pathStr = pointStr + "|" + pointStr
    print("(" + pointStr + ") : " + str(getElevation(pathStr)))

    ### Backup code for invalid input
    # if not startStr:
    #   startStr = "47.6062, -122.3321"
    # if not endStr:
    #   endStr = "34.0522, -118.2437"
    # if not countStr:
    #     countStr = "0"
    # count = int(countStr)

    ### Example input (Locations in Seattle & LA)
    # 47.6062 -122.3321
    # 34.0522 -118.2437