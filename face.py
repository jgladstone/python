# Josh Gladstone
# Section B04
# marquis.gladstone@gatech.edu / GTID: 902985753
"""I worked on the homework assignment alone,
using only this semester's course materials."""


from Graphics import *

win = Window("Face", 400, 400)
#face
circle = Circle((200,200), 200)
circle.fill = Color("Yellow")
circle.draw(win)

#eyes
eye1 = Circle((100,125), 40)
eye1.fill = Color("White")
eye1.draw(win)
pupil1 = Circle((100,125), 20)
pupil1.fill = Color("Red")
pupil1.draw(win)


eye2 = Circle((300,125), 40)
eye2.fill = Color("White")
eye2.draw(win)
pupil2 = Circle((300,125), 20)
pupil2.fill = Color("Red")
pupil2.draw(win)

#Nose
nose = Polygon((200,150),(250,230),(160, 230))
nose.fill = Color("Blue")
nose.draw(win)

#Mouth
mouth = Curve((50,250),(200,375),(250,350),(350,250))
mouth.draw(win)

#Tattoo
tattoo1 = Rectangle((30,207),(100,222))
tattoo1.draw(win)
tattoo2 = Circle((50,191), 15)
tattoo2.draw(win)
tattoo3 = Circle((82,191), 15)
tattoo3.draw(win)