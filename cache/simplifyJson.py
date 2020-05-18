import json
import jsonpickle
from osrsbox import monsters_api

monsters = monsters_api.load()

monsterNames = []
monstersNoDupes = []
	
for monster in monsters:
	if monster.duplicate is False:
		if monster.name not in monsterNames:
			monstersNoDupes.append(monster)
			monsterNames.append(monster.name)
		
	
with open("monsters-cache.json", "w") as write_file:
	write_file.write(jsonpickle.encode(monstersNoDupes))