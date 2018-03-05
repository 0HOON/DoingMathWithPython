##Draw a graph of projectile motion of a ball

import matplotlib.pyplot as plt
import math

def draw_graph(x,y):
    plt.plot(x,y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')

def frange(start, stop, step):
    numbers= []

    while start < stop:
        numbers.append(start)
        start = start + step
    
    return numbers

def draw_trajectory(u, theta):
    
    theta = math.radians(theta)
    g = 9.8

    t_flight = 2*u*math.sin(theta)/g

    intervals = frange(0, t_flight, 0.001)

    x = []
    y = []

    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)

    draw_graph(x,y)

if __name__ == '__main__':
    try:
        u = float(input('Enter the initial velocity (m/s): '))
        theta =float(input('Enter the angle of projection (degrees): '))
    except ValueError:
        print('You entered an invalid input')
    else:
        draw_trajectory(u,theta)
        plt.show()

"""
three trajectories

if __name__ == '__main__':
    angles = [30,45,60]
    u = 25

    for ang in angles:
        draw_trajectory(u,ang)
    
    plt.legend(angles)

    plt.show()
"""