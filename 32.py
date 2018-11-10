#  Implement a program to check the total number of students.
# (create a sample file with RegNo, StudentName, Branch)

import csv

def csv_file():
	f=open("file.csv","r")
	read=csv.reader(f,delimiter=",")
	data=list(read)
	len_data=len(data)-1
	print("Total number of students :",len_data)

def main():
	csv_file()

if __name__ == '__main__':
	main()
