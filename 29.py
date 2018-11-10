#  In a given list find the total number of odd numbers, even numbers and their respetive sum and average.

def even_and_odd(mylist):
	print("List : ",mylist)
	sum_even=0
	sum_odd=0
	even_list=[]
	odd_list=[]
	for i in mylist:
		if i%2==0:
			even_list.append(i)
			sum_even+=i
		else:
			odd_list.append(i)
			sum_odd+=i

	even_length=len(even_list)
	odd_length=len(odd_list)
	even_average=sum_even/even_length
	odd_average=sum_odd/odd_length

	print("Even numbers list is :",even_list)
	print("Odd numbers list is :",odd_list)
	print("Sum of even numbers :",sum_even)
	print("Sum of odd numbers :",sum_odd)
	print("Average of even numbers :",even_average)
	print("Average of odd numbers :",odd_average)

def main():
	mylist=[1,3,4,6,23,34,54,45,67,65,76,88,22]
	even_and_odd(mylist)

if __name__ == '__main__':
	main()


