# Print the pyramid pattern using .

def print_pyramid(num):
	for i in range(0,num):
		for j in range(0,i):
			print(".",end='')
		print(" ")

def main():
	num=int(input("Enter the number of rows :"))
	print_pyramid(num)
	

if __name__ == '__main__':
	main()