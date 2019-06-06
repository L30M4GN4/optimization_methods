#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.optimize import linprog
if __name__ == '__main__':

	initial_volume = 3000
	costs = [0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0] #Vector of coefficients in objective function

	A_ub = [[3.7,0,0,0,     0,0,0,0,       0,0,0,0,       0,0,0,0,       0,0,0,0], #Matrix of coefficients (left part) in inequalities
		    [0,-0.4,0,0,    3.7,0,0,0,     0,0,0,0,       0,0,0,0,       0,0,0,0],
		    [0,-0.4,0,0,    0,-0.4,0,0,    3.7,0,0,0,     0,0,0,0,       0,0,0,0],
		    [0,-0.4,0,0,    0,-0.4,0,0,    0,-0.4,0,0,    3.7,0,0,0,     0,0,0,0],
		    [0,-0.4,0,0,    0,-0.4,0,0,    0,-0.4,0,0,    0,-0.4,0,0,    3.7,0,0,0],
		    [0,0,(1/0.8),0, 0,0,0,0,       0,0,0,0,       0,0,0,0,       0,0,0,0],
		    [0,0,0,-0.1,    0,0,(1/0.8),0, 0,0,0,0,       0,0,0,0,       0,0,0,0],
		    [0,0,0,-0.1,    0,0,0,-0.1,    0,0,(1/0.8),0, 0,0,0,0,       0,0,0,0],
		    [0,0,0,-0.1,    0,0,0,-0.1,    0,0,0,-0.1,    0,0,(1/0.8),0, 0,0,0,0],
		    [0,0,0,-0.1,    0,0,0,-0.1,    0,0,0,-0.1,    0,0,0,-0.1,    0,0,(1/0.8),0],
		    [0,0,1,1,       0,0,0,0,       0,0,0,0,       0,0,0,0,       0,0,0,0],
		    [-0.5,0,0,0,    0,0,1,1,       0,0,0,0,       0,0,0,0,       0,0,0,0],
		    [0,0,0,0,       -0.5,0,0,0,    0,0,1,1,       0,0,0,0,       0,0,0,0],
		    [0,0,0,0,       0,0,0,0,       -0.5,0,0,0,    0,0,1,1,       0,0,0,0],
		    [0,0,0,0,       0,0,0,0,       0,0,0,0,       -0.5,0,0,0,    0,0,1,1]]
		     
	b_ub = [5400, 5400, 5400, 5400, 5400, 1100, 1100, 1100, 1100, 1100, 1100, 0, 0, 0, 0] #Vector of coefficients (right part) in inequalities

	A_eq = [[1,1,1,1,    0,0,0,0,    0,0,0,0,    0,0,0,0,    0,0,0,0],#Matrix of coefficients (left part) in equalities
		    [-3.7,0,0,0, 1,1,1,1,    0,0,0,0,    0,0,0,0,    0,0,0,0],
		    [0,0,0,0,    -3.7,0,0,0, 1,1,1,1,    0,0,0,0,    0,0,0,0],
		    [0,0,0,0,    0,0,0,0,    -3.7,0,0,0, 1,1,1,1,    0,0,0,0],
		    [0,0,0,0,    0,0,0,0,    0,0,0,0,    -3.7,0,0,0, 1,1,1,1]] 
    
	b_eq = [initial_volume, 0, 0, 0, 0] #Vector of coefficients (right part) in equalities
	ans = linprog(costs, A_ub, b_ub, A_eq, b_eq)
	print(ans)

########################################################################################
##Usefull links:
#https://habr.com/ru/post/330648/
#https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.optimize.linprog.html
#https://cais.iias.spb.su/ponomarev/LP_tutorial.pdf page 26

##There are four types of wasting steel, our factory working for 5 years,so:
#Xs[1-5] - steel production
#Xs_u[1-5] - power increasing of steel production
#Xm[1-5] - machine production
#Xm_u[1-5] - power increasing of machine production

#Objective function (We need to maximize machine production):
#Xm1 + Xm2 + Xm3 + Xm4 + Xm5 -> max

#For matrix:
#x[0] - Xs1, 
#x[1] - Xs_u1, 
#x[2] - Xm1, 
#x[3] - Xm_u1, 
#x[4] - Xs2, 
#x[5] - Xs_u2, 
#x[6] - Xm2, 
#x[7] - Xm_u2, 
#x[8] - Xs3, 
#x[9] - Xs_u3, 
#x[10] - Xm3, 
#x[11] - Xm_u3, 
#x[12] - Xs4, 
#x[13] - Xs_u4, 
#x[14] - Xm4, 
#x[15] - Xm_u4, 
#x[16] - Xs5, 
#x[17] - Xs_u5, 
#x[18] - Xm5, 
#x[19] - Xm_u5

## Can't produce more, than power of factory:
#Steel production:
#3.7*Xs1 <= 5400
#3.7*Xs2 - 0.4*Xs_u1 <= 5400 										~ 3.7*Xs2 <= 5400 + 0.4*Xs_u1
#3.7*Xs3 - 0.4*Xs_u1 - 0.4*Xs_u2 <= 5400 							~ 3.7*Xs3 <= 5400 + 0.4*Xs_u1 + 0.4*Xs_u2
#3.7*Xs4 - 0.4*Xs_u1 - 0.4*Xs_u2 - 0.4*Xs_u3 <= 5400 				~ 3.7*Xs4 <= 5400 + 0.4*Xs_u1 + 0.4*Xs_u2 + 0.4*Xs_u3
#3.7*Xs5 - 0.4*Xs_u1 - 0.4*Xs_u2 - 0.4*Xs_u3 - 0.4*Xs_u4 <= 5400 	~ 3.7*Xs5 <= 5400 + 0.4*Xs_u1 + 0.4*Xs_u2 + 0.4*Xs_u3 + 0.4*Xs_u4
#Machine production:
#1/0.8*Xm1 <= 1100
#1/0.8*Xm2 - 0.1*Xm_u1 <= 1100 										~ 1/0.8*Xm2 <= 1100 + 0.1*Xm_u1
#1/0.8*Xm3 - 0.1*Xm_u1 - 0.1*Xm_u2 <= 1100 							~ 1/0.8*Xm3 <= 1100 + 0.1*Xm_u1 + 0.1*Xm_u2
#1/0.8*Xm4 - 0.1*Xm_u1 - 0.1*Xm_u2 - 0.1*Xm_u3 <= 1100 				~ 1/0.8*Xm4 <= 1100 + 0.1*Xm_u1 + 0.1*Xm_u2 + 0.1*Xm_u3
#1/0.8*Xm5 - 0.1*Xm_u1 - 0.1*Xm_u2 - 0.1*Xm_u3 - 0.1*Xm_u4 <= 1100 	~ 1/0.8*Xm5 <= 1100 + 0.1*Xm_u1 + 0.1*Xm_u2 + 0.1*Xm_u3 + 0.1*Xm_u4

## Machine production can't take more than half of all resources:
#Xm1 + Xm_u1 <= 1100
#Xm2 + Xm_u2 - 0.5*Xs1 <= 0 										~ Xm2 + Xm_u2 <= 0.5*Xs1 
#Xm3 + Xm_u3 - 0.5*Xs2 <= 0											~ Xm3 + Xm_u3 <= 0.5*Xs2
#Xm4 + Xm_u4 - 0.5*Xs3 <= 0											~ Xm4 + Xm_u4 <= 0.5*Xs3
#Xm5 + Xm_u5 - 0.5*Xs4 <= 0											~ Xm5 + Xm_u5 <= 0.5*Xs4

## Can't spend more, than we have in the begining of the year
#Xs1 + Xs_u1 + Xm1 + Xm_u1 = 3000
#Xs2 + Xs_u2 + Xm2 + Xm_u2 - 3.7*Xs1 = 0 							~ Xs2 + Xs_u2 + Xm2 + Xm_u2 = 3.7*Xs1 
#Xs3 + Xs_u3 + Xm3 + Xm_u3 - 3.7*Xs2 = 0							~ Xs3 + Xs_u3 + Xm3 + Xm_u3 = 3.7*Xs2
#Xs4 + Xs_u4 + Xm4 + Xm_u4 - 3.7*Xs3 = 0							~ Xs4 + Xs_u4 + Xm4 + Xm_u4 = 3.7*Xs3
#Xs5 + Xs_u5 + Xm5 + Xm_u5 - 3.7*Xs4 = 0							~ Xs5 + Xs_u5 + Xm5 + Xm_u5 = 3.7*Xs4

#Vx >= 0


