from bs4 import BeautifulSoup
import mechanize
from getSource import *

gradeValues = {"A+":4, "A":4, "A-":3.67, "B+":3.33, "B":3, "B-":2.67, "C+":2.33, "C":2, "C-":1.67, "D+":1.33, "D":1, "D-": 0.67, "F":0}


def main():

	#soup = getFile()
	source = navToPage()
	soup = BeautifulSoup(source)

	semesters = soup.findAll('td', id="REG_TERM_DESC")
	numSem = len(semesters)
	grades = {}

	for i, sem in enumerate(semesters):
		# Disregard "Prior to Matriculation" semester
		if "Prior" in sem.text:
			numSem -= 1
			break
	
	getData(numSem, grades, soup)

	print calculateGPA(grades)



def getData(numSem, grades, soup):

	for i in range(numSem):
		CRED_ATT = "CRED_ATT_%03i" %i
		LETTER = "GRADE_%03i" %i
		curSemCred = soup.findAll('td', headers=CRED_ATT)
		curSemLetter = soup.findAll('td', headers=LETTER)
		for j in range(len(curSemCred)):
			letter = curSemLetter[j].text
			if letter in gradeValues:
				cred = float(curSemCred[j].text)
				grades[letter] = grades.setdefault(letter, 0.0) + cred
	
def calculateGPA(grades):
	total = 0
	count = 0	
	for item in grades:
		num = grades[item]
		total += gradeValues[item] * num
		count += num 

	return "\nYour GPA: %f\n" % (total/count)


"""
def getFile():
	#Use this method if you have the source file.
	
	gpafile = ""

	while gpafile == "":
		try:
			fileName = raw_input("\nPlease input the name of the 'Grades at a Glance' source code file (e.g. index.html): ")
			gpafile = open(fileName, "r")	
		except IOError:
			print "\nFile does not exist. Try again."

	doc = gpafile.read()

	return BeautifulSoup(doc)

"""


main()
