from collections import OrderedDict
from operator import itemgetter

size =input("how many process you wanna create :")
pointer=0
arry={}
for count in range(size):
	arry.setdefault(count,[]).append(input("enter process arrival time :"))
	arry.setdefault(count,[]).append(input("enter process burst time :"))
	

turnaround_t=0
waiting_t=0
total_t=0

ordered_dict=OrderedDict(sorted(arry.items(),key=itemgetter(1)))

for count in ordered_dict:

	while(total_t<ordered_dict[count][0]):
		total_t=total_t+1

	if(ordered_dict[count][1]!=0):
		for t in range(ordered_dict[count][1]):
			total_t=total_t+1

	#storing turnaround and waiting of current process 	
	ordered_dict.setdefault(count,[]).append(total_t-ordered_dict[count][0])	
	ordered_dict.setdefault(count,[]).append(total_t-ordered_dict[count][0]-ordered_dict[count][1])
#	print ordered_dict[count],total_t

	#adding to total turn. and wait.
	turnaround_t+=ordered_dict[count][2]
	waiting_t+=ordered_dict[count][3]

print ("\n[0]->process id , [0]:[0]-> arrival time , [0]:[1] burst time ,[0]:[2] turnaround time , [0]:[3] waiting time\n")
print ordered_dict
print ('\nAverage turnaround time is %d' % (turnaround_t/size))	
print ('Average waiting time is %d' % (waiting_t/size))
