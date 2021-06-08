from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import random
import plotly.express as px
from random import *
import plotly.express as px
import math

#double-slit



rslit = int(input("\n enter the distance of slits from source:"))
rscr = int(input("\n enter the distance  of screen from source:"))

particles = int(input(("\n enter the no of particles:")))

radius = []
thetaangle = []
phiangle = []

r = 0
x = []
y = []
z = []
for n in range(0, particles + 1):
    r = 0
    for i in np.arange(0, rscr + 1, 1):
        r = i
        if r < rslit:
            theta = 0
            phi = 0
        elif r >= rslit:
            ran = randint(1, 10)
            if ran % 2 == 0:
                phi = 10
                theta = 0
                radius.append(r)
                y.append(r * math.sin(math.radians(phi)))
                z.append(r * math.cos(math.radians(theta)))
            elif ran % 2 != 0:
                theta =0
                phi = -10
                radius.append(r)
                y.append(r * math.sin(math.radians(phi)))
                z.append(r * math.cos(math.radians(theta)))



            rn = randint(1, 7)
            if rn == 1:
                theta = randint(-70, 70)
                phi = randint(-70, -60)
            if rn == 2:
                theta = randint(-70, 70)
                phi = randint(-50, -40)
            if rn == 3:
                theta = randint(-70, 70)
                phi = randint(-30, -20)
            if rn == 4:
                theta = randint(-70, 70)
                phi = randint(-5, 5)
            if rn == 5:
                theta = randint(-70, 70)
                phi = randint(20, 30)
            if rn == 6:
                theta = randint(-70, 70)
                phi = randint(40, 50)
            if rn == 7:
                theta = randint(-70, 70)
                phi = randint(60, 70)
        radius.append(r)
        thetaangle.append(theta)

        phiangle.append(phi)
        y.append(r * math.sin(math.radians(phi)))
        z.append(r * math.cos(math.radians(theta)))
time=[]
for i in np.arange(0,len(radius),1):
    time.append(i)

print("radius\n")
print(radius)
print("theta\n")
print(thetaangle)
print("phi\n")
print(phiangle)
fig = px.scatter_3d(x=radius,y= y,z= z,title='double-slit-experiment', height=800)
fig.update_traces(marker_size=2)
fig.write_html("double_slit.html")
print("figure saved ")
print(len(radius))




print("done")














