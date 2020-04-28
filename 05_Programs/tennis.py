import xml.etree.ElementTree as ET
import logging

def Logger():
	logging.basicConfig(filename="/storage/emulated/0/Python/tennis/player1.log", level=logging.DEBUG)
	
	return logging.getLogger("player1")
	


def create_XML():
	L1=[]
	text = "<data>\n\t<country name='Liechtenstein'>\n\t\t<rank>1</rank>\n\t\t<year first='2008' />\n\t\t<year second='2019' />\n\t\t<gdppc>141100</gdppc>\n\t\t<ball>*</ball>\n\t</country>\n</data>"

	L1=[text]

	Input=open("/storage/emulated/0/Python/tennis/country_data.xml", "w")
	for line in L1:
		Input.write(line + "\n")
	Input.close()
	
def create_Parse():
	tree = ET.parse("/storage/emulated/0/Python/tennis/country_data.xml")
	return tree.getroot() 
	

if __name__ == "__main__":

	player1=Logger()
	create_XML()
	root = create_Parse()
	
	
	for child in root:
		print(child.tag, child.attrib)
	
	for country in root.findall('country'):
		rank = country.find('rank').text
		name = country.get('name')
		print(name, rank)
	
	for year in root.iter('year'):
		print(year.attrib)
	
	for country in root.findall('country'):
		ball=country.find('ball').text
		if ball == "*":
			player1.info("*")
		print(ball)


#	myFile = "/storage/emulated/0/Python/tennis/country_data.txt"
#base = os.path.splitext(myFile)[0]
#os.rename(myFile, base + ".aln")
	

	