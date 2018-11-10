#  Implement a program to find the euclidean distance of two points. 

import math

def euclidean_distance():
	p1=[3,4]
	p2=[4,9]
	print("Point 1:",p1)
	print("point 2:",p2)
	distance=math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
	print("Euclidean distance between two points is :",distance)

def main():
	euclidean_distance()

if __name__ == '__main__':
	main()