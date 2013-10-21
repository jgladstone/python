#Kyle Grinstead/Josh Gladstone
#CS 1301 B04
#kylegrinstead@gatech.edu/marquis.gladstone@gatech.edu
#902983922/902985753
#We worked on this homework alone, using only this semester's course materials.

from Myro import *

init()

def makeWebPage(numberOfPictures):
	html = """
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
			<title>Myro Images</title>
		</head>
		<body>
			<h1>Welcome to the Myro Image Page!</h1>
			<p>Designed by Kyle Grinstead and Josh Gladstone</p>
			<table>
	"""

	for picNum in range(numberOfPictures):
		picName = "pic"+str(picNum)+".jpg"
		pic = takePicture()
		savePicture(pic, picName)
		avgLight = sum(getLight())/3
		turnRight(1,.25)
		if picNum % 4 == 0:
			html += "<tr>\n"
		html += "<td><img src='{}' width='50%' alt='{}' /><br /><p>{}</p></td>\n".format(picName,picName,avgLight)
		if (picNum + 1) % 4 == 0 or (picNum + 1) == numberOfPictures:
			html += "</tr>\n"

	html += """
			</table>
			<p>Pictures taken by {}.</p>
		</body>
	</html>
	""".format(getName())

	myPage = open("myPage.html", "w")
	myPage.write(html)
	myPage.close()