# Find the names ending with N and their count. 

import csv

def main():

    # 'a+' opens a file for both reading and writing and creates file if not exists
    with open('students.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        students = list()
        for row in csv_reader:
            if row['name'].endswith('N'):
                students.append(row['name'])

        

        print("\n There are ", len(students) ," students whose name ends with 'N':\n")

        if(len(students) > 0):
            print("---Names---")
            for name in students:
                print("   "+name)



if __name__=="__main__":
	main()