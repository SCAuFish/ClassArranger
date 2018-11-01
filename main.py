'''
	This file contains the main method to run specific functions.
	For now its main role is as a tester for the methods completed
	@ author Cheng Shen
	@ email chs091@ucsd.edu
	'''

import topOrder
from loadFromFile import load_from_file as load

if __name__ == '__main__':
	input_file = 'course_list.txt'
	course_names, course_vertices = load(input_file)
	print("All input courses: "+str(course_names))
	ordering = topOrder.top_Ordering(course_vertices)
	print("Taking order: ")
	for vertex in ordering:
		print(vertex.element)