#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.optimize import linprog
import matplotlib
import matplotlib.pyplot as plt
if __name__ == '__main__':


	fig, ax = plt.subplots()
	for i in range(1000, 10000, 50):
		initial_volume = i
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
		
		theSum_of_steel_to_steel = ans.x[0] + ans.x[4] + ans.x[8] + ans.x[12] + ans.x[16] 
		theSum_of_steel_to_up_steel = ans.x[1] + ans.x[5] + ans.x[9] + ans.x[13] + ans.x[17]
		theSum_of_steel_to_up_machine = ans.x[3] + ans.x[7] + ans.x[11] + ans.x[15] + ans.x[19]
			
		objective_function_val = plt.scatter(initial_volume, -ans.fun)
		steel_to_steel = plt.scatter(initial_volume, theSum_of_steel_to_steel, c="green") 
		steel_to_up_steel = plt.scatter(initial_volume, theSum_of_steel_to_up_steel, c="red") 
		steel_to_up_machine = plt.scatter(initial_volume, theSum_of_steel_to_up_machine, c="yellow")
		
	plt.title('Analisys of problem')
	ax.set_xlabel('Volume of steel')
	ax.set_ylabel('Values of variables')
	grid1 = plt.grid(True)
	plt.show()

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
#3.5*Xs1 <= 2000
#3.5*Xs2 - 0.4*Xs_u1 <= 2000 										~ 3.5*Xs2 <= 2000 + 0.4*Xs_u1
#3.5*Xs3 - 0.4*Xs_u1 - 0.4*Xs_u2 <= 2000 							~ 3.5*Xs3 <= 2000 + 0.4*Xs_u1 + 0.4*Xs_u2
#3.5*Xs4 - 0.4*Xs_u1 - 0.4*Xs_u2 - 0.4*Xs_u3 <= 2000 				~ 3.5*Xs4 <= 2000 + 0.4*Xs_u1 + 0.4*Xs_u2 + 0.4*Xs_u3
#3.5*Xs5 - 0.4*Xs_u1 - 0.4*Xs_u2 - 0.4*Xs_u3 - 0.4*Xs_u4 <= 2000 	~ 3.5*Xs5 <= 2000 + 0.4*Xs_u1 + 0.4*Xs_u2 + 0.4*Xs_u3 + 0.4*Xs_u4
#Machine production:
#1/1.2*Xm1 <= 1900
#1/1.2*Xm2 - 0.2*Xm_u1 <= 1900 										~ 1/1.2*Xm2 <= 1900 + 0.2*Xm_u1
#1/1.2*Xm3 - 0.2*Xm_u1 - 0.2*Xm_u2 <= 1900 							~ 1/1.2*Xm3 <= 1900 + 0.2*Xm_u1 + 0.2*Xm_u2
#1/1.2*Xm4 - 0.2*Xm_u1 - 0.2*Xm_u2 - 0.2*Xm_u3 <= 1900 				~ 1/1.2*Xm4 <= 1900 + 0.2*Xm_u1 + 0.2*Xm_u2 + 0.2*Xm_u3
#1/1.2*Xm5 - 0.2*Xm_u1 - 0.2*Xm_u2 - 0.2*Xm_u3 - 0.2*Xm_u4 <= 1900 	~ 1/1.2*Xm5 <= 1900 + 0.2*Xm_u1 + 0.2*Xm_u2 + 0.2*Xm_u3 + 0.2*Xm_u4

## Machine production can't take more than half of all resources:
#Xm1 + Xm_u1 <= 1900
#Xm2 + Xm_u2 - 0.5*Xs1 <= 0 										~ Xm2 + Xm_u2 <= 0.5*Xs1 
#Xm3 + Xm_u3 - 0.5*Xs2 <= 0											~ Xm3 + Xm_u3 <= 0.5*Xs2
#Xm4 + Xm_u4 - 0.5*Xs3 <= 0											~ Xm4 + Xm_u4 <= 0.5*Xs3
#Xm5 + Xm_u5 - 0.5*Xs4 <= 0											~ Xm5 + Xm_u5 <= 0.5*Xs4

## Can't spend more, than we have in the begining of the year
#Xs1 + Xs_u1 + Xm1 + Xm_u1 = 3900
#Xs2 + Xs_u2 + Xm2 + Xm_u2 - 3.5*Xs1 = 0 							~ Xs2 + Xs_u2 + Xm2 + Xm_u2 = 3.5*Xs1 
#Xs3 + Xs_u3 + Xm3 + Xm_u3 - 3.5*Xs2 = 0							~ Xs3 + Xs_u3 + Xm3 + Xm_u3 = 3.5*Xs2
#Xs4 + Xs_u4 + Xm4 + Xm_u4 - 3.5*Xs3 = 0							~ Xs4 + Xs_u4 + Xm4 + Xm_u4 = 3.5*Xs3
#Xs5 + Xs_u5 + Xm5 + Xm_u5 - 3.5*Xs4 = 0							~ Xs5 + Xs_u5 + Xm5 + Xm_u5 = 3.5*Xs4

#Vx >= 0


