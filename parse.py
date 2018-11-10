# ---------------------
# Created by Don Andes |
# ---------------------------------------------------------------------------------------------------
# This program scrapes some common jobs websites and analyzes the output for keywords
# ---------------------------------------------------------------------------------------------------

import re
import sys
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable


jobSites = {
"Deloitte" : "https://jobs2.deloitte.com/us/en/Experienced-all-jobs?from=0&s=1&rk=l-experiencedalljobs", #First 50 results
"CACI" : "https://careers.caci.com/ListJobs/ByState/VA/Country-US/Page-1" #First 30 results
}


def parseSiteReturnNumResults(url, passedStringToSearchFor):
    stringToSeachFor = re.compile(passedStringToSearchFor, re.IGNORECASE)
    return stringToSeachFor.findall(BeautifulSoup(requests.get(url).text, 'html.parser').get_text())


if __name__ == '__main__':
	t = PrettyTable(['Company', 'Matches'])
	for key, value in jobSites.items():
		t.add_row([key, str(len(parseSiteReturnNumResults(value, sys.argv[1])))])
	t.align = "l"
	print t