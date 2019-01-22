import datetime
import random

class SexBuddy():

	def __init__(self, name):
		self.name = name
		self.exclusive = False
		self.start_of_punishment = datetime.date.today()
		self.num_sexy_times = 0

	def get_current_punishment_duration(self):
		return abs(datetime.date.today() - self.start_of_punishment)

	def update_emotional_advantage(self):
		return self.get_current_punishment_duration().days / 3

class Chu():

	def __init__(self):
		self.clean = True
		self.pregnant = False
		self.exclusive = False
		self.curr_emotional_advantage = 100
		self.sex_buddies = []
		self.exclusive_boytoy = None

	def exist(self):
		while (not self.exclusive and self.clean and not self.pregnant):
			self.sleep_around()
			for sb in self.sex_buddies:
				self.put_up_with(sb)
				emotional_advantage = sb.update_emotional_advantage()
				if (emotional_advantage > self.curr_emotional_advantage):
					self.become_exclusive_with(sb)
					break
				elif (self.pregnant):
					self.run_away()
					break;
					
	def run_away(self):
		self.exclusive_boytoy = None
		self.break_up_with_other_sex_buddies()

	def start_relationship_with(self, sex_buddy):
		self.sex_buddies.append(sex_buddy)

	def become_exclusive_with(self, sex_buddy):
		self.exclusive_boytoy = sex_buddy
		self.break_up_with_other_sex_buddies()
		self.exclusive = True
		print "You're the only one for me " + self.exclusive_boytoy.name

	def break_up_with(self, sex_buddy):
		self.sex_buddies.remove(sex_buddy)
		del sex_buddy

	def break_up_with_other_sex_buddies(self):
		for sb in self.sex_buddies:
			if (sb is not self.exclusive_boytoy):
				self.break_up_with(sb)

	def put_up_with(self, sex_buddy):
		sex_buddy.num_sexy_times += 1
		if (random.randint(1, 10000) == sex_buddy.num_sexy_times):
			print "Shit, it's positive:("
			self.pregnant = True

	def sleep_around(self):
		if (random.randint(1, 10000) == pow(len(self.sex_buddies), 3)):
			print "Mother fucker!"
			self.clean = False

def main():
	chu = Chu()
	chu.start_relationship_with(SexBuddy("#TheNewGuy"))
	chu.exist()

if __name__ == "__main__":
	main()





