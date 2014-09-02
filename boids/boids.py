#!/usr/bin/python
import turtle
import random
import math

boid=[]
N=10
V=4
C=0
C1=0
C2=10
C3=0
rayon=10


#creation des tortues
for i in range(N):
	boid.append(turtle.Turtle())

turtle.tracer(5,1)

#initialisation
for i in range(N):
	boid[i].penup()
	boid[i].setposition(random.randint(-150,150),random.randint(-150,150))
	boid[i].setheading(random.randint(0,359))
	boid[i].color((random.random(),random.random(),random.random()))
	#boid[i].pendown()

"""def position_moyenne():
	pmx, pmy = 0, 0
	for i in range(N):
		x,y = boid[i].position()
	 	pmx += x
		pmy += y
	pmx /= N
	pmy /= N
	return pmx, pmy
"""
def position_moyenne():
	return barycentre(boid)
def angle_moyen():
	angle=0.0
	for i in range(N):
		angle += boid[i].heading()
	return angle/N

def voisins(i):
	t_voisins=[]
	for j in range(N):
		if j!=i :
			if math.fabs(boid[i].distance(boid[j]))<rayon:
				t_voisins.append(boid[j])
	return t_voisins

#tab est un tableau de turtles
def barycentre(tab):
	bx,by=0,0
	for i in range(len(tab)):
		x,y=tab[i].position()
		bx+=x
		by+=y
	bx/=len(tab)
	by/=len(tab)
	return bx, by

def vecttoangl(vx,vy):
	angle=math.atan2(vy,vx)*(360/(2*math.pi))
	return angle

# L'angle est en radians
def angletovect(angle):
	return V*math.cos(angle*57.17), V*math.sin(angle *57.17)
	
def regle1(i):
	x,y=boid[i].position()
	pmx,pmy=position_moyenne()
	vx,vy=pmx-x, pmy-y
	return vx,vy

def regle2():
	return angletovect(angle_moyen())

def regle3(i):
	if len(voisins(i))==0:
		return 0,0
	else:
		x,y=boid[i].position()
		x2,y2=barycentre(voisins(i))
		return x-x2,y-y2

"""
def move(i):
	vx,vy=regle1(i)
	vx2,vy2=regle2()
	vx3,vy3=regle3(i)
	x,y=V*math.cos(boid[i].heading()*57.17),V*math.sin(boid[i].heading()*57.17)
	vx=x*C+vx*C1+vx2*C2+vx3*C3
	vy=y*C+vy*C1+vy2*C2+vy3*C3

	boid[i].setheading(vecttoangl(vx,vy))
	boid[i].forward(V)
"""
def move(i,v2x,v2y):
	vx,vy=regle1(i)
	vx3,vy3=regle3(i)
	x,y=V*math.cos(boid[i].heading()*57.17),V*math.sin(boid[i].heading()*57.17)
	"""
	vx=x*C+vx*C1+v2x*C2+vx3*C3
	vy=y*C+vy*C1+v2y*C2+vy3*C3
	"""
	vx=x*C+vx*C1+v2x*C2+vx3*C3
	vy=y*C+vy*C1+v2y*C2+vy3*C3
	boid[i].setheading(vecttoangl(vx,vy))
	boid[i].forward(V)


def move_all():
	vx2,vy2=regle2()
	for i in range(N):
		move(i,vx2,vy2)
	

while (1):
	move_all()



