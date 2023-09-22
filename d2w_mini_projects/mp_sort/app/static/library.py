from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number,seed):
    ls = []
    for i in range(0,number):
        ls.append(i)
    random.seed(seed)
    random.shuffle(ls)
    return ls

#Qi Xiang
def generate():
    number = 10
    seed = 200
    array = gen_random_int(number,seed)   
    array_str = ','.join(map(str, array))      
    array_str += "."
    document.getElementById("generate").innerHTML = array_str

#Joe
def sortnumber1():
	ls_str = document.getElementById("generate").innerHTML
	# remove full stop, split by ',', map int to str objects in ls
	ls_str = ls_str[:-1]
	ls_str = ls_str.split(",")
	ls_int = list(map(int,ls_str))
	
	#bubble sort v4
	n = len(ls_int)
	swapped = True
	while swapped:
		swapped = False
		new_n = 0
		for idx in range(1, n):
			if ls_int[idx-1] > ls_int[idx]:
				ls_int[idx - 1], ls_int[idx] = ls_int[idx], ls_int[idx - 1]
				swapped = True
				new_n = idx
		n= new_n    
	
	# convert all the items into one single string by iterating str() into each element using map()
	array_str = ','.join(map(str, ls_int))
	document.getElementById("sorted").innerHTML = array_str

	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''

#Kaelen
def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return
	
	else:
		#Convert input string into list of ints
		array_str = value.split(",") #Splits input string into a list of numbers
		array_ls = [] #Creates an empty list

		for i in range(len(array_str)):
			if array_str[i] == '': #Weeds out empty list entries due to extra or trailing commas in input
				continue
			else:    
				array_str[i]=int(array_str[i].strip()) #Removes whitespace, converts each element to int type
				array_ls.append(array_str[i]) #Adds each element into array_ls

		#Function to perform optimized insertion sort
		def insertion_sort(ls):
			n = len(ls)
			
			#Outer loop iterates selection of temp var, moving progressively towards the right.
			for out_idx in range(1,n):
				inn_idx = out_idx
				temp = ls[inn_idx]

				#Inner loop compares terms on the left of temp.
				while inn_idx>0 and ls[inn_idx-1]>temp:
				#Two possible termination conditions: inn_idx reaches 0 OR ls[inn_idx]<temp.

					ls[inn_idx-1], ls[inn_idx] = ls[inn_idx], ls[inn_idx-1] #Shift compared term to the right
					inn_idx -= 1 #Iterate inner loop backwards
			
			#Converts list back into string
			strg=", "
			strg=strg.join(str(i) for i in ls)
			return strg
	
		#Applies insertion_sort() onto array_ls, and assigns sorted list back into array_str
		array_str = insertion_sort(array_ls)

	document.getElementById("sorted").innerHTML = array_str


