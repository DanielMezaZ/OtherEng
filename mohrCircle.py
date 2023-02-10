# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 21:29:44 2023

@author: jesus
"""
import matplotlib.pyplot as mpl
import numpy as np

mpl.gca().set_aspect('equal')

[s11,s12,s22]=[3.00,0.00,1.00]
n=-45
theta=np.pi/180*n

sigma=np.array([[s11,s12],[s12,s22]])

mpl.scatter(s11, s12,s=100,label="(s11 , s12 )")
mpl.scatter(s22,-s12,s=100,label="(s22 ,-s12 )")
mpl.plot([s11,s22],[s12,-s12],c="blue")
mpl.xlabel("sigma")
mpl.ylabel("tau")

c=(s11+s22)/2
mpl.scatter(c,0,c="black")
r=(s22-s11)**2+(2*s12)**2
r=np.sqrt(r)/2
mpl.scatter(c+r,0,c="black")
mpl.scatter(c-r,0,c="black")

mpl.ylim(-1.1*r,1.1*r)
mpl.xlim(c-1.1*np.abs(r),c+1.1*np.abs(r))
mpl.plot([0,0],[-1.1*r,1.1*r],"--k",linewidth=0.5)
mpl.plot([c-1.1*np.abs(r),c+1.1*np.abs(r)],[0,0],"--k",linewidth=0.5)

t=np.linspace(0,2*np.pi,180)
X=c+r*np.cos(t)
Y=r*np.sin(t)
mpl.plot(X,Y,"--k")

d=(s11-s22)/2
s11_=c+d*np.cos(2*theta)+s12*np.sin(2*theta)
s22_=c-d*np.cos(2*theta)-s12*np.sin(2*theta)
s12_=-d*np.sin(2*theta)+s12*np.cos(2*theta)
if s22==c:
    phi=np.pi/2
else:
    phi=np.arctan(-s12/(s22-c))

[s11,s12,s22]=[s11_,s12_,s22_]
mpl.scatter(s11, s12,s=100,label="(s11´, s12´)")
mpl.scatter(s22,-s12,s=100,label="(s22´,-s12´)")
mpl.plot([s11,s22],[s12,-s12],c="red")

t=np.linspace(phi,phi-2*theta,np.abs(n))
X=c+r*np.cos(t)
Y=r*np.sin(t)
mpl.plot(X,Y,"-r",linewidth=2)
t=np.linspace(np.pi+phi,np.pi+phi-2*theta,np.abs(n))
X=c+r*np.cos(t)
Y=r*np.sin(t)
mpl.plot(X,Y,"-r",linewidth=2)

mpl.legend()