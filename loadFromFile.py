'''
	This file contains the method to read the prerequite information from a file
	and output a set of all the vertices
	The file should be in the foramt as follows:
	8B: 8A
	30: 12, 15L
	@ author Cheng Shen
	@ email chs091@ucsd.edu
	'''

from topOrder import Vertex

def load_from_file(filename):
	# This method parses an input file with the desiganted format
	input = open(filename, 'r')
	information_lines = input.readlines()

	# Load vertices
	vertices = {}
	for line in information_lines:
		line = line.strip()
		vertex_name, incoming_vertex_names = line.split(':')
		vertex_name = vertex_name.strip()
		incoming_vertex_names = incoming_vertex_names.strip()
		if len(vertex_name) == 0:
			continue

		if vertex_name in vertices:
			add_incoming_set(vertices, vertex_name, incoming_vertex_names)
		else:
			vertices[vertex_name] = Vertex(vertex_name)
			add_incoming_set(vertices, vertex_name, incoming_vertex_names)

	return set(vertices.keys()),set(vertices.values())

def add_incoming_set(vertices, vertex_name, incoming_vertex_names):
	vertex = vertices[vertex_name]
	incoming_vertex_names = incoming_vertex_names.split(',')
	for name in incoming_vertex_names:
		name = name.strip()
		if len(name) == 0:
			continue

		if name in vertices:
			# Add each other if the incoming vertex already exists
			vertex.incoming_set.add(vertices[name])
			vertices[name].outgoing_set.add(vertex)
		else:
			vertices[name] = Vertex(name)
			vertex.incoming_set.add(vertices[name])
			vertices[name].outgoing_set.add(vertex)
