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
	number = 10 #preset
    seed = 200 #preset

    # call gen_random_int() with the given number and seed
    # store it to the variable array
    array = gen_random_int(number,seed)

    # convert all the items into one single string by iterating str() into each element using map() 
    # the numbers should be separated by a comma
    # and a full stop should end the string
    array_str = ','.join(map(str, array))      
    array_str += "."

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str

#Joe
def sortnumber1():
	document.getElementById("generate").innerHTML = ls_str
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

	# Your code should start from here
	# store the final string to the variable array_str
	pass

	array_str = None

	document.getElementById("sorted").innerHTML = array_str


