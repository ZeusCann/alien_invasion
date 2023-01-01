


class GameStats:
	"""Track statistics for Alien Invasion."""

	def __init__(self, ai_game):
		"""Initialize statistics."""
		self.settings = ai_game.settings
		self.reset_stats()

		# Start game in an inactive state.
		self.game_active = False

		# High score should never be reset.
		#   Add to reset_stats to reset high score.
		self.high_score = 0

		# Created a variable to hold and work with high_score.txt
		high_score = 'high_score.txt'

		# Records and Displays previous high score even after closing game
		#   by reading from the 'high_score.txt' file.
		with open(high_score) as file_object:
			contents = file_object.read()
		self.high_score += int(contents)

		# Start Alien Invasion in an active state.
		#self.game_active = True

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
