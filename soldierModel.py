import math
import numpy

class Soldier():

	def __init__(self,xcoord,ycoord):
		self.x = xcoord;
		self.y = ycoord;
		self.alive = 1;
		

	def getPos(self):
		return (self.x, self.y)


	def checkKillrate(self, enemy):			#hur avtar traffsakerheten med avstand
		[xEnemy, yEnemy] = enemy.getPos()
		x = self.x - xEnemy;
		y = self.y - yEnemy;
		d = math.sqrt(pow(x,2) +pow(y,2))
		if d<15:
			killrate = 1/(1+math.exp(0.5*(d-5)));
		else: 
			killrate = 0
		return killrate;


	def getAngle(self,soldierOnePos,soldierTwoPos):
		deltaX = soldierTwoPos[0] - soldierOnePos[0];
		deltaX = float(deltaX)
		deltaY = soldierTwoPos[1] - soldierOnePos[1];
		deltaY = float(deltaY)
		if deltaX==0:
			return 0;
		if deltaY == 0:
			return 90;
		theta = math.atan(deltaX/deltaY);
		theta = math.degrees(theta);
		return theta;


	def isInLineOfFire(self,friendBetween,enemy):
		friendPos = self.getPos();													#return 1 if friend is in line of fire otherwise 0
		friendBetweenPos = friendBetween.getPos();
		enemyPos = enemy.getPos();
	
		alpha = self.getAngle(friendPos,enemyPos)
		beta = self.getAngle(friendPos,friendBetweenPos)
		Y1 = friendPos[1];
		Y2 = friendBetweenPos[1];
		Y3 = enemyPos[1];
		deltaAngle = abs(beta-alpha);	
		if (deltaAngle < 7) and (Y1<Y2) and (Y2<Y3):								#set angle of occlusion
			return 1;
		elif (deltaAngle < 7) and (Y1>Y2) and (Y2>Y3):
			return 1;			
			
		else:
			return 0;