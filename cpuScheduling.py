
# # numberOfProcesses = input("plz input number of processes: ")

# # listOfProcesses = input("plz input processes: ")

# # ArrivalTimes = input("plz input arrival times: ")

# # ExecutionTimes = input("plz input execution times: ")

# # typeOfScheduling = input("plz input type of scheduling algorithm: ")


numberOfProcesses = 5
listOfProcesses = ["p0","p1","p2","p3","p4"]
ArrivalTimes = [0,1,3,1,0]
ExecutionTimes = [5,3,10,6,8]
processPerClock = []
clock = 0

copyOfListOfProcesses = list(listOfProcesses)
copyOfArrivalTimes = list(ArrivalTimes)
copyOfExecutionTimes = list(ExecutionTimes)

copyOfListOfProcesses2 = list(listOfProcesses)
copyOfArrivalTimes2 = list(ArrivalTimes)
copyOfExecutionTimes2 = list(ExecutionTimes)

print "Number of processes: ", numberOfProcesses
print "List of processes: ", listOfProcesses
print "ArrivalTimes: ", ArrivalTimes
print "ExecutionTimes: ",ExecutionTimes
print "\n"

######SJF######
print "\n"
print "######SJF######"
print "\n"


while numberOfProcesses != 0:
	
	temp = []
	for i in range(len(ArrivalTimes)):
		if ArrivalTimes[i] <= clock :
			temp.append(ExecutionTimes[i])

	minimumExecutionTime = min(temp)
	
	for j in range(len(ExecutionTimes)):
		if ExecutionTimes[j] == minimumExecutionTime:
			
			tmp = j
			for p in range(ExecutionTimes[j]):
				processPerClock.append(listOfProcesses[j])
			listOfProcesses.remove(listOfProcesses[j])
			
			ArrivalTimes.remove(ArrivalTimes[j])
			
	clock = clock + ExecutionTimes[tmp]
	ExecutionTimes.remove(ExecutionTimes[tmp])

	numberOfProcesses = numberOfProcesses - 1

print "processPerClock: ", processPerClock

		

waitingtimes = []
for i in range(len(copyOfListOfProcesses)):
	waitingtimes.append(processPerClock.index("p" + str(i)))

averageWaitingsTime = float(sum(waitingtimes))/len(copyOfListOfProcesses)

print "average waiting time: ", averageWaitingsTime

responseTimes = []
for i in range(len(copyOfArrivalTimes)):
	responseTimes.append(waitingtimes[i]-copyOfArrivalTimes[i])

averageResponseTime = float(sum(responseTimes))/len(copyOfArrivalTimes)

print "average response time: ", averageResponseTime

turnAroundTimes = []

for i in range(len(copyOfArrivalTimes)):
	turnAroundTimes.append((len(processPerClock) - processPerClock[::-1].index("p" + str(i)) - 1) - copyOfArrivalTimes[i])

averageTurnAroundTime = float(sum(turnAroundTimes))/len(copyOfArrivalTimes)

print "average turnAround time: ", averageTurnAroundTime

#for drawing charts using pychart

# from pychart import *
# theme.get_options()

# #We have 10 sample points total.  The first value in each tuple is
# #the X value, and subsequent values are Y values for different lines.
# data = []

# for i in range(len(processPerClock)):
# 	data.append((i,int(processPerClock[i][-1]),int(processPerClock[i][-1])))

# print "data: ", data



# # The format attribute specifies the text to be drawn at each tick mark.
# # Here, texts are rotated -60 degrees ("/a-60"), left-aligned ("/hL"),
# # and numbers are printed as integers ("%d"). 
# xaxis = axis.X(format="/a-60/hL%d", tic_interval = 10, label="clock(SJF)")
# yaxis = axis.Y(tic_interval = 1, label="number of process")

# # Define the drawing area. "y_range=(0,None)" tells that the Y minimum
# # is 0, but the Y maximum is to be computed automatically. Without
# # y_ranges, Pychart will pick the minimum Y value among the samples,
# # i.e., 20, as the base value of Y axis.
# ar = area.T(x_axis=xaxis, y_axis=yaxis, y_range=(0,None))

# # The first plot extracts Y values from the 2nd column
# # ("ycol=1") of DATA ("data=data"). X values are takes from the first
# # column, which is the default.
# plot = line_plot.T(label="foo", data=data, ycol=1, tick_mark=tick_mark.star)
# plot2 = line_plot.T(label="bar", data=data, ycol=2, tick_mark=tick_mark.square)

# ar.add_plot(plot, plot2)

# # The call to ar.draw() usually comes at the end of a program.  It
# # draws the axes, the plots, and the legend (if any).

# ar.draw()


#to produce a PDF chart, run python like below
#python cpuScheduling.py --format=pdf >cpuScheduling.pdf


####FCSF####
print "\n"
print "######FCSF######"
print "\n"

numberOfProcesses = 5
listOfProcesses = ["p0","p1","p2","p3","p4"]
ArrivalTimes = [0,1,3,1,0]
ExecutionTimes = [5,3,10,6,8]

clock = 0

processPerClock = []

while len(listOfProcesses) != 0:

	lenghtOfArrivalTimes = len(ArrivalTimes) 

	temp = []
	temp2 = []
	for i in range(lenghtOfArrivalTimes):
		if ArrivalTimes[i] <= clock:
			temp.append(ArrivalTimes[i])
	

	minimumArrivalTime = min(temp)

	
	for j in range(lenghtOfArrivalTimes):
		
		if ArrivalTimes[j] == minimumArrivalTime:

			for p in range(ExecutionTimes[j]):
				processPerClock.append(listOfProcesses[j])

			clock = clock + ExecutionTimes[j]
			temp2.append(j)

			
	for i in sorted(temp2, reverse = True):
		del ExecutionTimes[i]
		del ArrivalTimes[i]
		del listOfProcesses[i]


	numberOfProcesses = numberOfProcesses - 1

print "processPerClock: ", processPerClock


waitingtimes = []
for i in range(len(copyOfListOfProcesses)):
	waitingtimes.append(processPerClock.index("p" + str(i)))

averageWaitingsTime = float(sum(waitingtimes))/len(copyOfListOfProcesses)

print "average waiting time: ", averageWaitingsTime

responseTimes = []
for i in range(len(copyOfArrivalTimes)):
	responseTimes.append(waitingtimes[i]-copyOfArrivalTimes[i])

averageResponseTime = float(sum(responseTimes))/len(copyOfArrivalTimes)

print "average response time: ", averageResponseTime

turnAroundTimes = []

for i in range(len(copyOfArrivalTimes)):
	turnAroundTimes.append((len(processPerClock) - processPerClock[::-1].index("p" + str(i)) - 1) - copyOfArrivalTimes[i])

averageTurnAroundTime = float(sum(turnAroundTimes))/len(copyOfArrivalTimes)

print "average turnAround time: ", averageTurnAroundTime

# from pychart import *
# theme.get_options()

# #We have 10 sample points total.  The first value in each tuple is
# #the X value, and subsequent values are Y values for different lines.
# data = []

# for i in range(len(processPerClock)):
# 	data.append((i,int(processPerClock[i][-1]),int(processPerClock[i][-1])))

# print "data: ", data



# # The format attribute specifies the text to be drawn at each tick mark.
# # Here, texts are rotated -60 degrees ("/a-60"), left-aligned ("/hL"),
# # and numbers are printed as integers ("%d"). 
# xaxis = axis.X(format="/a-60/hL%d", tic_interval = 10, label="clock(FCSF)")
# yaxis = axis.Y(tic_interval = 1, label="number of process")

# # Define the drawing area. "y_range=(0,None)" tells that the Y minimum
# # is 0, but the Y maximum is to be computed automatically. Without
# # y_ranges, Pychart will pick the minimum Y value among the samples,
# # i.e., 20, as the base value of Y axis.
# ar = area.T(x_axis=xaxis, y_axis=yaxis, y_range=(0,None))

# # The first plot extracts Y values from the 2nd column
# # ("ycol=1") of DATA ("data=data"). X values are takes from the first
# # column, which is the default.
# plot = line_plot.T(label="foo", data=data, ycol=1, tick_mark=tick_mark.star)
# plot2 = line_plot.T(label="bar", data=data, ycol=2, tick_mark=tick_mark.square)

# ar.add_plot(plot, plot2)

# # The call to ar.draw() usually comes at the end of a program.  It
# # draws the axes, the plots, and the legend (if any).

# ar.draw()


#to produce a PDF chart, run python like below
#python cpuScheduling.py --format=pdf >cpuScheduling.pdf	


####LIFO####
print "\n"
print "######LIFO######"
print "\n"

numberOfProcesses = 5
listOfProcesses = ["p0","p1","p2","p3","p4"]
ArrivalTimes = [0,1,3,1,0]
ExecutionTimes = [5,3,10,6,8]

clock = 0

processPerClock = []

while len(listOfProcesses) != 0:

	lenghtOfArrivalTimes = len(ArrivalTimes) 

	temp = []
	temp2 = []
	for i in range(lenghtOfArrivalTimes):
		if ArrivalTimes[i] <= clock:
			temp.append(ArrivalTimes[i])
	

	maximumArrivalTime = max(temp)

	
	for j in range(lenghtOfArrivalTimes):
		
		if ArrivalTimes[j] == maximumArrivalTime:

			for p in range(ExecutionTimes[j]):
				processPerClock.append(listOfProcesses[j])
			tmp = j
			clock = clock + ExecutionTimes[j]
			break
			
			
	
	del ExecutionTimes[tmp]
	del ArrivalTimes[tmp]
	del listOfProcesses[tmp]


	numberOfProcesses = numberOfProcesses - 1

print "processPerClock: ", processPerClock


waitingtimes = []
for i in range(len(copyOfListOfProcesses)):
	waitingtimes.append(processPerClock.index("p" + str(i)))

averageWaitingsTime = float(sum(waitingtimes))/len(copyOfListOfProcesses)

print "average waiting time: ", averageWaitingsTime

responseTimes = []
for i in range(len(copyOfArrivalTimes)):
	responseTimes.append(waitingtimes[i]-copyOfArrivalTimes[i])

averageResponseTime = float(sum(responseTimes))/len(copyOfArrivalTimes)

print "average response time: ", averageResponseTime

turnAroundTimes = []

for i in range(len(copyOfArrivalTimes)):
	turnAroundTimes.append((len(processPerClock) - processPerClock[::-1].index("p" + str(i)) - 1) - copyOfArrivalTimes[i])

averageTurnAroundTime = float(sum(turnAroundTimes))/len(copyOfArrivalTimes)

print "average turnAround time: ", averageTurnAroundTime


# from pychart import *
# theme.get_options()

# #We have 10 sample points total.  The first value in each tuple is
# #the X value, and subsequent values are Y values for different lines.
# data = []

# for i in range(len(processPerClock)):
# 	data.append((i,int(processPerClock[i][-1]),int(processPerClock[i][-1])))

# print "data: ", data



# # The format attribute specifies the text to be drawn at each tick mark.
# # Here, texts are rotated -60 degrees ("/a-60"), left-aligned ("/hL"),
# # and numbers are printed as integers ("%d"). 
# xaxis = axis.X(format="/a-60/hL%d", tic_interval = 10, label="clock(LIFO)")
# yaxis = axis.Y(tic_interval = 1, label="number of process")

# # Define the drawing area. "y_range=(0,None)" tells that the Y minimum
# # is 0, but the Y maximum is to be computed automatically. Without
# # y_ranges, Pychart will pick the minimum Y value among the samples,
# # i.e., 20, as the base value of Y axis.
# ar = area.T(x_axis=xaxis, y_axis=yaxis, y_range=(0,None))

# # The first plot extracts Y values from the 2nd column
# # ("ycol=1") of DATA ("data=data"). X values are takes from the first
# # column, which is the default.
# plot = line_plot.T(label="foo", data=data, ycol=1, tick_mark=tick_mark.star)
# plot2 = line_plot.T(label="bar", data=data, ycol=2, tick_mark=tick_mark.square)

# ar.add_plot(plot, plot2)

# # The call to ar.draw() usually comes at the end of a program.  It
# # draws the axes, the plots, and the legend (if any).

# ar.draw()


#to produce a PDF chart, run python like below
#python cpuScheduling.py --format=pdf >cpuScheduling.pdf

			
####RR####

print "\n"
print "######RR######"
print "\n"

numberOfProcesses = 5
listOfProcesses = ["p0","p1","p2","p3","p4"]
ArrivalTimes = [0,1,3,1,0]
ExecutionTimes = [5,3,10,6,8]

clock = 0

processPerClock = []

#quantom = input("plz input quantom: ")

quantom = 2



AE = zip(ArrivalTimes,ExecutionTimes)
AE.sort()

ArrivalTimes_sorted = [ArrivalTimes for ArrivalTimes, ExecutionTimes in AE]

ExecutionTimes_sorted = [ExecutionTimes for ArrivalTimes, ExecutionTimes in AE]



Al = zip(copyOfArrivalTimes,listOfProcesses)
Al.sort()
listOfProcesses_sorted = [listOfProcesses for copyOfArrivalTimes, listOfProcesses in Al]


while len(listOfProcesses_sorted) != 0:

	flag = False

	
	for i in range(len(AE)):
		
		for j in range(quantom):
			if ExecutionTimes_sorted[i] > 0:

				ExecutionTimes_sorted[i] = ExecutionTimes_sorted[i] - 1
				processPerClock.append(listOfProcesses_sorted[i])

			else:
				newTmp = i
				flag = True
				break

	if flag == True:
		del ExecutionTimes_sorted[newTmp]
		del AE[newTmp]
		del listOfProcesses_sorted[newTmp]
		del ArrivalTimes_sorted[newTmp]

print "processPerClock: ", processPerClock




# waiting time for RR: finish time - arrival time - execution time


turnAroundTimes = []

for i in range(len(copyOfArrivalTimes2)):
	turnAroundTimes.append((len(processPerClock) - processPerClock[::-1].index("p" + str(i)) - 1) - copyOfArrivalTimes2[i])

averageTurnAroundTime = float(sum(turnAroundTimes))/len(copyOfArrivalTimes2)

print "average turnAround time: ", averageTurnAroundTime

waitingtimes = []
for i in range(len(copyOfListOfProcesses2)):
	waitingtimes.append(turnAroundTimes[i] - copyOfExecutionTimes[i])

averageWaitingsTime = float(sum(waitingtimes))/len(copyOfArrivalTimes2)

print "average waiting time: ", averageWaitingsTime

responseTimes = []
for i in range(len(copyOfArrivalTimes2)):
	responseTimes.append(waitingtimes[i]-copyOfArrivalTimes2[i])

averageResponseTime = float(sum(responseTimes))/len(copyOfArrivalTimes2)

print "average response time: ", averageResponseTime




# from pychart import *
# theme.get_options()

# #We have 10 sample points total.  The first value in each tuple is
# #the X value, and subsequent values are Y values for different lines.
# data = []

# for i in range(len(processPerClock)):
# 	data.append((i,int(processPerClock[i][-1]),int(processPerClock[i][-1])))

# print "data: ", data



# # The format attribute specifies the text to be drawn at each tick mark.
# # Here, texts are rotated -60 degrees ("/a-60"), left-aligned ("/hL"),
# # and numbers are printed as integers ("%d"). 
# xaxis = axis.X(format="/a-60/hL%d", tic_interval = 10, label="clock(RR)")
# yaxis = axis.Y(tic_interval = 1, label="number of process")

# # Define the drawing area. "y_range=(0,None)" tells that the Y minimum
# # is 0, but the Y maximum is to be computed automatically. Without
# # y_ranges, Pychart will pick the minimum Y value among the samples,
# # i.e., 20, as the base value of Y axis.
# ar = area.T(x_axis=xaxis, y_axis=yaxis, y_range=(0,None))

# # The first plot extracts Y values from the 2nd column
# # ("ycol=1") of DATA ("data=data"). X values are takes from the first
# # column, which is the default.
# plot = line_plot.T(label="foo", data=data, ycol=1, tick_mark=tick_mark.star)
# plot2 = line_plot.T(label="bar", data=data, ycol=2, tick_mark=tick_mark.square)

# ar.add_plot(plot, plot2)

# # The call to ar.draw() usually comes at the end of a program.  It
# # draws the axes, the plots, and the legend (if any).

# ar.draw()


#to produce a PDF chart, run python like below
#python cpuScheduling.py --format=pdf >cpuScheduling.pdf
