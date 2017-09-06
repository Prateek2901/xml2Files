"""
I need 
authors name
Title
Full title
Keywords
Year
Abstract
"""

import xml.etree.ElementTree as ET
tree = ET.parse('beautify.xml')
root = tree.getroot()
for i,record in enumerate(root.iter('record')):
	# Author
	a_name = []
	for author in record.iter('author'):
		a_name.append(author.text)

	print (a_name)
	# Title
	title = record.find('titles').find('title').text
	
	#Full Title
	full_title = record.find('periodical').find('full-title').text
	
	# Keyword
	key = []
	for keyword in record.iter('keyword'):
		key.append(keyword.text)

	print(key)
	# Year
	year = record.find('dates').find('year').text
	
	# Abstract
	if record.find('abstract') is None:
		abstract = 'NO ABSTRACT FOUND'
	else:
		abstract = record.find('abstract').text

	file_name = str(i+1)+"."+title+","+ year+".txt"
	output = open(file_name,"w")

	output.write("Name of authors:-\n%s\n\nTitle:-\n%s\n\nFull Title:-\n%s\n\nKeywords:-\n%s\n\nYear:-\n%s\n\nAbstract:-\n%s"% 
		("".join(a_name),title,full_title,"".join(key),year,abstract))
	print("Name of authors:-\n%s\n\nTitle:-\n%s\n\nFull Title:-\n%s\n\nKeywords:-\n%s\n\nYear:-\n%s\n\nAbstract:-\n%s"% 
		("".join(a_name),title,full_title,"".join(key),year,abstract))

	output.close()
	print ('\n----------------------------------------------------------------\n')