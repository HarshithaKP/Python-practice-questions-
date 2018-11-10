# Implement a program to create a dictionary of students with Registration number and names. 
# Perform the two operations, insert and delete.
import sys

mydict={181041001:'Harshitha',181041002:'Suman',181041003:'Pavana',181041004:'Priyanka'}

def insertion():
	key=int(input("Enter the Registration num :"))
	mydict[key]=input("Enter the Student name :")
	print(mydict)
def deletion():
	key=int(input("Enter the Registration num :"))
	del mydict[key]
	print(mydict)
def main():
	print(mydict)
	while True:
		print("1.Insertion ")
		print("2.Deletion ")
		print("q.Exit")
		option=input("Choose your option : ")
		if option=='1':
			insertion()
		elif option=='2':
			deletion()
		elif option=='q':
			sys.exit()
		else:
			print("Enter correct option")

if __name__ == '__main__':
	main()





