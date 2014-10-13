# -*-coding:UTF-8 -*
import csv
import config
import xml.etree.ElementTree as ET
 
class Roster:
	"""Class which define a roster with followings parameters :
	- a race
	- players title
	- reroll cost"""

	races = []
	

	def __init__ (self):
		"""Load all the rosters"""
		self.tree = ET.parse('Reference-Roster.xml')
		self.root = self.tree.getroot()
		for self.line in self.root:
			Roster.races.append(self.line.attrib['race'])
	
	def get_roster(self, race):
		"""choose a roster"""
		all_player = []
		for line in self.root.findall('team'):
			if line.get('race') == race:
				self.choosen_roster=line
				describe = []
				for player in line.findall('player'):
					describe.append(player.get('title'))
					describe.append(player.find('movement').text)
					describe.append(player.find('movement').text)
					describe.append(player.find('movement').text)
					describe.append(player.find('movement').text)
					carac = player.find('movement').text+' '+player.find('strength').text+' '
					skills = player.find('skills').text

					all_player.append()
		return all_player
