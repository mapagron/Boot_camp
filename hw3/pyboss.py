#Challenge PyBoss
#General Info: 
#Columns: - Emp ID	Name	DOB	SSN	State
#Data_Format: - 214	Sarah Simpson	12/4/1985	282-01-8166	Florida

#1.1 importing libraries 
import os
import csv
from dateutil.parser import parse

#1.2 Import data
#Name files with no spaces
data1 = os.path.join('Resources\\employee_data1.csv')
data2 = os.path.join('Resources', 'employee_data2.csv')

#1.3 Creating lists to new file 
newdata = []
newName = []
newLastName = []
newDob = []
newSocial = []
newState = []
newDate = []

#1.4 using with to create the new file 

cvsfiles = [data1, data2]

for file in cvsfiles:
	
	with open(file, newline="") as cvsfileone:
		csvreaderone = csv.reader(cvsfileone, delimiter = ",")
		#creating the for loop to read all the rows 
		for row in csvreaderone: 
			#Using .append to add whatever needs to be add to the lists 
			#1.4.1 Separating name and last name from original column Name   
			newdata = row[1].split(" ")
			#to test out if new Name is actually splitting.  
			#print(newdata)
			
			#from newdata taking out the information for NewName and NewLastName
			newName.append(newdata[0])
			newLastName.append(newdata[1])

			#1.4.2 .append the date 
			# The DOB data should be re-written into DD/MM/YYYY format.
			# The currently format is 12/4/1985 and we want 04/12/1985 
			
			dob = row[2].split("/")
			#print(dob) -- it works! 
			dobSeparator = ["/"] * 1
			#print (dobSeparator)

			#newDate = dob.append(dob[1], dobSeparator[0], dob[0], dobSeparator[0], dob[2])
			# https://docs.python.org/2/tutorial/datastructures.html
			#newDate = dob.append(dob[1] + "/" + dob[0] + "/" + dob[2])
			#print (newDate)

			#1.4.3: #The SSN data should be re-written such that the first five numbers are hidden from view.
			
			#creating each number with an index so I can accesses it 
			ssnList = list(row[3])
			#print (ssnList) #it works 
			#changing item by item 
			ssnList[0] = "x" 
			ssnList[1] = "x"
			ssnList[2] = "x"
			ssnList[4] = "x"
			ssnList[5] = "x"
			#print(ssnList)
 
			#it works but does not work exactly 
			# it is a list within a list 
			newlist = sssList[1]+sssList[2]
			print (newlist)
			#newSocial.append(ssnList)
			#print(newSocial)


			#Social in an string print (type(newSocial))

			



			
