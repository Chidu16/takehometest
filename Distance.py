from numpy import arccos
from math import radians, sin, cos


# Function to calculate and return the distance between the company and the customer
# based on their latitudes and longitudes

def distance(lat,lon):

    # radius of earth in KM
    rad_earth = 6371

    # latitude and longitude of Dublin office converted to radians
    lat_intercom = radians(53.339428)
    lon_intercom = radians(-6.257664)

    #latitude and longitude of customers converted to radian
    lat_cust = radians(lat)
    lon_cust = radians(lon)

    try:
        #calculating the central angle between office and customer location
        lon_diff = abs((lon_intercom-lon_cust))
        central_angle = arccos((sin(lat_intercom)*sin(lat_cust))+ (cos(lat_intercom)*cos(lat_cust)*cos(lon_diff)))

        #calculating the actual distance
        act_dist = rad_earth*central_angle

    except ValueError:
        print("Kindly check the Latitude and Longitude values")

    return act_dist



