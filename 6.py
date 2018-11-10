#Create a list with 5 branches in SOIS. 
#Try to do the following operations a) append b) insert c) sort d) reverse sort 
import sys
SOIS=["CTV","EWT","BDA","CDA","VLSI","AES"]

def append_list(item):
	SOIS.append(item)
	print(SOIS)

def insert_list(pos,item):
	SOIS.insert(pos,item)
	print(SOIS)

def sort():
	SOIS.sort()
	print(SOIS)

def reverse_sort():
	SOIS.sort(reverse=True)
	print(SOIS)





def main():
	SOIS=["CTV","EWT","BDA","CDA","VLSI","AES"]
	print(SOIS)
	while True:
		print("1.Append")
		print("2.Insert")
		print("3.Sort")
		print("4.Reverse Sort")
		print("q.Quit")
		option=input("Enter your option :")
		if(option=='1'):
			item=input("Enter the branch to append ")
			append_list(item)
		elif(option=='2'):
			pos=int(input("Enter the position to insert "))
			item=input("Enter the branch to insert at :")
			insert_list(pos,item)
		elif(option=='3'):
			sort()
		elif(option=='4'):
			reverse_sort()
		elif(option=='q'):
			sys.exit()
		else:
			print("Enter the correct option ")

if __name__=='__main__':
	main()

