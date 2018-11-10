# Implement a program to create a list with two tuple of fruits and vegetables. 
#Access fruits separately and vegetables separately.

def list_of_tuples():
	mylist=[]
	mytuple1=('beens','aloo','carrot')
	mytuple2=('pappaya','orange','grapes')
	print("Empty list")
	print(mylist)
	mylist.append(mytuple1)
	print("List with one tuple",mylist)
	mylist.append(mytuple2)
	print("List with one tuple",mylist)
	print("Accessing the first tuple elements from the list ")
	print(mylist[0][2])
	print("Accessing the second tuple elements from the list ")
	print(mylist[1][0])
def main():
	list_of_tuples()

if __name__ == '__main__':
	main()