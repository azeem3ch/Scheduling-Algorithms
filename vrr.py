class process:

	def _init_ (self,arrival=0,burst=0,to=0,time=0,wait=0,quantum=0,turnaround=0,waiting=0,r_burst=0,r_time=0,p_name=0):
		self.arrival=0
		self.burst=0
		self.io=0
		self.time=0
		self.wait=0
		self.quantum=0
		self.turnaround=0
		self.waiting=0
		self.r_burst=0
		self.r_time=0
		self.p_name=0

def chknew(index,size,total,p_size,initial,ready):
	temp=-1
	i=index
	while(i<size):
		if(initial[i].arrival<=total):
			ready.append(initial[i])
			p_size+=1
			temp=i+1
		i+=1
	if(temp!=-1):
		index=temp		

	return index,p_size,ready

def chkwaiting(w_size,total_t,p_size,ready_list,waiting_list,a_index,chk):
	loop=0
	while(loop<w_size):
		a_chk=chk
		if(waiting_list[loop].arrival <= total_t):
			waiting_list[loop].arrival=waiting_list[loop].r_time
			waiting_list[loop].r_time=waiting_list[loop].time
			if(waiting_list[loop].quantum==quantum_t):
				ready_list.append(waiting_list[loop])
				del waiting_list[loop]
				w_size-=1
				p_size+=1
			else:
				ready_list.append(waiting_list[loop])
				p_size+=1
				if(chk==0):
					temp=process()
					temp=waiting_list[loop]
					var1=p_size-1
					var2=p_size-2
				
					while(var2>a_index):
						ready_list[var1]=ready_list[var2]
						var1-=1
						var2-=1
					a_index+=1
					ready_list[a_index]=waiting_list[loop]
				del waiting_list[loop]
				w_size-=1
		loop+=1

	return w_size,p_size,ready_list,waiting_list,a_index

size =int(input("how many process you wanna create :"))

initial_list=[process() for i in range(size)]

quantum_t=int(input("enter quantum time (>0):") )

for index in range (size):
	initial_list[index].quantum=quantum_t
	initial_list[index].p_name=int(input("enter process id :"))
	initial_list[index].arrival=int(input("enter arrival time of process :"))
	initial_list[index].burst=int(input("enter burst time of process :"))
	initial_list[index].r_burst=initial_list[index].burst
	initial_list[index].io=int(input("will this process go for i/o (1->yes /any key->no) :"))
	if(initial_list[index].io==1):
		initial_list[index].time=int(input("time after it will go for i/o (>0) :"))
		if(initial_list[index].time<1):
			initial_list[index].time=2
		initial_list[index].r_time=initial_list[index].time
		initial_list[index].wait=int(input("enter time process will take in i/o :"))

initial_list.sort(key=lambda c: c.arrival)

total_t=initial_list[0].arrival
i_index=0	#index of initial_list
p_size=0	#ready list size
e_index=0	#index of executed_list
w_index=0	#index of waiting
w_size=0	#size of waiting
a_index=0


ready_chk=0

ready_list=[]
waiting_list=[]
executed_list=[]
auxilary_list=[]


temp=0
for i in range(i_index,size):
	if(initial_list[i].arrival<=total_t):
		ready_list.append(initial_list[i])
		p_size+=1
		temp=i+1
i_index=temp



index=0
while(index<p_size or w_index<w_size or i_index<size):
	if(index<p_size):
		if(ready_list[index].r_burst<=ready_list[index].quantum):
			if(ready_list[index].io!=1):
				for loop in range(ready_list[index].r_burst):
					total_t+=1
					i_index,p_size,ready_list=chknew(i_index,size,total_t,p_size,initial_list,ready_list)
					w_size,p_size,ready_list,waiting_list,a_index=chkwaiting(w_size,total_t,p_size,ready_list,waiting_list,a_index,0)

				ready_list[index].turnaround = total_t - ready_list[index].arrival
				ready_list[index].waiting = total_t - ready_list[index].arrival - ready_list[index].burst
				executed_list.append(ready_list[index])
				e_index+=1

			elif(ready_list[index].r_burst<=ready_list[index].r_time):
				for loop in range(ready_list[index].r_burst):
					total_t+=1
					i_index,p_size,ready_list=chknew(i_index,size,total_t,p_size,initial_list,ready_list)
					w_size,p_size,ready_list,waiting_list,a_index=chkwaiting(w_size,total_t,p_size,ready_list,waiting_list,a_index,0)

				ready_list[index].turnaround = total_t - ready_list[index].arrival
				ready_list[index].waiting = total_t - ready_list[index].arrival - ready_list[index].burst
				executed_list.append(ready_list[index])
				e_index+=1

			else:
				for loop in range(ready_list[index].r_time):
					total_t+=1
					ready_list[index].quantum-=1
					i_index,p_size,ready_list=chknew(i_index,size,total_t,p_size,initial_list,ready_list)
					w_size,p_size,ready_list,waiting_list,a_index=chkwaiting(w_size,total_t,p_size,ready_list,waiting_list,a_index,0)

				ready_list[index].r_burst-=ready_list[index].r_time

				if(ready_list[index].quantum==0):
					ready_list[index].quantum=quantum_t
				
				waiting_list.append(ready_list[index])
				waiting_list[w_size].r_time=waiting_list[w_size].arrival
				waiting_list[w_size].arrival = total_t + waiting_list[w_size].wait
				waiting_list.sort(key=lambda c: c.arrival)
				w_size+=1
		else:
			if(ready_list[index].io!=1 or ready_list[index].quantum<ready_list[index].r_time):
				for loop in range(ready_list[index].quantum):
					total_t+=1
					ready_list[index].r_burst-=1
					if(ready_list[index].io==1):
						ready_list[index].r_time-=1
					i_index,p_size,ready_list=chknew(i_index,size,total_t,p_size,initial_list,ready_list)
					w_size,p_size,ready_list,waiting_list,a_index=chkwaiting(w_size,total_t,p_size,ready_list,waiting_list,a_index,0)
				
				ready_list.append(ready_list[index])
				p_size+=1
			else:
				for loop in range(ready_list[index].r_time):
					total_t+=1
					ready_list[index].quantum-=1
					i_index,p_size,ready_list=chknew(i_index,size,total_t,p_size,initial_list,ready_list)
					w_size,p_size,ready_list,waiting_list,a_index=chkwaiting(w_size,total_t,p_size,ready_list,waiting_list,a_index,0)

				ready_list[index].r_burst-=ready_list[index].r_time

				if(ready_list[index].quantum==0):
					ready_list[index].quantum=quantum_t
			
				waiting_list.append(ready_list[index])
				waiting_list[w_size].r_time=waiting_list[w_size].arrival
				waiting_list[w_size].arrival = total_t + waiting_list[w_size].wait
				waiting_list.sort(key=lambda c: c.arrival)
				w_size+=1
		if(a_index==index):
			a_index+=1
		index+=1	
	else:
		total_t+=1
		i_index,p_size,ready_list=chknew(i_index,size,total_t,p_size,initial_list,ready_list)
		w_size,p_size,ready_list,waiting_list,a_index=chkwaiting(w_size,total_t,p_size,ready_list,waiting_list,a_index,1)


print "process_id\tarrival_t\tburst_t    turnaround_t   waiting_t",e_index

for i in range(e_index):
	print "     ",executed_list[i].p_name,"\t  ",executed_list[i].arrival,"\t\t   ",executed_list[i].burst,"\t       ",executed_list[i].turnaround,"\t   ",executed_list[i].waiting,"\n"


