#  Implement a program to print the elements of a list.

def prin(mylist):
	print(mylist)

def main():
	mylist=[]
	n=int(input("Enter the total number of elements you wish to add to list :"))
	for i in range(0,n):
		element=input("Enter the element :")
		mylist.append(element)
	prin(mylist)

if __name__ == '__main__':
	main()