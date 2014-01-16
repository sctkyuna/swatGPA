from bs4 import BeautifulSoup
import mechanize
from getSource import *

gradeValues = {"A+":4, "A":4, "A-":3.67, "B+":3.33, "B":3.0, "B-":2.67, "C+":2.33, "C":2.0, "C-":1.67, "D+":1.33, "D":1.0, "D-": 0.67, "F":0.0}

#TODO: Add shadow grades and major GPA option
#TODO: Check Haverford's grading system
#TODO: MAKE A WEB APP?!?


def main():

	soup = getSoup()
	
	# Obtain number of semesters
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

def getSoup():
	"""
	Option 0: user provides source code to Grades at a Glance webpage
	Option *: user enters username and password
	"""
		
	option = raw_input("\nEnter 0 to provide your own source code. Enter anything else to provide authentication (recommended): ")
	
	if option == "0":
		return getSource()
	
	else:
		source = navToPage()
		return BeautifulSoup(source)


def getSource():
	"""
	Retrieves user-provided source code.
	"""
	
	sourceFile = False
	
	while not sourceFile:
		try:
			fileName = raw_input("\nEnter source code file name here (e.g. myswat.html): ")
			sourceFile = open(fileName, "r")
		except IOError:
			print "File could not be found. Please try again."
	
	source = sourceFile.read()

	return BeautifulSoup(source)


def getData(numSem, grades, soup):
	"""
	Fills in dictionary "grades" with key "letter grade" and value "credit value"
	"""
	
	# For each semester, grabs letter grades and credit value.
	for i in range(numSem):
		CRED_ATT = "CRED_ATT_%03i" %i
		LETTER = "GRADE_%03i" %i
		curSemCred = soup.findAll('td', headers=CRED_ATT) #e.g. [0.5, 1, 1.5, 1]
		curSemLetter = soup.findAll('td', headers=LETTER) #e.g. [A, A, A-, B+]
		for j in range(len(curSemCred)):
			letter = curSemLetter[j].text
			# If letter conforms to a grade (e.g. not CR or NC).
			if letter in gradeValues:
				cred = float(curSemCred[j].text)
				grades[letter] = grades.setdefault(letter, 0.0) + cred
			else:
				# To check if letter is a 3.0, 3.33, etc (Bryn Mawr's system)
				try:
					val = float(letter)
				except ValueError:
					continue
				cred = float(curSemCred[j].text)				
				grades[letter] = grades.setdefault(letter, 0.0) + cred
					

def calculateGPA(grades):
	total = 0 # total additive value of grades
	count = 0 # total number of letter grades received

	for item in grades:
		num = grades[item] # number of letter grade received
		# If KeyError, probably a Bryn Mawr grade
		try:
			total += gradeValues[item] * num 	
		except KeyError:
			total += float(item) * num
		count += num 
	return "\nYour GPA: %f\n" % (total/count)



if __name__ == "__main__":
	main()
