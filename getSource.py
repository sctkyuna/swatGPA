import mechanize
import getpass
import re

def navToPage():

	br = mechanize.Browser()
	
	# Browser options
	br.set_handle_equiv(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	
	r = br.open('https://myswat.swarthmore.edu/pls/twbkwbis.P_WWWLogin')
	br.select_form(nr=0)

	br.form["sid"] = raw_input("Username: ")
	br.form["PIN"] = getpass.getpass("Password: ")
	
	results = br.submit().read()

	#TODO: Figure out how to handle wrong password/username combos	

	link = ""
	
	for link1 in br.links():
		if link1.text == "Student Main Menu":
			link = link1
			break

	response1 = br.follow_link(link)

	for link2 in br.links():
		if link2.text == "Student Records":
			link = link2
			break

	response2 = br.follow_link(link)

	for link3 in br.links():
		if link3.text == "Grades at a Glance":
			link = link3
			break
	
	response3 = br.follow_link(link)

	tempLink = response3.read()

	finalLink = re.search(r'https.*?"', tempLink).group()[:-1]

	br.addheaders = [('Referer', 'https://myswat.swarthmore.edu/pls/pks_apex_myswat_authentication.apex_unofficial_grades')]	
	response4 = br.open(finalLink)

	return response4.read()


navToPage()
