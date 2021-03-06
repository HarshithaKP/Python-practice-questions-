#  Implement a program to find the square root of a function using newton-rapson method.
# babylonial method for finding square root of a number (derived from newton-rapson method)
# 1 Start with an arbitrary positive start value x (the closer to the root, the better).
# 2 Initialize y = 1.
# 3. Do following until desired approximation is achieved.
#   a) Get the next approximation for root using average of x and y
#   b) Set y = n/x

def square_root(n):
	x = n 
	y = 1
	e = 0.000000000000001

	while(x-y > e):
		x = (x+y)/2
		y = n/x
	return x

def main():
	try:
		n = int(input("Enter a number :"))
		print(" Square root is: \n", square_root(n))
	except:
		print("Enter a valid number")



if __name__=="__main__":
	main()
