#A53307224
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def TD_point_south(x,y):
    z =  -(x**2 + y**2 - 1)/(x**2 + y**2 + 1)
    new_x = x*z + x
    new_y = y*z + y
    return new_x, new_y, z

def TD_point_north(x,y):
    z =  (x**2 + y**2 - 1)/(x**2 + y**2 + 1)
    new_x = -x*z + x
    new_y = -y*z + y
    return new_x, new_y, z

def main():
    start = [0,0,1]
    end = [0,0,-1]
    w = [-1,0,0]
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    # Data for three-dimensional scattered points
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = np.cos(u)*np.sin(v)
    y = np.sin(u)*np.sin(v)
    z = np.cos(v)
    ax.plot_wireframe(x, y, z, color="w")
    ax.scatter(start[0], start[1], start[2], color="g", s=100)
    ax.scatter(end[0], end[1], end[2], color="g", s=100)
    ax.scatter(w[0], w[1], w[2], color="g", s=100)
    # Draw trajecroty
    x = np.linspace(0,0,50)
    y = np.linspace(0,-1,50)
    for i in zip(x,y):
        new_x, new_y, z = TD_point_south(i[0],i[1])
        ax.scatter(new_x, new_y, z, color="r", s=50)
    x = np.linspace(0,-1,50)
    y = -np.sqrt(1-x**2)
    for i in zip(x,y):
        new_x, new_y, z = TD_point_south(i[0],i[1])
        ax.scatter(new_x, new_y, z, color="r", s=50)
    x = np.linspace(-1,0,50)
    y = -np.sqrt(1-x**2)
    for i in zip(x,y):
        new_x, new_y, z = TD_point_north(i[0],i[1])
        ax.scatter(new_x, new_y, z, color="r", s=50)
    x = np.linspace(0,0,50)
    y = np.linspace(-1,0,50)
    for i in zip(x,y):
        new_x, new_y, z = TD_point_north(i[0],i[1])
        ax.scatter(new_x, new_y, z, color="r", s=50)
    plt.show()

if __name__ == '__main__':
    main()
    
