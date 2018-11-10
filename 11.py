#  Implement a program with functions, for finding the area of circle, triangle, square.
import sys
def area_of_circle():
	r=float(input("Enter the radius of the circle :"))
	area=3.14*r*r
	print("Area of the circle with radius ",r,"is : ",area)

def area_of_triangle():
	b=float(input("Enter the base of the triangle :"))
	h=float(input("Enter the height of the triangle :"))
	area=0.5*b*h
	print("Area of the triangle is : ",area)

def area_of_square():
	s=float(input("Enter the length of any one side of a square :"))
	area=s*s
	print("Area of the square with side length ",s,"is : ",area)

def main():
	while True:
		print("1 : Area of a Circle")
		print("2 : Area of a Triangle")
		print("3 : Area of a Square")
		print("q : Exit")
		option=input("Enter your choise :")
		if option=='1':
			area_of_circle()
		if option=='2':
			area_of_triangle()
		if option=='3':
			area_of_square()
		if option=='q':
			sys.exit()
		else:
			print("Wrong choise ")

if __name__ == '__main__':
	main()

