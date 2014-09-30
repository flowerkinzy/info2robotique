# -*- coding: utf-8 -*-
"""
Telemetry
"""

from sympy.geometry import Polygon,Line,Point,intersection
from sympy import N
import turtle
import random
from math import *
import numpy as np
import matplotlib.pyplot as plt
import time

def new_box(x,y,c):
    V = turtle.Turtle()
    V.hideturtle(); V.penup()
    V.setpos(x-c/2,y-c/2); V.setheading(0) ; V.pendown()
    for i in range(4):
        V.fd(c)
        V.left(90)
    return Polygon(Point(x-c/2,y-c/2),Point(x-c/2,y+c/2),Point(x+c/2,y+c/2),Point(x+c/2,y-c/2))

def telemetry(T,boxelist):
    a = radians(T.heading())
    P1,P2 = Point(T.xcor(),T.ycor()) , Point(T.xcor()+cos(a),T.ycor()+sin(a))
    P12 = P2 - P1
    intr = [N(P12.dot(p-P1)) for r in boxelist for p in intersection(Line(P1,P2),r) ]
    intr = [d for d in intr if d >= 0]
    #print intr
    return None if intr==[] else (min(intr)+np.random.normal(0,10))
    
def turn_around(T,boxelist,n):
    mesures = [telemetry(T,boxelist)]
    for i in range(n-1):
        T.left(360.0/n)
        mesures.append(telemetry(T,boxelist))
    return mesures
"""    
def sortie(mesures,v):
    max=0
    compteur=0
    for i in range(len(mesures)):
        if mesures[i]<v:
            compteur=0
        else:
            compteur=compteur+1
            if(i==len(mesures)-1):
                j=i+1
                while mesures[j-len(mesures)]<v:
                    compteur=compteur+1
                    j=j+1
                if compteur>max:
                    max=compteur
                    indice=j
                
            
            else:
                if compteur>max:
                    max=compteur
                    indice=i
                
    return (indice-int(max/2))%len(mesures)
"""   
def sortie2(mesures,v, longmin):
    max1=0
    max2=0
    compteur=0
    sortieindice=[]
    sortielong=[]
    for i in range(len(mesures)):
        if mesures[i]<v:
            
            if compteur>0:
                print "compteur avant obstacle à lindice ",i,":  ",compteur
                sortieindice.append(i-1)
                sortielong.append(compteur)
            compteur=0
        else:
            compteur=compteur+1
    
    i1=sortieindice[sortielong.index(max(sortielong))]
    max1=sortielong.pop(sortielong.index(max(sortielong)))
    i2=sortieindice[sortielong.index(max(sortielong))]
    max2=sortielong.pop(sortielong.index(max(sortielong)))
    
    print "sortie1:",i1,"(",max1,")/sortie2:",i2,"(",max2,")"
    
    if max2<longmin:
        return i1%len(mesures)
    else:
        d1=abs((len(mesures)/2)-(i1-int(max1/2))%len(mesures))
        d2=abs((len(mesures)/2)-(i2-int(max2/2))%len(mesures))
        if d1<d2:
            return i1%len(mesures)
        else:
            return i2%len(mesures)
     
"""
            if(i==len(mesures)-1):
                j=i+1
                while mesures[j-len(mesures)]<v:
                    compteur=compteur+1
                    j=j+1
                  ##   if compteur>max2 and compteur<=max:
                   ##      max2=compteur
                  ##       indice2=j
                    if compteur>max:
                        max2=max
                        max=compteur
                        indice2=indice
                        indice=j"""
                
                
            
            ##else:
              ##   if compteur>max2 and compteur<=max:
               ##      max2=compteur
              ##       indice2=i
               ##  if compteur>max:
                ##     max2=max
              ##       max=compteur
               ##      indice2=indice
               ##      indice=i
"""          
            print "sortie1",indice,"(",max,")/sortie2:",indice2,"(",max2,")"
            if max2<2:
                return  indice%len(mesures)  
            else:
              ##  return min((indice-int(max/2))%len(mesures), (indice2-int(max2/2))%len(mesures))
                d1=abs((len(mesures)/2)-(indice-int(max/2))%len(mesures))
                d2=abs((len(mesures)/2)-(indice2-int(max2/2))%len(mesures))
                if d1<d2:
                    return indice%len(mesures)
                else:
                    return indice2%len(mesures)"""
           
                    
    
def escape(T,indice,n,v):
    if indice<(n/2):
        T.left(indice*360.0/n)
    else:
        T.right((indice-(n/2))*360.0/n)      
    T.fd(v)
    
def navigate(T,boxelist,n, longmin):
    mesures = turn_around(T,boxelist,n)
    plt.plot(mesures)
    plt.show()
    limit =sum(mesures,0.0)/len(mesures)
    print "Limite choisie:",limit
    i = sortie2(mesures,sum(mesures,0.0)/len(mesures), longmin)
    print "Sortie choisie: ",i
    escape(T,i,n,limit*2/3)

######### main ########
turtle.clearscreen()
T = turtle.Turtle()
T.penup()

boxelist = [ new_box(0,0,400) ]
boxelist = boxelist +[ new_box(100*cos(1+i*2*pi/15),100*sin(1+i*2*pi/15),random.randint(10,40)) for i in range(12)]
boxelist = boxelist +[ new_box(170*cos(1+i*2*pi/15),170*sin(1+i*2*pi/15),random.randint(10,40)) for i in range(12)]
for i in range(5):
    navigate(T,boxelist,50,5)
    time.sleep(2)

raw_input()
