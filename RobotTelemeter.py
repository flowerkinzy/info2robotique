# -*- coding: utf-8 -*-
"""
Telemetry
"""
import random
import nxt, thread, time

from math import *
import numpy as np
import matplotlib.pyplot as plt
robot = nxt.find_one_brick()
mA = nxt.Motor(robot, nxt.PORT_B)
mB = nxt.Motor(robot, nxt.PORT_C)
sonar = nxt.sensor.Ultrasonic(robot,nxt.PORT_1)


"""def new_box(x,y,c):
    V = turtle.Turtle()
    V.hideturtle(); V.penup()
    V.setpos(x-c/2,y-c/2); V.setheading(0) ; V.pendown()
    for i in range(4):
        V.fd(c)
        V.left(90)
    return Polygon(Point(x-c/2,y-c/2),Point(x-c/2,y+c/2),Point(x+c/2,y+c/2),Point(x+c/2,y-c/2))
    """

def telemetry(T,boxelist):
    a = radians(T.heading())
    P1,P2 = Point(T.xcor(),T.ycor()) , Point(T.xcor()+cos(a),T.ycor()+sin(a))
    P12 = P2 - P1
    intr = [N(P12.dot(p-P1)) for r in boxelist for p in intersection(Line(P1,P2),r) ]
    intr = [d for d in intr if d >= 0]
    #print intr
    return None if intr==[] else (min(intr)+np.random.normal(0,10))
    
def turn_around(n):
    mesures = [sonar.get_sample()]
    mA.run(70)
    mB.run(-70)
    for i in range(n-1):
        #mA.turn(80,360.0/n,True)
        mesures.append(sonar.get_sample())
        time.sleep(0.02)
    mA.run(0)
    mB.run(0)

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
     

           
                    
    
def escape(indice,n,v):
    if indice<(n/2):
        mA.turn(80,indice*360.0/n,True)
    else:
        mB.turn(80,(indice-(n/2))*360.0/n,True)      
    mA.run(100);mB.run(100);time.sleep(2);mA.brake();mB.brake()
    
def navigate(n, longmin):
    mesures = turn_around(n)
    plt.plot(mesures)
    plt.show()
    limit =sum(mesures,0.0)/len(mesures)
    print "Limite choisie:",limit
    i = sortie2(mesures,sum(mesures,0.0)/len(mesures), longmin)
    print "Sortie choisie: ",i
    escape(i,n,limit*2/3.5)
   

######### main ########

for i in range(10):
    navigate(200,5)
    time.sleep(2)
raw_input()
