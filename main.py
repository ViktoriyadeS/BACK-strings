# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Part 1
from gettext import find


player1 = "Ruud Gullit"
player2 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = player1 + " " + str(goal_0)+", "+player2 + " " + str(goal_1)
report = f"{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute"


print(report)

# Part 2

player = "Marcel van Basten"
first_name = player[:player.find(" ")]
last_name = player[player.find(" ")+1:]
last_name_len = len(last_name)

name_short = f"{first_name[0]}. {last_name}"
chant = (f"{first_name}! " * len(first_name)).rstrip(" ")
good_chant = chant != chant.endswith(" ")


print(good_chant)

