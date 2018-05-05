from collections import OrderedDict
from operator import itemgetter

size =input("how many process you wanna create :")
pointer=0
arry={}
for count in range(size):
	arry.setdefault(count,[]).append(input("enter process arrival time :"))
	arry.setdefault(count,[]).append(input("enter process burst time :"))
	arry.setdefault(count,[]).append(0)
	

turnaround_t=0
waiting_t=0
total_t=0
executed={}
length=len(arry)

while(length!=0):
	minimum=0
	key=-1
	minchk=0
	for chk in arry:
		if(arry[chk][0]<=total_t and arry[chk][2]==0):
			if(minchk==0):				
				minimum=arry[chk][1]
				key=chk
				minchk=1
			else:
				if(arry[chk][1]<minimum):
					minimum=arry[chk][1]
					key=chk
	if(key!=-1):
		for loop in range(arry[key][1]):
			total_t=total_t+1

		executed.setdefault(key,[]).append(arry[key][0])
		executed.setdefault(key,[]).append(arry[key][1])
		executed.setdefault(key,[]).append(total_t-arry[key][0])	
		executed.setdefault(key,[]).append(total_t-arry[key][0]-arry[key][1])
		#adding to total turn. and wait.
		turnaround_t+=executed[key][2]
		waiting_t+=executed[key][3]
		arry[key][2]=1
		length=length-1;
	else:
		total_t=total_t+1

print ("\n[0]->process id , [0]:[0]-> arrival time , [0]:[1] burst time ,[0]:[2] turnaround time , [0]:[3] waiting time\n")
print executed

print ('\nAverage turnaround time is %d' % (turnaround_t/size))	
print ('Average waiting time is %d' % (waiting_t/size))
