import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

# ❌ ⬆ DON'T CHANGE THE CODE ABOVE ⬆ ❌
def fire_gun():
	# ✅ ↓ your code here ↓ ✅
	chamber_position = spin_chamber()
	if chamber_position == bullet_position:
		print("you are dead!")
	else:
		print("keep playing!")
		
	return chamber_position



print(fire_gun())
