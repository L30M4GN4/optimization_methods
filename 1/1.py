#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.optimize import linprog
if __name__ == '__main__':
	costs = [4.6, 3.5, 4.6, 3.5, 2.7, 3.5, 2.7, 3.5, 4.6, 3.5, 2.7, 3.5] #Vector of costs (#Vector of coefficients in objective function)

	A_ub = [[1,1,0,0,0,0,0,0,1,1,0,0], #Matrix of coefficients (left part) in inequalities
		    [0,0,1,1,0,0,0,0,0,0,0,0],
		    [0,0,0,0,1,1,0,0,0,0,1,1],
		    [0,0,0,0,0,0,1,1,0,0,0,0],
		    [-1,0,0,0,-1,0,0,0,0,0,0,0],
		    [0,0,-1,0,0,0,-1,0,-0.7,0,-0.7,0],
		    [0,-1,0,0,0,-1,0,0,0,0,0,0],
		    [0,0,0,-1,0,0,0,-1,0,-0.7,0,-0.7],]
		     
	b_ub = [3900, 4500, 5900, 4200, -2100, -2800, -5000, -4600] #Vector of coefficients (right part) in inequalities

	A_eq = [[1,0,1,0,1,0,1,0,0.7,0,0.7,0],#Matrix of coefficients (left part) in equalities
		    [0,1,0,1,0,1,0,1,0,0.7,0,0.7]] 
		    
	b_eq = [5600, 10200] #Vector of coefficients (right part) in equalities

	print(linprog(costs, A_ub, b_ub, A_eq, b_eq))

########################################################################################

##Usefull links:
#https://habr.com/ru/post/330648/
#https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.optimize.linprog.html
#https://cais.iias.spb.su/ponomarev/LP_tutorial.pdf page 26

##There are two types of steel in a two warehouses:
#warehouse1_steelA = 3900
#warehouse1_steelB = 4500
#warehouse2_steelA = 5900
#warehouse2_steelB= 4200

##And two consumers needs two types of steel:
#consumer1_steelA = 2100
#consumer1_steelB = 2800
#consumer1_steelA_or_steelB = 700
#consumer2_steelA = 5000
#consumer2_steelB = 4600

##One ton of steel B may be replaced with 1/0.7 ton of steel A, but not vice versa:
#steelA = 0.7*steelB 

##Shipping costs:
#cost1_1 = 4.6
#cost1_2 = 3.5
#cost2_1 = 2.7
#cost2_2 = 3.5

##All x-s are supply volumes:
#x[0] - warehouse1_A-consumer1,
#x[1] - warehouse1_A-consumer2, 
#x[2] - warehouse1_B-consumer1, 
#x[3] - warehouse1_B-consumer2, 
#x[4] - warehouse2_A-consumer1, 
#x[5] - warehouse2_A-consumer2, 
#x[6] - warehouse2_B-consumer1, 
#x[7] - warehouse2_B-consumer2, 
#x[8] - warehouse1_AtoB-consumer1,  
#x[9] - warehouse1_AtoB-consumer2, 
#x[10] - warehouse2_AtoB-consumer1, 
#x[11] - warehouse2_AtoB-consumer2 

#Objective function
#4.6*(x[0] + x[2] + x[8]) + 3.5*(x[1] + x[3] + x[5] + x[7] + x[9] + x[11]) + 2.7*(x[4] + x[6] + x[10]) -> min

## Can't give more than we have
#1st warehouse:
#(x[0] + x[1] + x[8] + x[9]) <= 3900
#(x[2] + x[3]) <= 4500
#2nd warehouse:
#(x[4] + x[5] + x[10] + x[11]) <= 5900
#(x[6] + x[7]) <= 4200

## Ship as much as you need
#1st consumer:
#(x[0] + x[4] >= 2100) ~ #(-x[0] - x[4] <= -2100)  
#(x[2] + x[6] + 0.7(x[8]+x[10])>= 2800) ~ #(-x[2] - x[6] - 0.7(x[8]-x[10]) <= -2800)
#(x[0] + x[4] + x[2] + x[6] + 0.7(x[8]+x[10])) = 5600
#2nd consumer:	
#(x[1] + x[5]) >= 5000 ~ #(-x[1] - x[5]) <= -5000
#(x[3] + x[7]+ 0.7(x[9]+x[11])) >= 4600 ~ #(x[3] - x[7] - 0.7(x[9]-x[11])) <= -4600)
#(x[1] + x[5] + x[3] + x[7]+ 0.7(x[9]+x[11])) = 10200

#x[0:11] > 0


