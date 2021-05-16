import matplotlib.pyplot as plt
import numpy as np
# Track Name from Tracks List
track_name = input("Track Name :")
show_xy = input("Enter the number of the position 1.center 2.inside 3.outside :")
show_xy = int(show_xy)

absolute_path = "."

waypoints = np.load("%s/tracks/%s.npy" % (absolute_path, track_name))

print("Number of waypoints = " + str(waypoints.shape[0]))

for i,point in enumerate(waypoints):
    center_xy = [point[0],point[1]] 
    inside_xy = [point[2],point[3]] 
    outside_xy = [point[4],point[5]] 

    plt.scatter(center_xy[0], center_xy[1])
    plt.scatter(inside_xy[0], inside_xy[1])
    plt.scatter(outside_xy[0], outside_xy[1])

    if show_xy == 1 :
        xy = [round(i, 8) for i in center_xy]
        print(xy)
    elif show_xy == 2 :
        xy = [round(i, 8) for i in inside_xy]
        print(xy)
    elif show_xy == 3 :
        xy = [round(i, 8) for i in outside_xy]
        print(xy)
    elif show_xy != 1 or show_xy != 2 or show_xy != 3:
        print("Invalid number")
        break

#plt.show()