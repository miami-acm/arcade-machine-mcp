import json

from mcp.game import Game


def _load_config(filename='config.json'):
	with open(filename, 'r') as json_file:
		config = json.load(json_file)

	return config


def load_games(filename='config.json'):
	config = _load_config(filename)
	games = [Game(i['name'], i['command'], i['image']) for i in config['games']]

	return games
