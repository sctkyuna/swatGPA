import mechanize
import getpass
import re

#TODO: Add comments

def navToPage():

	br = mechanize.Browser()
	
	# Browser options
	br.set_handle_equiv(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	
	r = br.open('https://myswat.swarthmore.edu/pls/twbkwbis.P_WWWLogin')

	br = getLogin(br)

	response1 = br.follow_link(findLink(br, "Student Main Menu"))
	response2 = br.follow_link(findLink(br, "Student Records"))
	response3 = br.follow_link(findLink(br, "Grades at a Glance"))
	
	tempLink = response3.read()

	finalLink = re.search(r'https.*?"', tempLink).group()[:-1]

	# Spoof browser into thinking redirect is coming from myswat.
	br.addheaders = [('Referer', 'https://myswat.swarthmore.edu/pls/pks_apex_myswat_authentication.apex_unofficial_grades')]	
	response4 = br.open(finalLink)

	return response4.read()

def findLink(br, linkText):

	# Find link object by iterating through all links in page.
	for link in br.links():
		if link.text == linkText:
			return link

def getLogin(br):

	#TODO: Figure out how to handle wrong password/username combos		

	br.select_form(nr=0)

	br.form["sid"] = raw_input("\nUsername: ")
	br.form["PIN"] = getpass.getpass("Password: ")
	
	results = br.submit().read()

	return br

