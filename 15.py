# Implement a function to implement to find the length of the list without standard library.

def mylist(list1):
	count=0
	for i in list1:
		count=count+1

	print("Length of the list is :",count)

def main():
	print("Function to find length of the list")
	list1=['a','b','c','d','e','f']
	print("List is",list1)
	mylist(list1)

if __name__ == '__main__':
	main()

