#!/usr/bin/env python3
# -*- coding: utf-8 -*-

inf = 10**8																#infinum

plans_list = []
temp_list = []
optimal_plan = []
table = [0,7,6,3,0,2] 													#My table's values
def making_lists(Machines, Storage,month,cost):
	 plans_list.append((month,Storage,Machines,cost))

def searching_minimum(temp_list):
	for i in temp_list:
		tmp = (min((j[3]) for j in temp_list))
		if tmp in i:
			return i

def printing_result(plans_list):
	temp_list.clear()
	for i in reversed(plans_list):
		if i[0] == 6 and i[2] == 0:
			temp_list.append(i)
		else: continue
	optimal_plan.append(searching_minimum(temp_list))
	for i in optimal_plan:
		for j in reversed(plans_list):
			if (i and j and j[0] == (i[0]-1) and j[2] == i[1]):
				temp_list.append(j)
		if searching_minimum(temp_list) not in optimal_plan:
			optimal_plan.append(searching_minimum(temp_list))
			temp_list.clear()
#	for i in optimal_plan:
#		print ("Month " + str(i[0]) + ": stored - " + str(i[1]) + " shipped -  " + str(i[2]-i[1]+table[int(i[0])-1]) + " bought - " + str(table[i[0]-1]) + " => " + str(i[2]))
	return optimal_plan[0:-1]		
	
def solving_problem(price_of_storage):
#	Given as conditions of the problem
	#################
	num_of_month = 6
	max_shipping = 5
	max_storage = 20
	init_machines = 1
	#################
	
#	Making matrix of goal function (costs of one month)
	#################
	F = [[inf]*(num_of_month+1) for i in range (max_storage+1)] 			# matrix (num_of_month+1)x(max_storage+1) of goal function, consists of 																																				inf
	F[init_machines][0] = 0 												# The cost of storage+shipping 0 machines in 0 month = 0, bcs we have 																															them as initial (0 month)
	#################
	
	month = 0
	for month in range (num_of_month):
		for Storage in range (max_storage+1):
			cost = F[Storage][month] 										#firstly, all costs = inf 
			for Shipped in range (max_shipping+1):
				Needed = table[month]
				if (Needed < 0): Needed = 0
				Machines = Storage + Shipped - Needed						#Num of machines in the end of month
				if (0 <= Machines <= max_storage):
					if (Shipped > 0): cost_of_shipping = 50 + 10*Shipped
					else:
						Shipped = 0
						cost_of_shipping = 0
					
					cost_of_storage = price_of_storage*(Storage+Needed)		#Customers buy machines during the month, not in the begining of it.
					new_cost = cost + cost_of_shipping + cost_of_storage 	#if cost != inf => cost = new_cost (Rewriting costs)
					if new_cost < F[Machines][month+1]:
						F[Machines][month+1] = new_cost
#						Uncomment this for debugging:
#						print("Месяц: " + str(month + 1) + " было " + str(Storage) + " + доставлено " + str(Shipped) +
#                          " - забрали " + str(Needed) + " => " + str(Machines) +
#                          " на доставку " + str(cost_of_shipping) + "$ " +
#                          " затраты на хранение: " + str(cost_of_storage) + "$")
						making_lists(Machines, Storage, month+1, new_cost)
	return F
	
def main():
	price_of_storage = 10
	F = solving_problem(price_of_storage)
#	And this for debugging too:
#	machines = 0
#	for line in F:
#		print("%2d" % machines, end=' ')
#		machines += 1
#		for x in line:
#		    print("inf" if x == inf else x, end=' ')
#		print()
#	print ("Optimal plan is:")
	save = printing_result(plans_list).copy()
	withoult_costs = []
	for i in save:
		withoult_costs.append((i[0],i[1], i[2])) #Strip off costs in corteje
	save_withoult_costs = withoult_costs.copy()
	plans_list.clear()
	optimal_plan.clear()
	print ("Previous optimal plan is: ")
	print (save)
	for price_of_storage in range (1,200):
		withoult_costs.clear()
		F = solving_problem(price_of_storage)
		tmp = printing_result(plans_list).copy()
		for i in tmp:
			withoult_costs.append((i[0],i[1], i[2]))
		new_withoult_costs = withoult_costs.copy()
		plans_list.clear()
		optimal_plan.clear()
		for i in range(len(new_withoult_costs)):
			if (new_withoult_costs[i] != save_withoult_costs[i]):
				print ("New optimal plan: ", tmp)
				print ("Began optimal at " + str(price_of_storage) + " cost of storage")
				break
		else: continue
		break 	


if __name__ == '__main__':
	main()

########################################################################################

##There are three types of wasting money, our problem is calculated for 6 months,so:
#Shipped[1-6] - machines shipped
#Storage[1-6] - machines in warehouse
#Needed[1-6] - machines needed

#final_cost = cost_1 + cost_2 + ... + cost_6

#Storagej = Storagej-1 + Shippedj - Neededj
#50*Is_shipped + 10*Shipped = cost_of_one_shipping
#10*Storage = cost_of_storage

#sum_costN = min{cost_of_one_shippingN + cost_of_storageN + sum_cost(N-1)}, N = 1..6
#sum_cost0 = 0
#cost_of_one_shipping1 = 50*Is_shipped1 + 10*Shipped1
#cost_of_storage1 = 10*Storage1

#sum_cost1 = min{cost_of_one_shipping1 + cost_of_storage1 + sum_cost0}
#Shippedn = NeedN - Storage(N-1)
#StorageN = 0
#StorageN - 5 + NeedN <= Storage(N-1) <=

#Storage0 = 0

