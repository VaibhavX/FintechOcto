from sys import exit

def gold_room() :
	print "This room be full of gold me hearty. How much do you take?"
	next = raw_input('> ')
	if "0" in next or "1" in next:
		how_much = int(next)
	else :
		dead("Man, learn to type a fucking number!")

	if how_much < 50 :
		print "You're not greedy! You win!"
		exit(0)
	else :
		dead("You greedy bastard!")

def bear_room():
	print "There be a bear here. \n He has a bunch of honey. \n The fat bear is sitting in front of the door to the next room"
	print "How are you going to move the bear?"
	bear_moved = False
	while True :
		next = raw_input('> ')
		if next == "take honey" :
			dead("The bear looks at you and slaps your face off")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go to the next room now!"
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear got pissed off. He chews your legs and lets you die. You moron!")
		elif next == "open door" and bear_moved:
			gold_room()
		elif next == "open door" and not bear_moved :
			dead("The bear rolls over you and kills you with it's weight.")
		else :
			print "I got no idea what that means matey"
			bear_room()

def cthulu_room():
	print "The great dark lord cthulu doth cast his gaze upon thy dimunitive frame."
	print "His gaze do be rendering you insane slowly."
	print "Does thou runst or eatst your head?"
	next = raw_input('> ')
	if 'flee' in next :
		start()
	elif 'head' in next :
		dead("Thou eatst your own head!! Thou art insane")
	else :
		print "I got no idea what that means matey"
		cthulu_room()

def dead(why) :
	print why, "Good fucking job buddy!"
	exit(0)

def start():
	print "You find yourself in a dark room."
	print "As your eyes adjust to the darkness, you see two doors.\n One to the left and one to the right."
	print "Which door would you take?"

	next = raw_input('> ')

	if next == 'left':
		bear_room()
	elif next == 'right':
		cthulu_room()
	else :
		dead("Your mind is slowly consumed by the madness that is brought on by loneliness.")

start()