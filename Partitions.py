#----------------------------------------------------------
"""
UNIVERSIDAD DEL VALLE DE GUATEMALA
Matemática Discreta - 10

	Program made by : 
		- Saúl Contreras (SuulCoder)
			18409


	The following program calculates the 
	partitions of an integer object.

		Input:
			N value of the integer
			K length of the partitions returned

		Output:
			All the partitions that satisfies
			the input parameters
"""
#----------------------------------------------------------

import itertools
from itertools import combinations_with_replacement

#----------------------------------------------------------

def printPartition(partition):
	toPrint = str(partition[0])
	count = 0
	for number in partition:
		if count!=0:
			toPrint += " + " + str(number)
		count+=1
	return toPrint 

def getPartition(N,k):
	"""
		This fucntion will calculate the partitions of 
		the given integer N that has k numbers
	"""
	partitions = ""
	options = []
	for i in range(1,N):
		options.append(i)
	combinantions = list(combinations_with_replacement(options,k))			#Generate all combinantions of lenght k with the possible values
	for i in combinantions:
		total = 0
		for number in i:														#Check all those whose total is N
			total+=number
		if(total==N):
			partitions+=printPartition(i)+","
	return partitions.split(',')

#----------------------------------------------------------

print("""

-----------------------------------------------------------
                     Partition getter	
-----------------------------------------------------------
	The following program calculates the 
	partitions of an integer


	""")
N = 0
k = 0
blocked = True
while(blocked):																			#Deffensive program.
	try:
		N = int(input("Write value N: The value of the integer:\t"))					#Getting N
		blocked = False
	except Exception as e:
		print("Write an integer number\n")
blocked = True
while(blocked):
	try:
		k = int(input("Write k: the length of the partitions returned\t"))				#Getting K
		if(N>k):
			blocked = False
		else:
			print("Write a valid k\n")
	except:
		print("Write an integer number\n")

print("\n Partitions of " + str(N) + " of " + str(k) + "-length:\n\n")					#Output design
print("\tProcessing Data...	Wait\n\n")
partitions = getPartition(N,k)
data = []
for partition in partitions:															#Split to get a list and have data in arrays
	partition.split("+")
	data_ = []
	for i in partition.split("+"):
		try:
			data_.append(int(i))
		except:
			pass
	data.append(data_)
for part in data:																		#Sort each partition to eliminate repeated ones
	part.sort(reverse=True)
data.sort(reverse=True)
partitions = list(data for data,_ in itertools.groupby(data))
partitions.pop(-1)																		#There will be always an empty list so we will delete it
for partition in partitions:
	print("\t"+printPartition(partition))	 
