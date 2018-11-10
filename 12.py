#  Implement a program with lamda functions, for finding the area of circle, triangle, square.
import sys

def main():
	print("Lambda function")
	while True:
		print("1 : Area of a Circle")
		print("2 : Area of a Triangle")
		print("3 : Area of a Square")
		print("q : Exit")
		option=input("Enter your choise :")
		if option=='1':
			r=float(input("Enter the radius :"))
			a=lambda r:3.1415*r*r
			print(a(r))
		if option=='2':
			b=float(input("Enter the base :"))
			h=float(input("Enter the height :"))
			a=lambda b,h: 0.5*b*h
			print(a(b,h))
		if option=='3':
			s=float(input("Enter the length of side :"))
			a=lambda s: s*s

			print(a(s))
		if option=='q':
			sys.exit()
		else:
			print("Wrong choise ")

if __name__ == '__main__':
	main()
