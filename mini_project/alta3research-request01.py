#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

#at least two endpoints
#at least one of your endpoints should return JSON
#has ONE additional feature from the following list:
#	one endpoint returns HTML that uses jinja2 logic
#	requires a session value be present in order to get a response
#	writes to/reads from a cookie
#	reads from/writes to a sqlite3 database

app = Flask(__name__)

data = [
        {
            'name': 'Crucible',
            'gp_wealth': 816000000,
            'quest_points': 286,
            'pets': [
                {'name': 'heron',
                    'image': 'https://oldschool.runescape.wiki/images/thumb/Heron_%28follower%29.png/280px-Heron_%28follower%29.png?1a8a8'},
                {'name': 'squirrel',
                    'image': 'https://oldschool.runescape.wiki/images/thumb/Giant_squirrel_%28follower%29.png/240px-Giant_squirrel_%28follower%29.png?6927a'},
                {'name': 'cat',
                    'image': 'https://oldschool.runescape.wiki/images/thumb/Cat_%28grey_and_black%29.png/180px-Cat_%28grey_and_black%29.png?ae447'},
                {'name': 'rock',
                    'image': 'https://oldschool.runescape.wiki/images/thumb/Pet_rock_detail.png/120px-Pet_rock_detail.png?c8bbf'},
                {'name': 'monkey',
                    'image': 'https://oldschool.runescape.wiki/images/thumb/Monkey_%28Monkey_Madness_II%29_equipped.png/120px-Monkey_%28Monkey_Madness_II%29_equipped.png?2b882'},
                {'name': 'fish',
                    'image': 'https://oldschool.runescape.wiki/images/thumb/Fishbowl_%28blue%29_detail.png/110px-Fishbowl_%28blue%29_detail.png?0b99a'}
                ],
            'inventory': ['yew logs', 'infernal axe', 'teleport tablet'],
            'stats': {
                'attack': 86,
                'strength': 94,
                'defence': 86,
                'magic': 90,
                'ranged': 94,
                'prayer': 80,
                'hitpoints': 95
                }
            },
        {
            'name': 'steveXXX117',
            'gp_wealth': 350,
            'quest_points': 50,
            'pets': [],
            'inventory': ['bread', 'dough', 'chef hat'],
            'stats': {
                'attack': 40,
                'strength': 40,
                'defence': 1,
                'cooking': 90,
                'prayer': 99,
                'hitpoints': 60
                }
            },
        {
            'name': 'randy bo bandy',
            'gp_wealth': 50000,
            'quest_points': 109,
            'pets': [
                {'name': 'squirrel',
                    'image': 'https://oldschool.runescape.wiki/images/thumb/Giant_squirrel_%28follower%29.png/240px-Giant_squirrel_%28follower%29.png?6927a'}],
            'inventory': ['bread', 'beef', 'cheese'],
            'stats': {
                'attack': 30,
                'strength': 55,
                'defence': 50,
                'cooking': 99,
                'prayer': 60,
                'hitpoints': 60,
                'agility': 64
                }
            }

        ]



@app.route("/")
def player():
    return data

@app.route("/view/<int:player>")
def pets(player):
    return render_template("pets.html", petInfo = data[player]['pets'], playerStats = data[player]['stats'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
