''' This file contains the algorithm of topological ordering
	@ author Cheng Shen
	'''

from queue import Queue

class Vertex:
	def __init__(self, elem, incoming_set = None, outgoing_set = None):
		self.incoming_set = set()
		self.outgoing_set = set()
		# Initialize with given data
		if incoming_set is not None:
			for incoming_vertex in incoming_set:
				self.incoming_set.add(incoming_vertex)
		if outgoing_set is not None:
			for ougoing_vertex in outgoing_set:
				self.outgoing_set.add(outgoing_vertex)

		self.element = elem

		# Add the object itself to the followings of its prerequisites
		if incoming_set is not None:
			for incoming_vertex in incoming_set:
				incoming_vertex.outgoing_set.add(self)

	def add_incoming(self, incoming_set):
		for incoming_vertex in incoming_set:
			self.incoming_set.add(incoming_vertex)
			incoming_vertex.outgoing_set.add(self)

	def add_outgoing(self, outgoing_set):
		for outgoing_vertex in outgoing_set:
			self.outgoing_set.add(outgoing_vertex)
			outgoing_vertex.incoming_set.add(self)

def top_Ordering(vertices):
	# find sources
	ordering = []
	sources = find_sources(vertices)

	while not sources.empty():
		toAdd = sources.get()
		ordering.append(toAdd)
		followers = toAdd.outgoing_set
		for follower in followers:
			follower.incoming_set.remove(toAdd)
			if len(follower.incoming_set) == 0:
				sources.put(follower)

	return ordering


def find_sources(vertices):
	result = Queue()
	for vertex in vertices:
		if len(vertex.incoming_set) == 0:
			result.put(vertex)

	return result

A = Vertex('8A')
B = Vertex('8B')
C = Vertex('12')
D = Vertex('15L')
E = Vertex('30')

B_pre = set()
B_pre.add(A)
C_pre = set()
C_pre.add(A)
C_pre.add(B)
D_pre = set()
D_pre.add(A)
D_pre.add(B)
E_pre = set()
E_pre.add(C)
E_pre.add(D)

B.add_incoming(B_pre)
C.add_incoming(C_pre)
D.add_incoming(D_pre)
E.add_incoming(E_pre)
vertices = [A,B,C,D,E]
ordering = top_Ordering(vertices)
for vertex in ordering:
	print(str(vertex.element)+" ")