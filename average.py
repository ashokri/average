import csv
from statistics import mean

with open ('address to direcotry that contains csv file') as f:
    reader = csv.reader(f)
    for row in reader:
    
        
        name = row [0]
        these_grades = list()


        # task one: average all students and print their names and averages
        for grades in row[1:]:
            these_grades.append(int(grades))

        print(name, mean(these_grades))
        #end of task one

        #task two: print name in alphabatic order and the averges
        name_order = list()
        name_order = name.sorted()
        print(name_order)
