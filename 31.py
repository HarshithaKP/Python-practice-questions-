#  Implement a program to check the elements of a list is a palindrome or not.

def palindrome(mylist,reverse_mylist):
	print(mylist)
	print(reverse_mylist)
	if mylist==reverse_mylist:
		print("Palindrome")

	else:
		print("Not a palindrome")

def main():
	mylist=[1,2,3,3,2,1]
	reverse_mylist=mylist
	reverse_mylist.reverse()
	palindrome(mylist,reverse_mylist)

if __name__ == '__main__':
	main()