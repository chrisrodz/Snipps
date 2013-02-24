"""
honeyComb.py
Christian A. Rodriguez Encarnacion 801-11-6705
Compter Science Challenge Problems #001

September 18, 2012

This program solves the Computer Science Challenge Problem Series #001

I save each pair of integers to solve the problem in parallel arrays, and accept input
until the combination integers 0 0 are entered.

First the program creates the honeycomb structure representing it as a graph.
I do this using a list of lists. Then I accept the user's input and save each
pair of numbers in parallel arrays. Lastly I iterate through these arrays calling
the pathCount function, which prints the number of steps in the shortest path from
a node A to a node B in my graph.
"""


""" USER INPUT """

print "Enter pairs of integers and I will solve the honeycomb problem for each pair."
print "Enter 0 0 to stop."

one = []  # For the first integers
two = []  # For the second integers

str = raw_input()
values = str.split()

while not(int(values[0]) == 0 and int(values[1]) == 0):  # Iterate until 0 0 is entered.
	one.append(int(values[0]))
	two.append(int(values[1]))
	str = raw_input()
	values = str.split()

print one # print the first integer list
print two # print the second integer list

""" CREATE THE HONEYCOMB """

MAX = 10000 # Max number of nodes in my graph

honey = [[2,3,4,5,6,7],[1,3,7,8,9,10],[1,2],[1],[1],[1],[1,2],[2],[2],[2]]
# To create the "honeycomb" structure I hardcode nodes 1 and 2 and every node
# they connect to

connect = 7 # Indicator variable

for i in range(1,2*MAX): # I create enough nodes to keep my honeycomb structure
	honey.append([])


# This for loop creates the rest of the graph. I iterate through each node and create
# an edge to all 6 of the other nodes it is supposed to connect with.

for i in range(2,MAX-1):
	while len(honey[i]) < 6: # Nodes can have a maximum of 6 edges
		if not(honey[i].count(i+2)): # All nodes are connected to the one next to them
			honey[i].append(i+2)
			honey[i+1].append(i+1)
		else: 
			honey[connect+i].append(i+1) # The connect variable helps me point to where
			honey[i].append(connect+i+1) # the node is supposed to connect
			connect = connect + 1
			
	connect = connect - 2



"""definition of pathCount()

This function accepts two integers 'first' and 'last' as arguments and will output 
the sentence: "The distance between cells 'first' and 'last' is 'count'."

If 'first' == 'last' we know 'count' is 0. Otherwise the function will execute the
following algorithm:
1. Increment 'count' by 1.
2. Save 'first' in an array.
3. Find all cells 'first' connects to and save them in an array.
4. Check if 'last' is there. If it is return 'count'.
5. If not then repeat step 1 with the array of all cells 'first' connects with.

Variables:
first = parameter; The first of the values to find the shortest path in the honeycomb
second = parameter; The second of the values to find the shortest path in the honeycomb
array1 = The array to hold the cells we find. Starts with 1 element, 'first'
array2 = The array we use to temporarily hold the cells array1 elements connect to
count = The number of steps from cell 'first' to cell 'second'
cond = A boolean flag to determine when the loop has finished
"""
def pathCount(first,second):
	
	if first == second:  # Trivial
		print 'The distance between cells',first,'and',second,'is 0'
		return
	
	array1 = [first] # Save 'first' in array1
	array2 = set() # Declare as empty set to automatically remove duplicates
	count = 0
	cond = 1

	while cond:
	
		count = count + 1
	
		for i in array1:
			array2 = array2 | set(honey[i-1]) # Add cells connected to array1
	
		array2 = array2 - set(array1) # Remove original array1 cells

		if second in array2:
			cond = 0
		else:
			array1 = list(array2) # Redefine array1 as array2 in list format
			array2 = set() # Redeclare as an empty set

	print 'The distance between cells',first,'and',second,'is',count
# End of function

""" CALL PATHCOUNT FOR EACH PAIR IN THE USER INPUT """

for i in range(0,len(one)):  # Iterate through all input values and call pathCount
	pathCount(one[i],two[i]) 

