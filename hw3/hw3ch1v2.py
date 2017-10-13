#Code for Challenge#1_Homework3
#Financial analisys 

#10_01_17: Result: The file is created but only has rows, it does not have any data


#Order of the task: 
#1. Merging the files (importing libraries, open files, and creating a new file)
#1.1 To create the new file use in the column 1(date), separator "-" to get the month


#1.1 importing libraries 
import os
import csv
#import pandas as pd
#import numpy as np
#import seaborn

#1.2 Importing data
#Name files with no spaces
data1 = os.path.join('Resources', 'budget_data_1.csv')
data2 = os.path.join('Resources', 'budget_data_2.csv')

#1.3 Creating lists to new file 
#newdate = []
datemonth = []
dateyear = []
revenue = []
revenueTwo = []

#1.4 using with to create the new file 
#firts: testing with one 

cvsfiles = [data1, data2]

for file in cvsfiles:
	
	with open(file, newline="") as cvsfileone:
		csvreaderone = csv.reader(cvsfileone, delimiter = ",")
		#creating the for loop to read all the rows in budget_data_1
		for row in csvreaderone: 
			#Using .append to add whatever needs to be add to the lists date = [] and revenue = []
			#1.4.1 as to count month separete than day, I will separate them  
			newdate = row[0].split("-")
			#to test out if new date is actually splitting. The answer is YES! 
			#print(newdate)
					
			#1.4.2 .append the revenue 
			revenue.append(row[1])
			
			dateyear.append(newdate[0])

			# for this one I got an error : list index out of range - it was because the data has different size
			datemonth.append(newdate[1])


#printing variables 
#Result : All printed - and working 
#print(revenue) 
#print(datemonth)
#print(dateyear)


#2. Calculate

#2.1 The total number of months included in the dataset
numberMonths = len(datemonth)
print (numberMonths)

#2.2 The total amount of revenue gained over the entire period
#removing header from revenue 
#revenue.remove("Revenue")
#revenue.pop([0])
#print(revenue)

# changing revenue as integer 
#list comprenhension: for i (each value that finds)
# type ---- command to get tha type of object 

for i in revenue:
	if i == "Revenue":
		revenue.remove("Revenue")
		#print("found it")
	else: 	
		revenueTwo.append(int(i)) 

#print (revenueTwo)

#calculating total amount of revenue

TotalRevenue = sum(revenueTwo)
print (TotalRevenue)
	
#2.3 The average change in revenue between months over the entire period
#creating a function to calculate the average 

def average (list1):
     
     suma = sum((i) for i in list1)
     #if suma == 0:
     	#suma = sum((i+1) for i in list1) 
     average = suma / len(list1)
     return average  

print (average(revenueTwo))

#2.4 The greatest increase in revenue (date and amount) over the entire period

print (max(revenueTwo))

#2.5 The greatest decrease in revenue (date and amount) over the entire period

print (min(revenueTwo))



#1.5 Zipping into a new file
#Zip is an iterator in pandas so to create the data frame, I have to create them as lists. 

#combinedcsv = list(zip(datemonth, dateyear, revenue))
#print(combinedcsv)
#trying without creating a list 
'''
combinedcsv = zip(datemonth, dateyear, revenue)

# 1.6 Set variable for output file
outputfile = os.path.join("budget_data_final.csv")

# 1.7 Open the new file
# w: argument that allows writting  
with open(outputfile, "w", newline="") as csvfinal:
	writer = csv.writer(csvfinal)

	#to add headers'
	writer.writerow(["day", "month", "revenue"])

	#write in zipped rows
	writer.writerow(combinedcsv)
	#Result - it is printing as rows not as columns (???)
	#So how can I include the printing as rows ? 
	#writer.writerow(combinedcsv) // pd.DataFrame(combinedcsv)
''' 











#3. Work with Pandas - no valid for this assignment 

#This allows me to create columns 
#dataframestocks = pd.DataFrame(combinedcsv)
#print(dataframestocks)
#Test_Pivot_Table
#dataframestocks.pivot(index='month', values='revenue')





#for i 

#The total amount of revenue gained over the entire period


#totalAverage = sum(dataframestocks[3])
#print(totalAverage) 

 
#sum(int(revenue)
#print(TotalRevenue)

#The average change in revenue between months over the entire period
#The greatest increase in revenue (date and amount) over the entire period
#The greatest decrease in revenue (date and amount) over the entire period


#QUESTIONS FOR CLASS
# Files written as columns - there is a simpler way?
# To do operations with columns and calling the column - See these two examples: 
#The total number of months included in the dataset
'''
countMonth = 0
for i in dataframestocks: 
	if dataframestocks[0:i] > dataframestocks[0:i + 1]
	countMonth = countMonth + 1 
#The total amount of revenue gained over the entire period
for i in dataframestrocks:
	totalAverage = sum(dataframestocks[3])
print(totalAverage)
'''
